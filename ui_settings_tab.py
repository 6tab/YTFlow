from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QCheckBox,
    QComboBox, QLabel, QSpinBox, QGroupBox, QLineEdit
)
from PyQt6.QtCore import Qt, QEasingCurve, QPropertyAnimation  # Fix: Import QEasingCurve and QPropertyAnimation

class CollapsibleGroupBox(QGroupBox):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setCheckable(True)
        self.setChecked(True)
        self.animation = QPropertyAnimation(self, b"maximumHeight")
        self.animation.setDuration(300)  # 300ms animation
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)  # Fix: Use QEasingCurve.Type

        self.toggled.connect(self.toggle_collapse)

    def toggle_collapse(self, checked):
        """Toggle the collapse state of the group box."""
        if checked:
            self.animation.setStartValue(0)
            self.animation.setEndValue(self.sizeHint().height())
        else:
            self.animation.setStartValue(self.sizeHint().height())
            self.animation.setEndValue(0)
        self.animation.start()

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # General Settings Group
        general_group = CollapsibleGroupBox("General Settings")
        general_layout = QVBoxLayout()

        # Download Folder Selection
        folder_layout = QHBoxLayout()
        self.folder_path = QLineEdit()
        self.folder_path.setPlaceholderText("Default Download Path")
        self.folder_path.setReadOnly(True)
        self.folder_button = QPushButton("Change Download Folder")
        self.folder_button.clicked.connect(self.select_folder)
        folder_layout.addWidget(self.folder_path)
        folder_layout.addWidget(self.folder_button)
        general_layout.addLayout(folder_layout)

        # Theme Settings
        self.theme_checkbox = QCheckBox("Enable Dark Mode")
        self.theme_checkbox.setChecked(True)
        general_layout.addWidget(self.theme_checkbox)

        # Concurrent Downloads
        downloads_layout = QHBoxLayout()
        downloads_layout.addWidget(QLabel("Maximum Concurrent Downloads:"))
        self.max_downloads = QSpinBox()
        self.max_downloads.setRange(1, 5)
        self.max_downloads.setValue(2)
        downloads_layout.addWidget(self.max_downloads)
        downloads_layout.addStretch()
        general_layout.addLayout(downloads_layout)

        general_group.setLayout(general_layout)
        layout.addWidget(general_group)

        # Auto-Encode Settings Group
        encode_group = CollapsibleGroupBox("Auto-Encode Settings")
        encode_layout = QVBoxLayout()

        # Enable Auto-Encode
        self.auto_encode_checkbox = QCheckBox("Enable Auto-Encode")
        encode_layout.addWidget(self.auto_encode_checkbox)

        # Output Format
        format_layout = QHBoxLayout()
        format_layout.addWidget(QLabel("Output Format:"))
        self.format_combo = QComboBox()
        self.format_combo.addItems(["MP4", "MKV", "AVI", "WebM"])
        format_layout.addWidget(self.format_combo)
        format_layout.addStretch()
        encode_layout.addLayout(format_layout)

        # Video Quality
        quality_layout = QHBoxLayout()
        quality_layout.addWidget(QLabel("Video Quality:"))
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["Original", "1080p", "720p", "480p", "360p"])
        quality_layout.addWidget(self.quality_combo)
        quality_layout.addStretch()
        encode_layout.addLayout(quality_layout)

        # Audio Settings
        audio_layout = QHBoxLayout()
        audio_layout.addWidget(QLabel("Audio Bitrate:"))
        self.audio_combo = QComboBox()
        self.audio_combo.addItems(["Original", "320k", "256k", "192k", "128k"])
        audio_layout.addWidget(self.audio_combo)
        audio_layout.addStretch()
        encode_layout.addLayout(audio_layout)

        # Hardware Acceleration
        self.hw_accel_checkbox = QCheckBox("Enable Hardware Acceleration")
        encode_layout.addWidget(self.hw_accel_checkbox)

        encode_group.setLayout(encode_layout)
        layout.addWidget(encode_group)

        # Download Settings Group
        download_group = CollapsibleGroupBox("Download Settings")
        download_layout = QVBoxLayout()

        # Subtitle Options
        self.auto_subs_checkbox = QCheckBox("Auto-Download Subtitles")
        download_layout.addWidget(self.auto_subs_checkbox)

        # Preferred Language
        lang_layout = QHBoxLayout()
        lang_layout.addWidget(QLabel("Preferred Language:"))
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["English", "Spanish", "French", "German", "Japanese"])
        lang_layout.addWidget(self.lang_combo)
        lang_layout.addStretch()
        download_layout.addLayout(lang_layout)

        # Thumbnail Options
        self.thumbnail_checkbox = QCheckBox("Download Thumbnail")
        download_layout.addWidget(self.thumbnail_checkbox)

        # Auto-Start Download
        self.autostart_checkbox = QCheckBox("Auto-Start Downloads")
        download_layout.addWidget(self.autostart_checkbox)

        download_group.setLayout(download_layout)
        layout.addWidget(download_group)

        # Add stretch to push everything to the top
        layout.addStretch()
        self.setLayout(layout)

    def select_folder(self):
        """Open a file dialog to select the download folder."""
        folder = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        if folder:
            self.folder_path.setText(folder)