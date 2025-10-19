from .ui_main_window import*
from views.pages.job_list.job_list.vm_job_list_table import JobListTable
from views.pages.fetch_jobs.fetch_jobs.vm_main import JobFetchMainFrame
from views.pages.upload_resume.upload_resume.vm_upload_resume import UploadResumeFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._init_ui()
        self._init_event_handlers()

        self._init_defaults()

    def _init_ui(self):
        self._init_fetch_jobs_page()
        self._init_job_list_table()
        self._init_upload_resume_page()

    def _init_fetch_jobs_page(self):
        layout = QVBoxLayout(self.ui.page_fetch_jobs)
        layout.setContentsMargins(0, 0, 0, 0)
        fetch_jobs_frame = JobFetchMainFrame()
        layout.addWidget(fetch_jobs_frame)

    def _init_job_list_table(self):
        layout = QVBoxLayout(self.ui.page_retrieved_jobs)
        layout.setContentsMargins(0, 0, 0, 0)
        job_list_table = JobListTable()
        layout.addWidget(job_list_table)

    def _init_upload_resume_page(self):
        layout = QVBoxLayout(self.ui.page_upload_resume)
        layout.setContentsMargins(0, 0, 0, 0)
        upload_resume_frame = UploadResumeFrame()
        layout.addWidget(upload_resume_frame)

    def _init_event_handlers(self):
        self.ui.toolButton_show_fetch_jobs_page.clicked.connect(
            self.on_fetch_jobs_clicked
        )
        self.ui.toolButton_show_retrieved_jobs_page.clicked.connect(
            self.on_retrieved_jobs_clicked
        )
        self.ui.toolButton_show_upload_resume_page.clicked.connect(
            self.on_upload_resume_clicked
        )

    def _init_defaults(self):
        self.on_fetch_jobs_clicked()

    def on_fetch_jobs_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_retrieved_jobs_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_upload_resume_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
