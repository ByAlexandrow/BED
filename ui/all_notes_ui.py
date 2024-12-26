from PySide6.QtWidgets import QDialog


class AllNotesDialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("BED - All Notes")
        self.setFixedSize(900, 600)
