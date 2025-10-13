from .ui_job_list_row import *
from models.job import Job


class JobListRow(QFrame):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

    def apply_values(self, job: Job):
        self.ui.label_id.setText(job.id)
        self.ui.label_site.setText(job.site)
        self.ui.label_title.setText(job.title)
        self.ui.label_company_name.setText(job.company_name)
        self.ui.label_location.setText(job.location)
        self.ui.label_job_type.setText(job.job_type)
        self.ui.checkBox_is_remote.setChecked(job.is_remote)
        self.ui.label_job_level.setText(job.job_level)
        self.ui.label_description.setText(job.description)