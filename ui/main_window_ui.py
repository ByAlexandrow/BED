from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

from ui.topbar import TopBar
from ui.about_dialog_ui import AboutDialogUI
from ui.account_dialog_ui import AccountDialogUI
from ui.task_manager_ui import TaskManagerUI
from ui.footer import Footer
from ui.chat_ui import ChatButtonUI, ChatDialogUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('resources/favicon/main.png'))
        self.setWindowTitle("BED - Better Every Day")

        # Устанавливаем размеры окна
        self.setGeometry(100, 100, 1300, 750)

        # Инициализируем интерфейс
        self.init_ui()

        # Устанавливаем стиль для главного окна
        self.setStyleSheet("""
            QMainWindow {
                background-image: url("resources/background/anonim.jpg");
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

    def init_ui(self):
        # Создаём TopBar
        self.top_bar = TopBar(self)
        self.top_bar.account_button.clicked.connect(self.show_account_dialog)
        self.top_bar.about_button.clicked.connect(self.show_about_dialog)

        # Создаём интерфейс TaskManagerUI
        self.task_manager_ui = TaskManagerUI()

        # Устанавливаем фиксированные размеры для TaskManagerUI
        self.task_manager_ui.setFixedWidth(300)

        # Создаём основной виджет с вертикальным компоновщиком
        main_layout_widget = QWidget()
        main_layout = QVBoxLayout(main_layout_widget)

        # Добавляем TopBar в верхнюю часть
        main_layout.addWidget(self.top_bar)

        # Создаём горизонтальный макет для TaskManagerUI и остального содержимого
        content_layout = QHBoxLayout()

        # Добавляем TaskManagerUI слева
        content_layout.addWidget(self.task_manager_ui)

        # Добавляем растягивающийся элемент, чтобы TaskManagerUI оставался слева
        content_layout.addStretch()

        # Добавляем горизонтальный макет в основной вертикальный макет
        main_layout.addLayout(content_layout)

        # Добавляем Footer в нижнюю часть
        self.footer = Footer()
        main_layout.addWidget(self.footer)

        # Устанавливаем основной виджет в качестве центрального виджета
        self.setCentralWidget(main_layout_widget)

        # Добавляем кнопку чата в правый нижний угол
        self.chat_button = ChatButtonUI(self)
        self.chat_button.clicked.connect(self.show_chat_dialog)
        self.update_chat_button_position()  # Устанавливаем начальную позицию кнопки

        # Подключаем обработчик изменения размеров окна
        self.resizeEvent = self.on_resize


    def show_about_dialog(self):
        about_dialog = AboutDialogUI(self)
        about_dialog.exec()
    

    def show_account_dialog(self):
        account_dialog = AccountDialogUI(self)
        account_dialog.exec()

    
    def show_chat_dialog(self):
        chat_dialog = ChatDialogUI(self)
        chat_dialog.exec()


    def update_chat_button_position(self):
        """
        Обновляет позицию кнопки чата в правом нижнем углу окна.
        """
        # Получаем размеры окна
        window_width = self.width()
        window_height = self.height()

        # Вычисляем позицию кнопки
        button_width = self.chat_button.width()
        button_height = self.chat_button.height()
        x = window_width - button_width - 20  # Отступ справа
        y = window_height - button_height - 35  # Отступ снизу

        # Устанавливаем позицию кнопки
        self.chat_button.move(x, y)


    def on_resize(self, event):
        """
        Обрабатывает событие изменения размеров окна.
        """
        self.update_chat_button_position()
        super().resizeEvent(event)
