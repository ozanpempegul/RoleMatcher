from PySide6.QtWidgets import QPushButton
from managers.db import db_manager
from managers.file_manager import file_manager
from managers.chat_manager import chat_manager
from models.job import Job
import re


class TailorResumeButton(QPushButton):
    def __init__(self, parent=None, job: Job = None):
        super().__init__("Tailor", parent)
        self.setObjectName("tailor_resume_button")
        self._init_style()
        self.job = job


    def _init_style(self):
        self.setStyleSheet("""
            QPushButton#tailor_resume_button {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
        """)


    def mousePressEvent(self, event):
        cv_text = file_manager.get_last_summary_json()
        result = chat_manager.tailor_resume(self.job, cv_text)
        score = self.extract_match_score(result)
        db_manager.save_match_score(self.job.id, score)
        file_manager.save_tailored_resume_as_pdf(result, self.job.id)
        super().mousePressEvent(event)


    def extract_match_score(self, html_text: str) -> float | None:
        """
        Extract the matching score from HTML comment.
        Example comment: <!-- MATCHING_SCORE: 87 -->
        Returns the score as float, or None if not found.
        """
        match = re.search(r"<!--\s*MATCHING_SCORE:\s*(\d+(\.\d+)?)\s*-->", html_text)
        if match:
            return float(match.group(1))
        return None