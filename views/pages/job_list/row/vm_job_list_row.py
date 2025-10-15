from .ui_job_list_row import *
from models.job import Job, Sites
from managers.db import db_manager
import webbrowser

class JobListRow(QFrame):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_event_handlers()

    def _init_event_handlers(self):
        self.ui.toolButton_open_link.clicked.connect(self._on_open_link_clicked)
        self.ui.toolButton_remove.clicked.connect(self._on_remove_clicked)

    def apply_values(self, job: Job, idx: int):
        self.id = job.id # Store job ID for db reference
        self.ui.label_id.setText(str(idx))
        for site in Sites:
            if site.value == job.site:
                self.ui.label_site.setText(site.name)
                break
        self.ui.label_title.setText(job.title)
        self.ui.label_company_name.setText(job.company_name)
        self.ui.label_location.setText(job.location)
        self.ui.label_job_type.setText(job.job_type)
        self.ui.checkBox_is_remote.setChecked(job.is_remote)
        self.ui.label_job_level.setText(job.job_level)
        self.link = job.url
        # self.ui.label_description.setText(job.description)

    def _on_open_link_clicked(self):
        print("Open link clicked:", self.link)
        if self.link:
            webbrowser.open(self.link)

    def _on_remove_clicked(self):
        db_manager.remove_job(self.id)
