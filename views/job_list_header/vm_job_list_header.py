from .ui_job_list_header import *


class JobListHeader(QFrame):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)