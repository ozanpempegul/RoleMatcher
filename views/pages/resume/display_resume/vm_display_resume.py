import json
from pathlib import Path
from PySide6 import QtWidgets
from .ui_display_resume import *
from PySide6.QtCore import Signal
from common.imports.log import*
import time


class DisplayResumeFrame(QFrame):

    signal_cv_removed = Signal()

    def __init__(self, file_path=None):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.file_path = file_path

        self._init_ui()
        self._init_event_handlers()
    

    def _init_ui(self):
        if self.file_path:
            self.load_json_to_form(self.file_path)


    def _init_event_handlers(self):
        self.ui.toolButton_remove_cv.clicked.connect(self.remove_current_cv)


    def add_line(self, layout, key, value):
        h = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel(f"{key}:")
        edit = QtWidgets.QLineEdit(str(value) if value is not None else "")
        edit.setReadOnly(True)
        h.addWidget(label)
        h.addWidget(edit)
        layout.addLayout(h)


    def set_file_path(self, path):
        self.file_path = path
        self.load_json_to_form(path)


    def populate_static_fields(self, layout, data):
        for key, value in data.items():
            if isinstance(value, list):
                list_widget = QtWidgets.QListWidget()
                list_widget.addItems([str(i) for i in value])
                layout.addWidget(QtWidgets.QLabel(f"{key}:"))
                layout.addWidget(list_widget)
            elif isinstance(value, dict):
                group = QtWidgets.QGroupBox(key)
                inner = QtWidgets.QVBoxLayout()
                self.populate_static_fields(inner, value)
                group.setLayout(inner)
                layout.addWidget(group)
            else:
                self.add_line(layout, key, value)


    def populate_experience(self, layout, exp_list):
        for exp in exp_list:
            group = QtWidgets.QGroupBox(exp.get("role", "Experience"))
            inner = QtWidgets.QVBoxLayout()
            for key, val in exp.items():
                if key == "bullets":
                    list_widget = QtWidgets.QListWidget()
                    for bullet in val:
                        list_widget.addItem(bullet)
                    inner.addWidget(QtWidgets.QLabel("Bullets:"))
                    inner.addWidget(list_widget)
                else:
                    self.add_line(inner, key, val)
            group.setLayout(inner)
            layout.addWidget(group)


    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clear_layout(child.layout())


    def load_json_to_form(self, path):
        try:
            self.clear_layout(self.ui.metaLayout)
            self.clear_layout(self.ui.profileLayout)
            self.clear_layout(self.ui.skillsLayout)
            self.clear_layout(self.ui.educationLayout)
            self.clear_layout(self.ui.experienceLayout)
            self.clear_layout(self.ui.projectsLayout)
        except Exception as e:
            logging.error(f"Error clearing layout: {e}")

        time.sleep(0.1)  # small delay to ensure UI updates
        print("path:", path)

        if not path:
            return

        try:
            data = json.loads(Path(path).read_text(encoding="utf-8-sig"))
        except Exception as e:
            # Surface a clear error for debugging / UI logging
            logging.error(f"Unable to load resume summary JSON: {e}")

        # Fill sections
        if "meta" in data:
            self.populate_static_fields(self.ui.metaLayout, data["meta"])
        if "profile" in data:
            self.populate_static_fields(self.ui.profileLayout, data["profile"])
        if "skills" in data:
            self.populate_static_fields(self.ui.skillsLayout, data["skills"])
        if "education" in data:
            self.populate_static_fields(self.ui.educationLayout, {"education": data["education"]})
        if "experience" in data:
            self.populate_experience(self.ui.experienceLayout, data["experience"])
        if "projects" in data:
            self.populate_static_fields(self.ui.projectsLayout, {"projects": data["projects"]})


    def remove_current_cv(self):
        if not self.file_path:
            QtWidgets.QMessageBox.information(self, "Remove CV", "No CV selected.")
            return

        path = Path(self.file_path)
        if not path.exists():
            QtWidgets.QMessageBox.information(self, "Remove CV", f"File not found:\n{self.file_path}")
            self.file_path = None
            return

        resp = QtWidgets.QMessageBox.question(
            self,
            "Remove CV",
            f"Do you want to permanently delete this file?\n{self.file_path}",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )
        if resp != QtWidgets.QMessageBox.Yes:
            return

        try:
            path.unlink()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to remove file:\n{e}")
            logging.error(f"Failed to remove file: {e}")
            return

        self.file_path = None
        # clear displayed fields
        self.load_json_to_form(self.file_path)

        self.signal_cv_removed.emit()

        QtWidgets.QMessageBox.information(self, "Remove CV", "File removed.")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = DisplayResumeFrame()

    window.show()
    app.exec()





