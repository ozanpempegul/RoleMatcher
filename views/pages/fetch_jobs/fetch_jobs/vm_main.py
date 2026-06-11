from .ui_main import*
from ..config.vm_config import ConfigFrame
from ..link.vm_link import LinkFrame
from managers.db import db_manager
from workers.job_fetch_worker import JobFetchWorker
from workers.job_link_fetch_worker import JobLinkFetchWorker
from workers.save_jobs_worker import SaveJobsWorker
from PySide6.QtWidgets import QMessageBox
from common.imports.log import *
from enum import Enum



class FetchJobsPage(Enum):
    CONFIG = "config"
    LINK = "link"

class JobFetchMainFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_variables()
        self._init_ui()
        self._init_event_handlers()

    def _init_variables(self):
        self.job_fetch_worker = None
        self.save_jobs_worker = None
        self._is_busy = False

    def _init_ui(self):
        self.config_frame = ConfigFrame()
        self.ui.stackedWidget_pages.addWidget(self.config_frame)
        self.link_frame = LinkFrame()
        self.ui.stackedWidget_pages.addWidget(self.link_frame)

        self._on_by_search_clicked()

    def _init_event_handlers(self):
        self.ui.toolButton_fetch.clicked.connect(self._on_fetch_clicked)
        self.ui.pushButton_by_search.clicked.connect(self._on_by_search_clicked)
        self.ui.pushButton_by_link.clicked.connect(self._on_by_link_clicked)

    def _on_fetch_clicked(self):
        if self._is_busy:
            return

        if self._current_page == FetchJobsPage.CONFIG:
            config = self.config_frame.get_config()
            worker = JobFetchWorker(config)
        elif self._current_page == FetchJobsPage.LINK:
            link = self.link_frame.get_link()
            if not link:
                QMessageBox.warning(self, "Missing URL", "Please enter a job URL.")
                return
            worker = JobLinkFetchWorker(link)
        else:
            return

        self._set_busy(True, "Fetching...")
        self._start_fetch_worker(worker)

    def _start_fetch_worker(self, worker):
        self._cleanup_fetch_worker()
        self.job_fetch_worker = worker
        worker.signal_finished.connect(self._on_jobs_fetched)
        worker.signal_error.connect(self._on_fetch_error)
        worker.signal_progress.connect(self._on_progress)
        worker.start()

    def _start_save_worker(self, jobs_df):
        self._cleanup_save_worker()
        self.save_jobs_worker = SaveJobsWorker(jobs_df)
        self.save_jobs_worker.signal_finished.connect(self._on_jobs_saved)
        self.save_jobs_worker.signal_error.connect(self._on_save_error)
        self.save_jobs_worker.signal_progress.connect(self._on_progress)
        self.save_jobs_worker.start()

    def _cleanup_fetch_worker(self):
        if not self.job_fetch_worker:
            return
        self.job_fetch_worker.signal_finished.disconnect(self._on_jobs_fetched)
        self.job_fetch_worker.signal_error.disconnect(self._on_fetch_error)
        self.job_fetch_worker.signal_progress.disconnect(self._on_progress)
        if self.job_fetch_worker.isRunning():
            self.job_fetch_worker.quit()
            self.job_fetch_worker.wait()
        self.job_fetch_worker = None

    def _cleanup_save_worker(self):
        if not self.save_jobs_worker:
            return
        self.save_jobs_worker.signal_finished.disconnect(self._on_jobs_saved)
        self.save_jobs_worker.signal_error.disconnect(self._on_save_error)
        self.save_jobs_worker.signal_progress.disconnect(self._on_progress)
        if self.save_jobs_worker.isRunning():
            self.save_jobs_worker.quit()
            self.save_jobs_worker.wait()
        self.save_jobs_worker = None

    def _set_busy(self, busy: bool, button_text: str = "Fetch Jobs"):
        self._is_busy = busy
        self.ui.toolButton_fetch.setEnabled(not busy)
        self.ui.toolButton_fetch.setText(button_text)

    def _on_jobs_fetched(self, jobs_df):
        """Called when jobs are successfully fetched."""
        logging.info(f"Jobs fetched: {len(jobs_df)} jobs")
        self._cleanup_fetch_worker()
        self._set_busy(True, "Saving...")
        self._start_save_worker(jobs_df)

    def _on_jobs_saved(self, saved: int, skipped: int):
        """Called when jobs are successfully saved."""
        logging.info(f"Jobs saved: {saved}, skipped: {skipped}")
        self._cleanup_save_worker()
        self._set_busy(False)
        if saved == 0 and skipped > 0:
            QMessageBox.information(
                self,
                "Already Saved",
                "The job is already in your list. Open the job list page to view it.",
            )
        elif skipped > 0:
            QMessageBox.information(
                self,
                "Success",
                f"Saved {saved} job(s). {skipped} duplicate(s) were already in your list.",
            )
        else:
            QMessageBox.information(
                self,
                "Success",
                f"Saved {saved} job(s) successfully!",
            )

    def _on_fetch_error(self, error_msg: str):
        """Called when job fetching fails."""
        logging.error(f"Job fetch error: {error_msg}")
        self._cleanup_fetch_worker()
        self._set_busy(False)
        QMessageBox.critical(self, "Error", f"Failed to fetch jobs:\n{error_msg}")

    def _on_save_error(self, error_msg: str):
        """Called when saving jobs fails."""
        logging.error(f"Job save error: {error_msg}")
        self._cleanup_save_worker()
        self._set_busy(False)
        QMessageBox.critical(self, "Error", f"Failed to save jobs:\n{error_msg}")

    def _on_progress(self, message: str):
        """Called for progress updates."""
        logging.info(f"Progress: {message}")
        # Optionally update UI with progress message

    def _on_by_search_clicked(self):
        self._current_page = FetchJobsPage.CONFIG
        self.ui.stackedWidget_pages.setCurrentWidget(self.config_frame)

    def _on_by_link_clicked(self):
        self._current_page = FetchJobsPage.LINK
        self.ui.stackedWidget_pages.setCurrentWidget(self.link_frame)


