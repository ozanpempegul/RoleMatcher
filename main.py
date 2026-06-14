from dotenv import load_dotenv

load_dotenv(override=True)

from views.main_window.vm_main_window import*


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("RoleMatcher")
    app.setApplicationDisplayName("RoleMatcher")  # optional; user-facing name
    app.setOrganizationName("RoleMatcher")        # optional; used by QSettings paths
    main_window = MainWindow()
    main_window.setWindowTitle(app.applicationDisplayName())
    main_window.show()
    app.exec()
