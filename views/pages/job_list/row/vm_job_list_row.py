import re
from .ui_job_list_row import *
from models.job import Job, Sites
from managers.db import db_manager
import webbrowser
from managers.file_manager import file_manager
from managers.chat_manager import chat_manager



class JobListRow(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_event_handlers()


    def _init_event_handlers(self):
        self.ui.toolButton_open_link.clicked.connect(self._on_open_link_clicked)
        self.ui.toolButton_remove.clicked.connect(self._on_remove_clicked)
        self.ui.toolButton_generate_tailored_resume.clicked.connect(self._on_generate_tailored_resume_clicked)
        self.ui.toolButton_generate_cover_letter.clicked.connect(self._on_generate_cover_letter_clicked)


    def apply_values(self, job: Job, idx: int, match_score: float | None):
        self.job = job
        self.id = job.id # Store job ID for db reference
        self.ui.label_match_score.setText(f"{match_score:.2f}%" if match_score is not None else "N/A")
        self.ui.label_id.setText(str(idx))
        self.ui.label_title.setText(job.title)
        self.ui.label_company_name.setText(job.company_name)
        self.ui.label_location.setText(job.location)
        self.ui.label_job_type.setText(job.job_type)
        self.ui.checkBox_is_remote.setChecked(job.is_remote)
        self.link = job.url
        self.job_description = job.description


    def _on_open_link_clicked(self):
        if self.link:
            webbrowser.open(self.link)


    def _on_remove_clicked(self):
        db_manager.remove_job(self.id)


    def _on_generate_tailored_resume_clicked(self):
        cv_text = file_manager.get_last_summary_json()
        print("cv text: ", cv_text)
        result = chat_manager.tailor_resume(self.job, cv_text)
        score = self.extract_match_score(result)
        db_manager.save_match_score(self.id, score)
        file_manager.save_tailored_resume_as_pdf(result, self.id)
        # Call the resume tailoring function here with the job details


    def _on_generate_cover_letter_clicked(self):
        cv_text = file_manager.get_last_summary_json()
        result = chat_manager.generate_cover_letter(self.job, cv_text)
        file_manager.save_cover_letter_as_pdf(result, self.id)


    def extract_match_score(self, html_text: str) -> float | None:
        """
        Extract the matching score from HTML comment.
        Example comment: <!-- MATCHING_SCORE: 87 -->
        Returns the score as float, or None if not found.
        """
        match = re.search(r"<!--\s*MATCHING_SCORE:\s*(\d+(\.\d+)?)\s*-->", html_text)
        if match:
            return float(match.group(1))
        return None