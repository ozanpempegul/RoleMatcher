from .ui_main import*
from ..config.vm_config import ConfigFrame
from managers.db import db_manager
from managers.job_fetcher import job_fetcher



class JobFetchMainFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_ui()
        self._init_event_handlers()

    def _init_ui(self):
        layout = QVBoxLayout(self.ui.frame_config)
        layout.setContentsMargins(0, 0, 0, 0)
        self.config_frame = ConfigFrame()
        layout.addWidget(self.config_frame)

    def _init_event_handlers(self):
        self.ui.toolButton_fetch.clicked.connect(self._on_fetch_clicked)

    def _on_fetch_clicked(self):
        config = self.config_frame.get_config()

        # fetch jobs
        job_fetcher.apply_config(config)
        jobs = job_fetcher.fetch_jobs()

        # # save jobs
        db_manager.save_jobs(jobs)  # Use the manager's method


