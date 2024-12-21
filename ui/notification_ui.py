from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QSize


class NotificationButtonUI(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QIcon("resources/icons/notification.png")) 
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


class NotificationDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - Work Rest Balance")
        self.setFixedSize(600, 250)

        layout = QVBoxLayout()

        # Текст сверху
        self.label = QLabel("You will receive rest notifications every hour while your computer is running")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.label.setFont(font)
        layout.addWidget(self.label)

        # Уменьшаем расстояние между текстом и полем ввода
        layout.addSpacing(10)

        # Поле ввода для выбора времени
        self.time_combo = QComboBox()
        self.time_combo.addItems(["5 minutes - not recommended", "10 minutes - optimal time", "15 minutes - default time"])
        self.time_combo.setCurrentIndex(2)
        self.time_combo.setFixedSize(400, 40)
        self.time_combo.setStyleSheet("""
            QComboBox {
                background-color: rgba(255, 255, 255, 0.05); 
                border: 1px solid white;
                border-radius: 15px;
                padding: 10px;
                font-family: 'Arial';
                font-size: 14px;
            }
        """)
        layout.addWidget(self.time_combo, alignment=Qt.AlignCenter)

        layout.addSpacing(50)

        self.help_label = QLabel("You can change it at any time")
        self.help_label.setAlignment(Qt.AlignCenter)
        font = QFont("Georgia", 12)
        self.help_label.setFont(font)
        layout.addWidget(self.help_label)

        # Увеличиваем расстояние между полем ввода и кнопками
        layout.addSpacing(15)

        # Кнопки "Сохранить" и "Изменить"
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.save_button = QPushButton()
        self.save_button.setFixedSize(90, 50)
        self.save_button.setIcon(QIcon("resources/icons/save.png"))
        self.save_button.setIconSize(QSize(40, 40))
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.save_button.clicked.connect(self.save_data)

        self.change_button = QPushButton()
        self.change_button.setFixedSize(90, 50)
        self.change_button.setIcon(QIcon("resources/icons/edit.png"))
        self.change_button.setIconSize(QSize(40, 40))
        self.change_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                border: 1px solid white;
                border-radius: 15px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.change_button.clicked.connect(self.change_data)

        button_layout.addWidget(self.change_button)
        button_layout.addWidget(self.save_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        self.setLayout(layout)


    def save_data(self):
        selected_time = self.time_combo.currentText()
        print(f"Data saved with time: {selected_time}")


    def change_data(self):
        selected_time = self.time_combo.currentText()
        print(f"Data changed to time: {selected_time}")
