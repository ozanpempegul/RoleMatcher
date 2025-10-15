from .ui_job_list_table import *
from ..row.vm_job_list_row import JobListRow
from ..header.vm_job_list_header import JobListHeader
from models.job import Job
from managers.db import db_manager


class JobListTable(QFrame):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self._init_variables()
        self._init_ui()
        self._init_event_handlers()

    def _init_variables(self):
        self.header = JobListHeader()

    def _init_ui(self):
        self._init_header_frame()

    def _init_header_frame(self):
        layout = self.ui.frame_job_list_table.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.frame_job_list_header)
            layout.setContentsMargins(0, 0, 0, 0)
        self.header = JobListHeader()
        self.header.ui.toolButton_refresh.clicked.connect(self.retrieve_jobs)
        layout.addWidget(self.header)

    def _init_event_handlers(self):
        db_manager.signal_data_saved.connect(self.retrieve_jobs)
        
    def add_row(self, job: Job, idx: int):
        table_layout = self.ui.frame_job_list_table.layout()
        row = JobListRow()
        row.apply_values(job, idx)
        table_layout.addWidget(row)

    def clear_rows(self):
        layout = self.ui.frame_job_list_table.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
    
    def retrieve_jobs(self):
        # clear existing rows
        self.clear_rows()
        self._init_header_frame()
        # get jobs
        retrieved_jobs = db_manager.get_jobs()
        print(f"Retrieved {len(retrieved_jobs)} jobs from the database")
        for idx, job in enumerate(retrieved_jobs):
            self.add_row(job, idx)
