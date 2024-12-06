from PySide6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

from ui.topbar import TopBar
from ui.dialog import Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('resources/favicon/main.png'))
        self.setWindowTitle("BED - Better Every Day")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

        self.setStyleSheet("""
            QMainWindow {
                background-image: url("resources/background/anonim.jpg");
                background-repeat: no-repeat;
                background-position: center;
            }
        """)


    def init_ui(self):
        self.top_bar = TopBar(self)
        self.top_bar.account_button.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.account))
        self.top_bar.about_button.clicked.connect(self.show_about_dialog)

        # Создаем основной виджет с вертикальным компоновщиком
        main_layout_widget = QWidget()
        main_layout = QVBoxLayout(main_layout_widget)

        # Добавляем TopBar в верхнюю часть
        main_layout.addWidget(self.top_bar)

        # Добавляем растягивающийся элемент, чтобы TopBar оставался сверху
        main_layout.addStretch()

        # Устанавливаем основной виджет в качестве центрального виджета
        self.setCentralWidget(main_layout_widget)


    def show_about_dialog(self):
        dialog = Dialog(self)
        dialog.exec()
