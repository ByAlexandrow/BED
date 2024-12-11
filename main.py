import sys

from PySide6.QtWidgets import QApplication

from database.db_manager import create_task_db

from ui.main_window_ui import MainWindow


if __name__ == "__main__":
    create_task_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())