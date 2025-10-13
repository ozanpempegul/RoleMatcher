from .ui_job_list_table import *
from ..job_list_row.vm_job_list_row import JobListRow
from ..job_list_header.vm_job_list_header import JobListHeader
from models.job import Job


class JobListTable(QFrame):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self._init_ui()
        job = Job()
        job.id = "1"
        job.site = "Indeed"
        job.title = "Software Engineer"
        job.company_name = "Tech Corp"
        job.location = "New York, NY"
        job.job_type = "Full-time"
        job.is_remote = True
        job.job_level = "Mid"
        job.description = "Develop and maintain software applications."
        self.add_row(job)


    def _init_ui(self):
        header_layout = QVBoxLayout(self.ui.frame_job_list_header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header = JobListHeader()
        header_layout.addWidget(header)

    def add_row(self, job: Job):
        table_layout = self.ui.frame_job_list_table.layout()
        row = JobListRow()
        row.apply_values(job)
        table_layout.addWidget(row)
    
