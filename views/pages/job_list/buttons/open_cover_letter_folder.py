from PySide6.QtWidgets import QPushButton, QMessageBox
from managers.file_manager import file_manager
from models.job import Job
from common.imports.log import *


class OpenCoverLetterFolderButton(QPushButton):
    def __init__(self, parent=None, job: Job = None):
        super().__init__("Open Folder", parent)
        self.setObjectName("open_cover_letter_folder_button")
        self._init_style()
        self.job = job


    def _init_style(self):
        self.setStyleSheet("""
            QPushButton#open_cover_letter_folder_button {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
        """)


    def mousePressEvent(self, event):
        try:
            file_manager.open_job_cover_letter_folder(self.job)
        except Exception as e:
            logging.error(f"Failed to open cover letter folder for job {self.job.id}: {e}")
            QMessageBox.critical(self, "Error", str(e))
        super().mousePressEvent(event)
