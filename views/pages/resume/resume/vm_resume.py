from .ui_resume import *
from ..upload_resume.vm_upload_resume import UploadResumeFrame
from ..display_resume.vm_display_resume import DisplayResumeFrame
from managers.resume_summarizer import resume_summarizer


class ResumePage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_ui()
        self._init_event_handlers()


    def _init_ui(self):
        self._init_upload_resume_frame()
        self._init_display_resume_frame()
        data = resume_summarizer.get_data_from_summary_json()
        if data:
            self.display_resume_frame.load_json_to_form(data)
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)


    def _init_upload_resume_frame(self):
        layout = QVBoxLayout(self.ui.page_upload)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.upload_resume_frame = UploadResumeFrame()
        layout.addWidget(self.upload_resume_frame)


    def _init_display_resume_frame(self):
        layout = QVBoxLayout(self.ui.page_display)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.display_resume_frame = DisplayResumeFrame()
        layout.addWidget(self.display_resume_frame)


    def _init_event_handlers(self):
        resume_summarizer.signal_resume_summarized.connect(self.on_resume_uploaded)
        self.display_resume_frame.signal_cv_removed.connect(self.on_cv_removed)


    def on_resume_uploaded(self, data):
        self.display_resume_frame.load_json_to_form(data)
        self.ui.stackedWidget.setCurrentIndex(1)


    def on_cv_removed(self):
        self.ui.stackedWidget.setCurrentIndex(0)

