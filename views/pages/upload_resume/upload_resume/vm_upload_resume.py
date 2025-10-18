from .ui_upload_resume import *
from PySide6.QtWidgets import QFileDialog
from managers.resume_summarizer import resume_summarizer


class UploadResumeFrame(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self._init_event_handlers()

    def _init_event_handlers(self):
        self.ui.frame_drop_area.dragEnterEvent = self.on_drag_enter
        self.ui.frame_drop_area.dropEvent = self.on_drop
        self.ui.frame_drop_area.mousePressEvent = self.on_mouse_press
        self.ui.toolButton_upload_cv.clicked.connect(self.on_upload_cv_clicked)

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
            # Add code here to handle the uploaded file (e.g., save or process it)

    def on_upload_cv_clicked(self):
        if self.file_path:
            print("Upload CV button clicked")
            resume_summarizer.start_pipeline(self.file_path)