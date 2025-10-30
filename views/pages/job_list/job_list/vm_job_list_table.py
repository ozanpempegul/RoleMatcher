from .ui_job_list_table import *
from ..buttons.remove import RemoveButton
from ..buttons.open_link import OpenLinkButton
from ..buttons.tailor_resume import TailorResumeButton
from ..buttons.generate_cover_letter import GenerateCoverLetterButton
from models.job import Job
from managers.db import db_manager
from common.imports.log import*


class JobListTable(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self._init_variables()
        self._init_ui()
        self._init_event_handlers()


    def _init_variables(self):
        pass


    def _init_ui(self):
        pass


    def _init_event_handlers(self):
        db_manager.signal_data_saved.connect(self.retrieve_jobs)
        self.ui.toolButton_refresh.clicked.connect(self.retrieve_jobs)
        

    def add_row(self, job: Job, idx: int, match_score: float | None):
        try:
            # ensure the table has a row at this index before setting items
            # insertRow will create a new row at idx (shifting others if needed)
            # alternatively you could use setRowCount(len) before populating all rows
            self.ui.tableWidget.insertRow(idx)
            self.ui.tableWidget.setItem(idx, 0, QTableWidgetItem(job.title))
            self.ui.tableWidget.setItem(idx, 1, QTableWidgetItem(job.company_name))
            self.ui.tableWidget.setItem(idx, 2, QTableWidgetItem(job.location))
            self.ui.tableWidget.setItem(idx, 3, QTableWidgetItem(job.job_type))
            self.ui.tableWidget.setItem(idx, 4, QTableWidgetItem("Yes" if job.is_remote else "No"))
            score_text = f"{match_score:.2f}%" if match_score is not None else "N/A"
            self.ui.tableWidget.setItem(idx, 5, QTableWidgetItem(score_text))
            remove_btn = RemoveButton(idx=job.id)
            self.ui.tableWidget.setCellWidget(idx, 6, remove_btn)
            open_link_btn = OpenLinkButton(url=job.url)
            self.ui.tableWidget.setCellWidget(idx, 7, open_link_btn)
            tailor_resume_btn = TailorResumeButton(job=job)
            self.ui.tableWidget.setCellWidget(idx, 8, tailor_resume_btn)
            generate_cover_letter_btn = GenerateCoverLetterButton(job=job)
            self.ui.tableWidget.setCellWidget(idx, 9, generate_cover_letter_btn)
            self.ui.tableWidget.resizeColumnsToContents()
        except Exception as e:
            print(f"Error adding row for job ID {getattr(job, 'id', 'unknown')}: {e}")
            logging.error(f"Error adding row for job ID {getattr(job, 'id', 'unknown')}: {e}")


    def clear_rows(self):
        # clear the QTableWidget rows first
        try:
            self.ui.tableWidget.setRowCount(0)
        except Exception:
            # fallback to clearing any layout-based rows (if used elsewhere)
            pass


    def retrieve_jobs(self):
        # clear existing rows
        self.clear_rows()
        # get jobs
        retrieved_jobs = db_manager.get_jobs()
        for idx, job in enumerate(retrieved_jobs):
            match_score = db_manager.get_match_score(job.id)
            self.add_row(job, idx, match_score)
