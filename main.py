import sys

from PySide6.QtWidgets import QApplication

from database.db_task_manager import create_task_db
from database.db_settings_manager import create_settings_db

from ui.main_window_ui import MainWindow


if __name__ == "__main__":
    create_task_db()
    create_settings_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())