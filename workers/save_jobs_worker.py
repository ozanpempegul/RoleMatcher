from PySide6.QtCore import QThread, Signal
from managers.db import db_manager
import pandas as pd
from common.imports.log import *


class SaveJobsWorker(QThread):
    """Worker thread for saving jobs to the database."""
    signal_finished = Signal(int, int)  # saved, skipped
    signal_error = Signal(str)
    signal_progress = Signal(str)

    def __init__(self, jobs_df: pd.DataFrame):
        super().__init__()
        self.jobs_df = jobs_df

    def run(self):
        try:
            logging.info("Starting job save in background thread")
            self.signal_progress.emit("Saving jobs to database...")
            saved, skipped = db_manager.save_jobs(self.jobs_df)
            logging.info(f"Jobs saved: {saved}, skipped: {skipped}")
            self.signal_finished.emit(saved, skipped)
        except Exception as e:
            logging.error(f"Error saving jobs: {e}")
            self.signal_error.emit(str(e))
