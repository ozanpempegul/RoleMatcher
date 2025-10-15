from dotenv import load_dotenv
from views.main_window.vm_main_window import*


if __name__ == "__main__":
    # init env
    load_dotenv()

    # init ui
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
