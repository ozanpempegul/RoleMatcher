from PySide6.QtWidgets import QPushButton
import webbrowser



class OpenLinkButton(QPushButton):
    def __init__(self, parent=None, url: str = ""):
        super().__init__("Open Link", parent)
        self.setObjectName("open_link_button")
        self._init_style()
        self.url = url


    def _init_style(self):
        self.setStyleSheet("""
            QPushButton#open_link_button {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
        """)

    def mousePressEvent(self, event):
        if self.url:
            webbrowser.open(self.url)
        super().mousePressEvent(event)

    