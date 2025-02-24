from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                           QComboBox, QPushButton, QFrame, QScrollArea,
                           QFileDialog, QProgressBar)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QDragEnterEvent, QDropEvent

class AutoEncodeTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setAcceptDrops(True)

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Scroll Area
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

        # Drag and Drop Area
        self.drop_area = QFrame()
        self.drop_area.setMinimumHeight(200)
        self.drop_area.setStyleSheet("""
            QFrame {
                background-color: #2A2A2A;
                border: 2px dashed #3A86FF;
                border-radius: 10px;
            }
        """)
        drop_layout = QVBoxLayout(self.drop_area)
        
        drop_label = QLabel("Drag and drop video files here\nor")
        drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        drop_label.setStyleSheet("color: white; font-size: 14px;")
        
        self.browse_button = QPushButton("Browse Files")
        self.browse_button.setStyleSheet("""
            QPushButton {
                background-color: #3A86FF;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
                max-width: 150px;
            }
            QPushButton:hover {
                background-color: #2A6FD1;
            }
        """)
        self.browse_button.clicked.connect(self.browse_files)
        
        drop_layout.addWidget(drop_label)
        drop_layout.addWidget(self.browse_button, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(self.drop_area)

        # Encoding Options
        options_frame = QFrame()
        options_frame.setStyleSheet("""
            QFrame {
                background-color: #2A2A2A;
                border-radius: 10px;
                padding: 15px;
            }
        """)
        options_layout = QVBoxLayout(options_frame)

        # Format Selection
        format_layout = QHBoxLayout()
        format_label = QLabel("Output Format:")
        format_label.setStyleSheet("color: white; font-weight: bold;")
        self.format_combo = QComboBox()
        self.format_combo.addItems(["MP4", "MKV", "AVI", "WebM"])
        self.format_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 2px solid #3A86FF;
                border-radius: 5px;
                background: #1E1E1E;
                color: white;
                min-width: 150px;
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
        format_layout.addStretch()
        options_layout.addLayout(format_layout)

        # Quality Selection
        quality_layout = QHBoxLayout()
        quality_label = QLabel("Video Quality:")
        quality_label.setStyleSheet("color: white; font-weight: bold;")
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["Original", "1080p", "720p", "480p", "360p"])
        self.quality_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 2px solid #3A86FF;
                border-radius: 5px;
                background: #1E1E1E;
                color: white;
                min-width: 150px;
            }
        """)
        quality_layout.addWidget(quality_label)
        quality_layout.addWidget(self.quality_combo)
        quality_layout.addStretch()
        options_layout.addLayout(quality_layout)

        # Audio Quality Selection
        audio_layout = QHBoxLayout()
        audio_label = QLabel("Audio Quality:")
        audio_label.setStyleSheet("color: white; font-weight: bold;")
        self.audio_combo = QComboBox()
        self.audio_combo.addItems(["Original", "320kbps", "256kbps", "192kbps", "128kbps"])
        self.audio_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 2px solid #3A86FF;
                border-radius: 5px;
                background: #1E1E1E;
                color: white;
                min-width: 150px;
            }
        """)
        audio_layout.addWidget(audio_label)
        audio_layout.addWidget(self.audio_combo)
        audio_layout.addStretch()
        options_layout.addLayout(audio_layout)

        content_layout.addWidget(options_frame)

        # Encode Button
        self.encode_button = QPushButton("Start Encoding")
        self.encode_button.setStyleSheet("""
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
        """)
        content_layout.addWidget(self.encode_button)

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
        content_layout.addWidget(self.progress_bar)

        content_layout.addStretch()
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        self.setLayout(layout)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        """Handle dropped files."""
        if event.mimeData().hasUrls():
            self.files = [url.toLocalFile() for url in event.mimeData().urls()]
            self.update_drop_area()

    def browse_files(self):
        """Open a file dialog to select video files."""
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Video Files", "", "Video Files (*.mp4 *.mkv *.avi *.webm)"
        )
        if files:
            self.files = files
            self.update_drop_area()

    def update_drop_area(self):
        """Update the drop area to show the selected files."""
        if hasattr(self, 'files') and self.files:
            file_list = "\n".join([f"• {file.split('/')[-1]}" for file in self.files])
            self.drop_area.findChild(QLabel).setText(f"Selected Files:\n{file_list}")
            self.drop_area.setStyleSheet("""
                QFrame {
                    background-color: #2A2A2A;
                    border: 2px solid #3A86FF;
                    border-radius: 10px;
                }
            """)
        else:
            self.drop_area.findChild(QLabel).setText("Drag and drop video files here\nor")
            self.drop_area.setStyleSheet("""
                QFrame {
                    background-color: #2A2A2A;
                    border: 2px dashed #3A86FF;
                    border-radius: 10px;
                }
            """)

    def start_encoding(self):
        """Start encoding the selected files."""
        if not hasattr(self, 'files') or not self.files:
            self.show_error("No files selected!")
            return

        # Get encoding options
        output_format = self.format_combo.currentText().lower()
        video_quality = self.quality_combo.currentText()
        audio_quality = self.audio_combo.currentText()

        # Start encoding process
        self.encode_button.setEnabled(False)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(len(self.files))

        for index, file in enumerate(self.files):
            self.encode_file(file, output_format, video_quality, audio_quality)
            self.progress_bar.setValue(index + 1)

        self.encode_button.setEnabled(True)
        self.show_success("Encoding completed!")

    def encode_file(self, file, output_format, video_quality, audio_quality):
        """Encode a single file."""
        import subprocess
        output_file = file.replace(".", f"_encoded.{output_format}")

        # Build FFmpeg command
        command = [
            "ffmpeg",
            "-i", file,
            "-c:v", "libx264" if output_format == "mp4" else "libvpx-vp9",
            "-c:a", "aac" if output_format == "mp4" else "libvorbis",
            "-b:v", self.get_video_bitrate(video_quality),
            "-b:a", self.get_audio_bitrate(audio_quality),
            output_file
        ]

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            self.show_error(f"Failed to encode {file}: {e}")

    def get_video_bitrate(self, quality):
        """Get video bitrate based on quality selection."""
        return {
            "Original": "0",
            "1080p": "5000k",
            "720p": "2500k",
            "480p": "1000k",
            "360p": "500k",
        }.get(quality, "0")

    def get_audio_bitrate(self, quality):
        """Get audio bitrate based on quality selection."""
        return {
            "Original": "0",
            "320kbps": "320k",
            "256kbps": "256k",
            "192kbps": "192k",
            "128kbps": "128k",
        }.get(quality, "0")

    def show_error(self, message):
        """Show an error message."""
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.critical(self, "Error", message)

    def show_success(self, message):
        """Show a success message."""
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self, "Success", message)            