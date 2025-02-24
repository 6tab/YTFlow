from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, 
                           QPushButton, QComboBox, QProgressBar, QLabel,
                           QFrame, QScrollArea)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from animations import ButtonClickAnimation

class DownloadsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Main content area with scroll
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: #2A2A2A;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #3A86FF;
                border-radius: 5px;
            }
        """)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)

        # URL Input Section
        url_frame = QFrame()
        url_frame.setStyleSheet("""
            QFrame {
                background-color: #2A2A2A;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        url_layout = QHBoxLayout(url_frame)
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste YouTube URL here...")
        self.url_input.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #3A86FF;
                border-radius: 5px;
                background: #1E1E1E;
                color: white;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #2A6FD1;
            }
        """)

        self.paste_button = QPushButton("Paste")
        self.paste_button.setStyleSheet("""
            QPushButton {
                background-color: #3A86FF;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2A6FD1;
            }
        """)
        self.paste_button.clicked.connect(self.animate_button)

        url_layout.addWidget(self.url_input)
        url_layout.addWidget(self.paste_button)
        content_layout.addWidget(url_frame)

        # Format and Quality Selection
        options_frame = QFrame()
        options_frame.setStyleSheet("""
            QFrame {
                background-color: #2A2A2A;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        options_layout = QHBoxLayout(options_frame)

        # Format selection
        format_layout = QVBoxLayout()
        format_label = QLabel("Format")
        format_label.setStyleSheet("color: white; font-weight: bold;")
        self.format_combo = QComboBox()
        self.format_combo.addItems(["MP4", "MP3", "WAV", "M4A"])
        self.format_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 2px solid #3A86FF;
                border-radius: 5px;
                background: #1E1E1E;
                color: white;
                min-width: 100px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: url(resources/down_arrow.png);
                width: 12px;
                height: 12px;
            }
        """)
        format_layout.addWidget(format_label)
        format_layout.addWidget(self.format_combo)

        # Quality selection
        quality_layout = QVBoxLayout()
        quality_label = QLabel("Quality")
        quality_label.setStyleSheet("color: white; font-weight: bold;")
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["1080p", "720p", "480p", "360p", "Auto"])
        self.quality_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 2px solid #3A86FF;
                border-radius: 5px;
                background: #1E1E1E;
                color: white;
                min-width: 100px;
            }
        """)
        quality_layout.addWidget(quality_label)
        quality_layout.addWidget(self.quality_combo)

        options_layout.addLayout(format_layout)
        options_layout.addLayout(quality_layout)
        options_layout.addStretch()
        content_layout.addWidget(options_frame)

        # Download Button
        self.download_button = QPushButton("Download")
        self.download_button.setStyleSheet("""
            QPushButton {
                background-color: #3A86FF;
                color: white;
                padding: 15px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2A6FD1;
            }
            QPushButton:pressed {
                background-color: #1A5FB1;
            }
        """)
        self.download_button.clicked.connect(self.animate_button)
        content_layout.addWidget(self.download_button)

        # Progress Section
        progress_frame = QFrame()
        progress_frame.setStyleSheet("""
            QFrame {
                background-color: #2A2A2A;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        progress_layout = QVBoxLayout(progress_frame)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #3A86FF;
                border-radius: 5px;
                background: #1E1E1E;
                padding: 2px;
                height: 20px;
            }
            QProgressBar::chunk {
                background-color: #3A86FF;
                border-radius: 3px;
            }
        """)
        progress_layout.addWidget(self.progress_bar)

        # Status Label
        self.status_label = QLabel("Ready")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("""
            QLabel {
                color: white;
                padding: 5px;
                font-size: 12px;
            }
        """)
        progress_layout.addWidget(self.status_label)

        content_layout.addWidget(progress_frame)
        content_layout.addStretch()

        # Set the scroll area content
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        self.setLayout(layout)

    def animate_button(self):
        """Animate the clicked button."""
        button = self.sender()
        if button:
            ButtonClickAnimation(button).animate()