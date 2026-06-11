import pandas as pd
from PySide6.QtCore import QThread, Signal

from common.imports.log import *
from managers.job_link_fetcher import job_link_fetcher


class JobLinkFetchWorker(QThread):
    signal_finished = Signal(pd.DataFrame)
    signal_error = Signal(str)
    signal_progress = Signal(str)

    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def run(self):
        try:
            logging.info("Starting job link fetch in background thread")
            self.signal_progress.emit("Fetching job from link...")
            jobs = job_link_fetcher.fetch_job_by_url(self.url)
            logging.info("Fetched job from link")
            self.signal_finished.emit(jobs)
        except Exception as e:
            logging.error(f"Error fetching job from link: {e}")
            self.signal_error.emit(str(e))
