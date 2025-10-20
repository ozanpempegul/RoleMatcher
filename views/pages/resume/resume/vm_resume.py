from .ui_resume import *
from ..upload_resume.vm_upload_resume import UploadResumeFrame
from ..display_resume.vm_display_resume import DisplayResumeFrame
from pathlib import Path

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
        file_path = self.get_latest_summary_json()
        if file_path:
            self.display_resume_frame.set_file_path(file_path)
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
        self.upload_resume_frame.signal_cv_uploaded.connect(self.on_resume_uploaded)
        self.display_resume_frame.signal_cv_removed.connect(self.on_cv_removed)


    def on_resume_uploaded(self, file_path):
        print("Resume uploaded:", file_path)
        self.display_resume_frame.set_file_path(file_path)
        self.ui.stackedWidget.setCurrentIndex(1)


    def on_cv_removed(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def get_latest_summary_json(self):
        """
        Look for a 'summaries' directory and return the latest .json file by filename.
        Search order:
         - current working directory and its parents
         - this module's directory and its parents
        Returns None if not found or no json files exist.
        """
        # Build search roots: cwd first (since you run the project there), then its parents,
        # then the module directory and its parents as a fallback.
        cwd = Path.cwd()
        module_dir = Path(__file__).resolve().parent

        search_roots = []
        for p in [cwd, *cwd.parents, module_dir, *module_dir.parents]:
            if p not in search_roots:
                search_roots.append(p)

        for root in search_roots:
            summaries_dir = root / "summaries"
            if summaries_dir.is_dir():
                json_files = [f for f in summaries_dir.iterdir() if f.is_file() and f.suffix.lower() == ".json"]
                if not json_files:
                    return None
                json_files.sort(key=lambda p: p.name)
                return str(json_files[-1])

        return None
