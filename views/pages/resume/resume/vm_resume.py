from .ui_resume import *
from ..upload_resume.vm_upload_resume import UploadResumeFrame
from ..display_resume.vm_display_resume import DisplayResumeFrame
from managers.file_manager import file_manager


class ResumePage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_ui()
        self._init_event_handlers()
        self.on_resume_uploaded(file_manager.get_last_summary_json())


    def _init_ui(self):
        self._init_upload_resume_frame()
        self._init_display_resume_frame()


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
        self.display_resume_frame.signal_cv_removed.connect(self.on_cv_removed)
        file_manager.signal_last_summary_json_loaded.connect(self.on_resume_uploaded)


    def on_resume_uploaded(self, data):
        if data:
            self.display_resume_frame.load_json_to_form(data)
            self.display_resume_frame.file_path = file_manager._find_last_summary_path()
            self.ui.stackedWidget.setCurrentIndex(1)


    def on_cv_removed(self):
        self.ui.stackedWidget.setCurrentIndex(0)

