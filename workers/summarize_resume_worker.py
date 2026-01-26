from PySide6.QtCore import QThread, Signal
from managers.chat_manager import chat_manager
from managers.file_manager import file_manager
from common.imports.log import *


class SummarizeResumeWorker(QThread):
    """Worker thread for summarizing resume from DOCX file."""
    signal_finished = Signal(str)  # summary_json_path
    signal_error = Signal(str)
    signal_progress = Signal(str)

    def __init__(self, resume_path: str):
        super().__init__()
        self.resume_path = resume_path

    def run(self):
        try:
            logging.info(f"Starting resume summarization in background thread")
            self.signal_progress.emit("Extracting text from resume...")
            
            # Call OpenAI API to summarize (this internally extracts text and saves summary)
            self.signal_progress.emit("Analyzing resume with AI...")
            summary_json = chat_manager.summarize_resume(self.resume_path)
            
            logging.info("Resume summarized successfully")
            self.signal_finished.emit(summary_json)
        except Exception as e:
            logging.error(f"Error summarizing resume: {e}")
            self.signal_error.emit(str(e))
