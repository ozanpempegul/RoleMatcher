from PySide6.QtWidgets import QPushButton, QMessageBox
from managers.file_manager import file_manager
from workers.tailor_resume_worker import TailorResumeWorker
from models.job import Job
import json
from common.imports.log import *


class TailorResumeButton(QPushButton):
    def __init__(self, parent=None, job: Job = None):
        super().__init__("Tailor", parent)
        self.setObjectName("tailor_resume_button")
        self._init_style()
        self.job = job
        self.worker = None


    def _init_style(self):
        self.setStyleSheet("""
            QPushButton#tailor_resume_button {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
            QPushButton#tailor_resume_button:disabled {
                background-color: #95a5a6;
            }
        """)


    def mousePressEvent(self, event):
        if self.worker and self.worker.isRunning():
            return  # Already processing
        
        cv_data = file_manager.get_last_summary_json()
        if not cv_data:
            QMessageBox.warning(self, "Warning", "Please upload and summarize a resume first.")
            return
        
        # Convert dict to JSON string for the API
        cv_text = json.dumps(cv_data, ensure_ascii=False) if isinstance(cv_data, dict) else str(cv_data)
        
        # Disable button during operation
        self.setEnabled(False)
        self.setText("Tailoring...")
        
        # Create and start worker thread
        self.worker = TailorResumeWorker(self.job, cv_text)
        self.worker.signal_finished.connect(self._on_finished)
        self.worker.signal_error.connect(self._on_error)
        self.worker.signal_progress.connect(self._on_progress)
        self.worker.start()
        
        super().mousePressEvent(event)

    def _on_finished(self, html_result: str, match_score: float):
        """Called when resume tailoring is complete."""
        logging.info(f"Resume tailored successfully for job {self.job.id}, score: {match_score}")
        self.setEnabled(True)
        self.setText("Tailor")
        
        # Clean up worker
        if self.worker:
            self.worker.quit()
            self.worker.wait()
            self.worker = None
        
        QMessageBox.information(self, "Success", 
                               f"Resume tailored successfully!\nMatch Score: {match_score:.2f}%")

    def _on_error(self, error_msg: str):
        """Called when resume tailoring fails."""
        logging.error(f"Resume tailoring error: {error_msg}")
        self.setEnabled(True)
        self.setText("Tailor")
        
        if self.worker:
            self.worker.quit()
            self.worker.wait()
            self.worker = None
        
        QMessageBox.critical(self, "Error", f"Failed to tailor resume:\n{error_msg}")

    def _on_progress(self, message: str):
        """Called for progress updates."""
        logging.info(f"Progress: {message}")
        self.setText(message[:15] + "..." if len(message) > 15 else message)