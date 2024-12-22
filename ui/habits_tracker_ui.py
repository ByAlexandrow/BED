from PySide6.QtWidgets import (
    QPushButton, QDialog, QVBoxLayout, QHBoxLayout,
    QWidget, QFrame, QGridLayout, QScrollArea,
    QLineEdit, QCheckBox, QLabel
)
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPalette, QColor

from datetime import datetime, timedelta

from database.db_habits_manager import (
    create_habits_db, add_new_habit, get_all_habits,
    get_all_habits_checkpoints, update_checkpoint,
    delete_habit_from_db
)


class HabitsButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/habits.png")) 
        self.setIconSize(QSize(40, 40))
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.1);
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.2);
            }
        """)


class HabitsDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Habits Tracker")
        self.setFixedSize(900, 600)

        # Создаем таблицы в базе данных, если их нет
        create_habits_db()

        # Основной макет
        self.layout = QVBoxLayout()

        # Создаем QScrollArea для добавления скролла
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Виджет для содержимого QScrollArea
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)

        # Макет для квадратных виджетов внутри QScrollArea
        self.grid_layout = QGridLayout(self.scroll_content)
        self.grid_layout.setSpacing(10)

        # Добавляем QScrollArea в основной макет
        self.layout.addWidget(self.scroll_area)

        # Создаем футер
        footer_layout = QHBoxLayout()
        footer_widget = QWidget()
        footer_widget.setLayout(footer_layout)

        # Кнопка "Добавить задачу"
        self.add_habits_button = QPushButton()
        self.add_habits_button.setFixedSize(100, 30)
        self.add_habits_button.setIcon(QIcon("resources/icons/add.png"))
        self.add_habits_button.setIconSize(QSize(30, 30))
        self.add_habits_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border: 1px solid white;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.add_habits_button.clicked.connect(self.add_square_widget)

        # Добавляем кнопку в футер и центрируем её
        footer_layout.addStretch()
        footer_layout.addWidget(self.add_habits_button)
        footer_layout.addStretch()

        # Добавляем футер в основной layout
        self.layout.addWidget(footer_widget)

        self.setLayout(self.layout)

        # Счетчик для квадратных виджетов
        self.square_counter = 0

        # Загружаем привычки из базы данных
        self.load_habits()


    def add_square_widget(self):
        """Добавляет квадратный виджет в макет."""
        # Создаем квадратный виджет
        square_widget = QFrame()
        square_widget.setFixedSize(250, 400)
        square_widget.setStyleSheet("background-color: rgba(255, 255, 255, 0); border-radius: 25px; border: 1px solid white; color: white;")

        # Внутренний макет для квадрата (QGridLayout для чекпоинтов)
        square_layout = QGridLayout()
        square_widget.setLayout(square_layout)

        # Поле ввода названия привычки
        habit_label = QLineEdit()
        habit_label.setPlaceholderText("Title (does not change)")
        habit_label.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); border-radius: 15px; color: white; padding: 5px;")
        habit_label.setReadOnly(False)
        square_layout.addWidget(habit_label, 0, 0, 1, 7)

        # Поле текущего месяца
        current_month_label = datetime.today()
        month_name_label = QLabel(current_month_label.strftime('%d %B %Y'))
        month_name_label.setStyleSheet("color: white; border: none;")
        month_name_label.setAlignment(Qt.AlignCenter)
        square_layout.addWidget(month_name_label, 1, 0, 1, 7)

        # Добавляем чекпоинты для каждого дня текущего месяца
        checkboxes = self.add_checkpoints(square_layout)

        # Расположение кнопки "Удалить"
        buttons_layout = QHBoxLayout()
        square_layout.addLayout(buttons_layout, 12, 0, 1, 7)

        # Кнопка "Удалить"
        delete_habit = QPushButton("❌")
        delete_habit.setFixedSize(QSize(30, 30))
        delete_habit.setStyleSheet("""
            QPushButton {
                border-radius: 15px;
            }
        """)
        delete_habit.clicked.connect(lambda: self.delete_habit(square_widget))
        buttons_layout.addWidget(delete_habit)

        # Вычисляем позицию для нового квадрата
        row = self.square_counter // 3
        col = self.square_counter % 3

        # Добавляем квадрат в макет
        self.grid_layout.addWidget(square_widget, row, col)

        # Увеличиваем счетчик
        self.square_counter += 1

        # Если квадратов больше 3 в строке, добавляем новую строку
        if self.square_counter % 3 == 0:
            self.grid_layout.setRowStretch(row, 1)
        
        # Возвращаем созданный виджет
        return square_widget


    def add_checkpoints(self, layout):
        """Добавляет чекпоинты для каждого дня текущего месяца."""
        today = datetime.today()
        month_start = datetime(today.year, today.month, 1)
        month_end = datetime(today.year, today.month, 28) + timedelta(days=4)
        month_end = month_end - timedelta(days=month_end.day)

        current_date = month_start
        row = 2
        col = 0

        checkboxes = []

        while current_date <= month_end:
            # Создаем чекпоинт
            checkbox = QCheckBox()
            checkbox.setStyleSheet("""
                QCheckBox {
                    spacing: 0px;
                    margin: 5.5px;
                    padding: 0;
                    border: none;
                }
            """)

            # Создаем QLabel для отображения числа дня
            day_label = QLabel(current_date.strftime("%d"))
            day_label.setStyleSheet("color: white; font-size: 12px; border: none;")
            day_label.setAlignment(Qt.AlignCenter)

            # Ограничиваем установку чекпоинтов только на текущий день
            if current_date.date() == today.date():
                checkbox.setEnabled(True)
            else:
                checkbox.setEnabled(False)

            # Добавляем чекпоинт и QLabel в макет
            layout.addWidget(checkbox, row, col)
            layout.addWidget(day_label, row + 1, col)

            checkboxes.append(checkbox)

            col += 1
            if col == 7:
                col = 0
                row += 2

            current_date += timedelta(days=1)

        return checkboxes


    def delete_habit(self, square_widget):
        """Метод для удаления карточки привычки."""
        # Удаляем привычку из базы данных
        habit_label = square_widget.findChild(QLineEdit)
        habit_name = habit_label.text() or "Новая привычка"
        habit_id = add_new_habit(habit_name)
        delete_habit_from_db(habit_id)

        # Удаляем виджет из интерфейса
        self.grid_layout.removeWidget(square_widget)
        square_widget.deleteLater()
        self.square_counter -= 1


    def load_habits(self):
        """Загружает привычки из базы данных."""
        habits = get_all_habits()
        today = datetime.today()

        for habit in habits:
            habit_id, habit_name = habit

            # Добавляем квадратный виджет
            square_widget = self.add_square_widget()

            # Находим поле ввода названия привычки
            habit_label = square_widget.findChild(QLineEdit)
            habit_label.setText(habit_name)
            habit_label.setReadOnly(True)

            # Получаем чекпоинты для текущего месяца и года
            checkpoints = get_all_habits_checkpoints(habit_id, today.year, today.month)

            # Находим все чекпоинты в виджете
            checkboxes = square_widget.findChildren(QCheckBox)

            # Устанавливаем состояние чекпоинтов
            for day, checked in checkpoints:
                if day <= len(checkboxes):
                    checkboxes[day - 1].setChecked(checked == 1)
    

    def closeEvent(self, event):
        """Сохраняет данные в базу данных при закрытии окна."""
        if not self.validate_habits():
            event.ignore()
        else:
            self.save_habits()
            event.accept()


    def validate_habits(self):
        """Проверяет, заполнены ли все поля названий привычек."""
        valid = True
        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, QFrame):
                habit_label = widget.findChild(QLineEdit)
                if not habit_label.text().strip():  # Проверяем, заполнено ли поле
                    self.highlight_field(habit_label)
                    valid = False
        return valid


    def highlight_field(self, habit_label):
        """Подсвечивает поле ввода."""
        habit_label.setStyleSheet("""
                QLineEdit {
                    background-color: rgba(0, 0, 0, 0.4);
                    border: 1px solid rgba(255, 0, 0, 0.4);
                    border-radius: 15px;
                    color: white;
                    padding: 5px;
                }
            """)
        return habit_label


    def save_habits(self):
        """Обновляет состояние всех привычек и их чекпоинтов в базе данных."""
        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, QFrame):
                habit_label = widget.findChild(QLineEdit)
                checkboxes = widget.findChildren(QCheckBox)

                # Название привычки
                habit_name = habit_label.text().strip() or "Новая привычка"

                # Получаем ID привычки из базы данных
                habit_id = add_new_habit(habit_name)

                # Обновляем чекпоинты в базе данных
                today = datetime.today()
                for day, checkbox in enumerate(checkboxes, start=1):
                    update_checkpoint(habit_id, today.year, today.month, day, int(checkbox.isChecked()))

                habit_label.setReadOnly(True)
