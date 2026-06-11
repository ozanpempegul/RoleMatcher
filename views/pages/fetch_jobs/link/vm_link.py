from .ui_link import*

class LinkFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

    def get_link(self) -> str:
        return self.ui.lineEdit.text().strip()