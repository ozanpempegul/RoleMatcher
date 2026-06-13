from PySide6.QtCore import QThread, Signal
from managers.chat_manager import chat_manager
from managers.db import db_manager
from managers.file_manager import file_manager
from models.job import Job
import re
from common.imports.log import *


class TailorResumeWorker(QThread):
    """Worker thread for tailoring resume to a job description."""
    signal_finished = Signal(str, float)  # html_result, match_score
    signal_error = Signal(str)
    signal_progress = Signal(str)

    def __init__(self, job: Job, cv_text: str):
        super().__init__()
        self.job = job
        self.cv_text = cv_text

    def run(self):
        try:
            logging.info(f"Starting resume tailoring for job {self.job.id} in background thread")
            self.signal_progress.emit("Tailoring resume...")
            
            # Call OpenAI API
            result = chat_manager.tailor_resume(self.job, self.cv_text)
            
            # Extract match score
            score = self._extract_match_score(result)
            
            # Save match score to database
            if score is not None:
                db_manager.save_match_score(self.job.id, score)
            
            # Save PDF in background
            self.signal_progress.emit("Generating PDF...")
            file_manager.save_tailored_resume_as_pdf(result, self.job)
            
            logging.info(f"Resume tailored successfully for job {self.job.id}")
            self.signal_finished.emit(result, score if score is not None else 0.0)
        except Exception as e:
            logging.error(f"Error tailoring resume: {e}")
            self.signal_error.emit(str(e))

    def _extract_match_score(self, html_text: str) -> float | None:
        """Extract the matching score from HTML comment."""
        match = re.search(r"<!--\s*MATCHING_SCORE:\s*(\d+(\.\d+)?)\s*-->", html_text)
        if match:
            return float(match.group(1))
        return None
