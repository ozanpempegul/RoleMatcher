from PySide6.QtWidgets import QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from managers.db import db_manager



class RemoveButton(QToolButton):
    def __init__(self, parent=None, idx: int = -1):
        super().__init__(parent)
        self.setObjectName("remove_button")
        self._init_style()
        self.idx = idx


    def _init_style(self):
        self.setIcon(QIcon(":/job_list/assets/icons/remove.png"))
        self.setIconSize(QSize(32, 32))
        self.setStyleSheet("border: none;")


    def mousePressEvent(self, event):
        db_manager.remove_job(self.idx)
        super().mousePressEvent(event)

    