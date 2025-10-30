from PySide6.QtWidgets import QPushButton
from managers.file_manager import file_manager
from managers.chat_manager import chat_manager
from models.job import Job


class GenerateCoverLetterButton(QPushButton):
    def __init__(self, parent=None, job: Job = None):
        super().__init__("Cover Letter", parent)
        self.setObjectName("generate_cover_letter_button")
        self._init_style()
        self.job = job


    def _init_style(self):
        self.setStyleSheet("""
            QPushButton#generate_cover_letter_button {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
        """)


    def mousePressEvent(self, event):
        cv_text = file_manager.get_last_summary_json()
        result = chat_manager.generate_cover_letter(self.job, cv_text)
        file_manager.save_cover_letter_as_pdf(result, self.job.id)
        super().mousePressEvent(event)

