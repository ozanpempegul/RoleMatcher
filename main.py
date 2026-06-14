from dotenv import load_dotenv

load_dotenv(override=True)

from views.main_window.vm_main_window import*


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
