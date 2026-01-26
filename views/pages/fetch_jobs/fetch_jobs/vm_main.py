from .ui_main import*
from ..config.vm_config import ConfigFrame
from managers.db import db_manager
from workers.job_fetch_worker import JobFetchWorker
from workers.save_jobs_worker import SaveJobsWorker
from PySide6.QtWidgets import QMessageBox
from common.imports.log import *


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

    def _init_ui(self):
        layout = QVBoxLayout(self.ui.frame_config)
        layout.setContentsMargins(0, 0, 0, 0)
        self.config_frame = ConfigFrame()
        layout.addWidget(self.config_frame)

    def _init_event_handlers(self):
        self.ui.toolButton_fetch.clicked.connect(self._on_fetch_clicked)

    def _on_fetch_clicked(self):
        config = self.config_frame.get_config()
        
        # Disable button during operation
        self.ui.toolButton_fetch.setEnabled(False)
        self.ui.toolButton_fetch.setText("Fetching...")
        
        # Create and start job fetch worker
        self.job_fetch_worker = JobFetchWorker(config)
        self.job_fetch_worker.signal_finished.connect(self._on_jobs_fetched)
        self.job_fetch_worker.signal_error.connect(self._on_fetch_error)
        self.job_fetch_worker.signal_progress.connect(self._on_progress)
        self.job_fetch_worker.start()

    def _on_jobs_fetched(self, jobs_df):
        """Called when jobs are successfully fetched."""
        logging.info(f"Jobs fetched: {len(jobs_df)} jobs")
        
        # Update UI
        self.ui.toolButton_fetch.setText("Saving...")
        
        # Create and start save jobs worker
        self.save_jobs_worker = SaveJobsWorker(jobs_df)
        self.save_jobs_worker.signal_finished.connect(self._on_jobs_saved)
        self.save_jobs_worker.signal_error.connect(self._on_save_error)
        self.save_jobs_worker.signal_progress.connect(self._on_progress)
        self.save_jobs_worker.start()

    def _on_jobs_saved(self):
        """Called when jobs are successfully saved."""
        logging.info("Jobs saved successfully")
        self.ui.toolButton_fetch.setEnabled(True)
        self.ui.toolButton_fetch.setText("Fetch Jobs")
        
        # Clean up workers
        if self.job_fetch_worker:
            self.job_fetch_worker.quit()
            self.job_fetch_worker.wait()
            self.job_fetch_worker = None
        
        if self.save_jobs_worker:
            self.save_jobs_worker.quit()
            self.save_jobs_worker.wait()
            self.save_jobs_worker = None
        
        QMessageBox.information(self, "Success", "Jobs fetched and saved successfully!")

    def _on_fetch_error(self, error_msg: str):
        """Called when job fetching fails."""
        logging.error(f"Job fetch error: {error_msg}")
        self.ui.toolButton_fetch.setEnabled(True)
        self.ui.toolButton_fetch.setText("Fetch Jobs")
        
        if self.job_fetch_worker:
            self.job_fetch_worker.quit()
            self.job_fetch_worker.wait()
            self.job_fetch_worker = None
        
        QMessageBox.critical(self, "Error", f"Failed to fetch jobs:\n{error_msg}")

    def _on_save_error(self, error_msg: str):
        """Called when saving jobs fails."""
        logging.error(f"Job save error: {error_msg}")
        self.ui.toolButton_fetch.setEnabled(True)
        self.ui.toolButton_fetch.setText("Fetch Jobs")
        
        if self.save_jobs_worker:
            self.save_jobs_worker.quit()
            self.save_jobs_worker.wait()
            self.save_jobs_worker = None
        
        QMessageBox.critical(self, "Error", f"Failed to save jobs:\n{error_msg}")

    def _on_progress(self, message: str):
        """Called for progress updates."""
        logging.info(f"Progress: {message}")
        # Optionally update UI with progress message


