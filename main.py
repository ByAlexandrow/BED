import sys

from PySide6.QtWidgets import QApplication

from database.db_tasks_manager import create_tasks_db
from database.db_habits_manager import create_habits_db
from database.db_notes_manager import create_notes_db

from ui.main_window_ui import MainWindow


if __name__ == "__main__":
    # Инициализация баз данных
    create_tasks_db()
    create_habits_db()
    create_notes_db()

    # Создание приложения
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
