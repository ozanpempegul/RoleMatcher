from .ui_config import*
from models.job_fetcher_config import JobScraperConfig



class ConfigFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self._set_defaults()

    def _set_defaults(self):
        self.ui.checkBox_linkedin.setChecked(True)
        self.ui.checkBox_indeed.setChecked(False)
        self.ui.checkBox_google.setChecked(False)
        self.ui.lineEdit_search_term.setText("Software Engineer")
        self.ui.lineEdit_location.setText("Ankara, Turkey")
        self.ui.spinBox_fetch_count.setValue(1)
        self.ui.spinBox_hours_old.setValue(24)
        self.ui.checkBox_fetch_description.setChecked(True)

    def get_config(self) -> JobScraperConfig:
        config = JobScraperConfig()
        site_names = []
        if self.ui.checkBox_linkedin.isChecked():
            site_names.append("linkedin")
        if self.ui.checkBox_indeed.isChecked():
            site_names.append("indeed")
        if self.ui.checkBox_google.isChecked():
            site_names.append("google_jobs")
        config.site_names = site_names
        config.search_term = self.ui.lineEdit_search_term.text()
        config.location = self.ui.lineEdit_location.text()
        config.results_wanted = self.ui.spinBox_fetch_count.value()
        config.hours_old = self.ui.spinBox_hours_old.value()
        config.linkedin_fetch_description = self.ui.checkBox_fetch_description.isChecked()
        return config
    
    