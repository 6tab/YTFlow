from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QPushButton, QStackedWidget, QLabel, QFrame)
from PyQt6.QtGui import QIcon, QColor, QLinearGradient, QPainter, QFont
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QSize
from ui_downloads_tab import DownloadsTab
from ui_auto_encode_tab import AutoEncodeTab
from ui_settings_tab import SettingsTab
from ui_history_tab import HistoryTab
from ui_about_tab import AboutTab
from animations import GradientBackground, TabSwitchAnimation, ButtonClickAnimation

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon("resources/app_icon.png"))
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1E1E1E;
            }
        """)

        # Main layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QHBoxLayout(self.main_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("""
            QFrame {
                background-color: #2A2A2A;
                border-right: 2px solid #3A86FF;
            }
        """)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setSpacing(5)
        self.sidebar_layout.setContentsMargins(10, 20, 10, 20)

        # App title in sidebar
        title_label = QLabel("YouTube\nDownloader")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #3A86FF; padding: 10px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(title_label)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background-color: #3A86FF;")
        self.sidebar_layout.addWidget(separator)
        
        # Stacked widget for content
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet("""
            QStackedWidget {
                background-color: #1E1E1E;
                border-radius: 10px;
                margin: 10px;
            }
        """)

        # Add tabs
        self.tabs = {
            "Downloads": DownloadsTab(),
            "Auto Encode": AutoEncodeTab(),
            "Settings": SettingsTab(),
            "History": HistoryTab(),
            "About": AboutTab(),
        }

        # Create tab buttons with consistent styling
        button_style = """
            QPushButton {
                background-color: transparent;
                color: white;
                padding: 15px;
                border-radius: 5px;
                text-align: left;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3A86FF;
            }
            QPushButton:checked {
                background-color: #3A86FF;
                border-left: 4px solid white;
            }
        """

        self.tab_buttons = {}
        for name, tab in self.tabs.items():
            self.stacked_widget.addWidget(tab)
            
            button = QPushButton(name)
            button.setCheckable(True)
            button.setStyleSheet(button_style)
            button.setFixedHeight(50)
            button.clicked.connect(lambda checked, n=name: self.switch_tab(n))
            
            # Add icon to button
            icon = QIcon(f"resources/tab_icons/{name.lower()}.png")
            button.setIcon(icon)
            button.setIconSize(QSize(20, 20))
            
            self.tab_buttons[name] = button
            self.sidebar_layout.addWidget(button)

        # Add stretch to push buttons to top
        self.sidebar_layout.addStretch()

        # Version label at bottom
        version_label = QLabel("v1.0.0")
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version_label.setStyleSheet("color: #666666;")
        self.sidebar_layout.addWidget(version_label)

        # Add sidebar and stacked widget to main layout
        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.stacked_widget)

        # Set default tab
        self.switch_tab("Downloads")

    def switch_tab(self, name):
        # Update button states
        for button_name, button in self.tab_buttons.items():
            button.setChecked(button_name == name)

        # Animate tab switch
        tab_animation = TabSwitchAnimation(self.stacked_widget)
        start_rect = self.stacked_widget.geometry()
        end_rect = start_rect
        tab_animation.animate(start_rect, end_rect)
        self.stacked_widget.setCurrentWidget(self.tabs[name])