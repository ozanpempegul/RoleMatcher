from PySide6.QtCore import QThread, Signal
from managers.job_fetcher import job_fetcher
from models.job_fetcher_config import JobScraperConfig
import pandas as pd
from common.imports.log import *


class JobFetchWorker(QThread):
    """Worker thread for fetching jobs from job sites."""
    signal_finished = Signal(pd.DataFrame)
    signal_error = Signal(str)
    signal_progress = Signal(str)  # Optional: for progress updates

    def __init__(self, config: JobScraperConfig):
        super().__init__()
        self.config = config

    def run(self):
        try:
            logging.info("Starting job fetch in background thread")
            self.signal_progress.emit("Fetching jobs...")
            job_fetcher.apply_config(self.config)
            jobs = job_fetcher.fetch_jobs()
            logging.info(f"Fetched {len(jobs)} jobs")
            self.signal_finished.emit(jobs)
        except Exception as e:
            logging.error(f"Error fetching jobs: {e}")
            self.signal_error.emit(str(e))
