from .ui_upload_resume import *
from PySide6.QtWidgets import QFileDialog
from managers.resume_summarizer import resume_summarizer
from PySide6.QtCore import Signal


class UploadResumeFrame(QFrame):

    signal_cv_uploaded = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_event_handlers()

    def _init_event_handlers(self):
        resume_summarizer.signal_resume_summarized.connect(self.on_resume_summarized)
        self.ui.frame_drop_area.dragEnterEvent = self.on_drag_enter
        self.ui.frame_drop_area.dropEvent = self.on_drop
        self.ui.frame_drop_area.mousePressEvent = self.on_mouse_press

    def on_drag_enter(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def on_drop(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            print(f"Dropped file: {file_path}")
            # Here you can add code to handle the dropped file (e.g., upload it)

    def on_mouse_press(self, event):
        print("Drop area clicked")
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CV File",
            "",
            "Word Files (*.docx);;All Files (*)",
            options=options
        )
        if self.file_path:
            print(f"Selected CV file: {self.file_path}")
            resume_summarizer.start_pipeline(self.file_path)

    def on_resume_summarized(self, summary_path):
        print("Resume processing completed: ", summary_path)
        self.signal_cv_uploaded.emit(summary_path)
