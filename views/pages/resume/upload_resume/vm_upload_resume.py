from .ui_upload_resume import *
from PySide6.QtWidgets import QFileDialog, QMessageBox
from workers.summarize_resume_worker import SummarizeResumeWorker
from common.imports.log import *


class UploadResumeFrame(QFrame):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_variables()
        self._init_event_handlers()

    def _init_variables(self):
        self.worker = None

    def _init_event_handlers(self):
        self.ui.frame_drop_area.dragEnterEvent = self.on_drag_enter
        self.ui.frame_drop_area.dropEvent = self.on_drop
        self.ui.frame_drop_area.mousePressEvent = self.on_mouse_press

    def on_drag_enter(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def on_drop(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith('.docx'):
                self._process_resume(file_path)
            else:
                QMessageBox.warning(self, "Warning", "Please select a .docx file.")

    def on_mouse_press(self, event):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CV File",
            "",
            "Word Files (*.docx);;All Files (*)",
            options=options
        )
        if file_path:
            self._process_resume(file_path)

    def _process_resume(self, file_path: str):
        """Process the resume file in a background thread."""
        if self.worker and self.worker.isRunning():
            QMessageBox.warning(self, "Warning", "Resume processing is already in progress.")
            return
        
        # Disable UI during processing (if you have a status label, update it here)
        logging.info(f"Starting resume processing: {file_path}")
        
        # Create and start worker thread
        self.worker = SummarizeResumeWorker(file_path)
        self.worker.signal_finished.connect(self._on_finished)
        self.worker.signal_error.connect(self._on_error)
        self.worker.signal_progress.connect(self._on_progress)
        self.worker.start()

    def _on_finished(self, summary_json_path: str):
        """Called when resume summarization is complete."""
        logging.info(f"Resume summarized successfully: {summary_json_path}")
        
        # Clean up worker
        if self.worker:
            self.worker.quit()
            self.worker.wait()
            self.worker = None
        
        QMessageBox.information(self, "Success", "Resume processed successfully!")

    def _on_error(self, error_msg: str):
        """Called when resume summarization fails."""
        logging.error(f"Resume summarization error: {error_msg}")
        
        if self.worker:
            self.worker.quit()
            self.worker.wait()
            self.worker = None
        
        QMessageBox.critical(self, "Error", f"Failed to process resume:\n{error_msg}")

    def _on_progress(self, message: str):
        """Called for progress updates."""
        logging.info(f"Progress: {message}")
        # Optionally update UI with progress message

