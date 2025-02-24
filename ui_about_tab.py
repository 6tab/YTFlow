from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import webbrowser  # Use Python's built-in webbrowser module

class AboutTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # App Icon
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QIcon("resources/app_icon.png").pixmap(64, 64))
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.icon_label)

        # Version Info
        self.version_label = QLabel("Version: 1.0.0")
        self.version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.version_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.version_label)

        # Developer Credits
        self.credits_label = QLabel("Developed by 6tab")
        self.credits_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.credits_label.setStyleSheet("font-size: 12px; font-weight: bold;")
        layout.addWidget(self.credits_label)

        # GitHub Link
        self.github_button = QPushButton("Visit GitHub")
        self.github_button.setStyleSheet("""
            QPushButton {
                background-color: #3A86FF;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2A6FD1;
            }
        """)
        self.github_button.clicked.connect(self.open_github)
        layout.addWidget(self.github_button)

        self.setLayout(layout)

    def open_github(self):
        """Open the GitHub page in the default web browser."""
        webbrowser.open("https://github.com/6tab/")