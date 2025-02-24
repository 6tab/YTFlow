from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QLinearGradient, QColor, QPainterPath
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, QRect, QPoint

class GradientBackground(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)
        self.offset = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Create gradient background
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor("#1E1E1E"))
        gradient.setColorAt(1, QColor("#2A2A2A"))
        painter.fillRect(self.rect(), gradient)
        
        # Add subtle animated pattern
        painter.setPen(QColor("#3A86FF"))
        self.offset = (self.offset + 1) % 20
        for i in range(-20, self.width() + 20, 20):
            painter.drawLine(i + self.offset, 0, i + self.offset - 20, self.height())

class TabSwitchAnimation:
    def __init__(self, widget):
        self.widget = widget
        self.animation = QPropertyAnimation(self.widget, b"geometry")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def animate(self, start_rect, end_rect):
        # Slide animation
        self.animation.setStartValue(QRect(start_rect.x() + 50, start_rect.y(), 
                                         start_rect.width(), start_rect.height()))
        self.animation.setEndValue(end_rect)
        self.animation.start()

class ButtonClickAnimation:
    def __init__(self, button):
        self.button = button
        self.animation_group = QPropertyAnimation(self.button, b"geometry")
        self.animation_group.setDuration(200)
        self.animation_group.setEasingCurve(QEasingCurve.Type.OutBack)

    def animate(self):
        start_rect = self.button.geometry()
        # Scale down and up animation
        self.animation_group.setStartValue(start_rect)
        scaled_rect = QRect(
            start_rect.x() + 2,
            start_rect.y() + 2,
            start_rect.width() - 4,
            start_rect.height() - 4
        )
        self.animation_group.setKeyValueAt(0.5, scaled_rect)
        self.animation_group.setEndValue(start_rect)
        self.animation_group.start()