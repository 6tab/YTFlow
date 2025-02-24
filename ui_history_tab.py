from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton

class HistoryTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # History List
        self.history_list = QListWidget()
        layout.addWidget(self.history_list)

        # Redownload Button
        self.redownload_button = QPushButton("Redownload")
        layout.addWidget(self.redownload_button)

        self.setLayout(layout)