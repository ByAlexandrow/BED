from PySide6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

from ui.topbar import TopBar


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
        self.top_bar.about_button.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.about_dialog))

        self.setMenuWidget(self.top_bar)