from PySide6.QtCore import QThread, Signal
from managers.chat_manager import chat_manager
from managers.file_manager import file_manager
from models.job import Job
from common.imports.log import *


class CoverLetterWorker(QThread):
    """Worker thread for generating cover letters."""
    signal_finished = Signal(str)  # html_result
    signal_error = Signal(str)
    signal_progress = Signal(str)

    def __init__(self, job: Job, cv_text: str):
        super().__init__()
        self.job = job
        self.cv_text = cv_text

    def run(self):
        try:
            logging.info(f"Starting cover letter generation for job {self.job.id} in background thread")
            self.signal_progress.emit("Generating cover letter...")
            
            # Call OpenAI API
            result = chat_manager.generate_cover_letter(self.job, self.cv_text)
            
            # Save PDF in background
            self.signal_progress.emit("Generating PDF...")
            file_manager.save_cover_letter_as_pdf(result, self.job)
            
            logging.info(f"Cover letter generated successfully for job {self.job.id}")
            self.signal_finished.emit(result)
        except Exception as e:
            logging.error(f"Error generating cover letter: {e}")
            self.signal_error.emit(str(e))
