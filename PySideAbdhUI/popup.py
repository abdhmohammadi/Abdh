
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer, QPropertyAnimation, Qt
from PySide6.QtGui import QGuiApplication

class Popup(QDialog):
    def __init__(self,duration=3000,parent=None):

        if not parent: parent = QApplication.activeWindow() 

        super().__init__(parent=parent)
        self.setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint)  # Remove window decorations
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Make the background translucent
        #self.setModal(False)  # Make it a modal dialog
        
        # Set up the opacity animation
        self.opacity_animation = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_animation.setDuration(duration)  # Animation duration in milliseconds
        self.opacity_animation.setStartValue(0.0)  # Start fully transparent
        self.opacity_animation.setEndValue(1.0)  # End fully opaque

        # Set up the timer to close the dialog after 5 seconds
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.close)  # Ensure the dialog closes, not just the label

    @staticmethod
    def ShowMessage(message,parent,duration=3000,background='GREEN'):
        
        self = Popup(parent=parent,duration=duration)
        self.setStyleSheet(f'background-color:{background};color:black;padding:10px;border-radius:8px')

        # Set up the layout and message
        layout = QVBoxLayout(self)
        self.label = QLabel(message)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Center the dialog on the parent or screen
        if self.parent():
            parent_geometry = self.parent().geometry()
            self.move(parent_geometry.center() - self.rect().center())
        else:
            screen_geometry = QGuiApplication.primaryScreen().geometry()
            self.move(screen_geometry.center() - self.rect().center())

        # Start the opacity animation
        self.setWindowOpacity(0.0)  # Start fully transparent
        self.opacity_animation.start()

        # Show the dialog
        self.show()

        # Start the timer to close the dialog after 5 seconds
        self.timer.start(duration)
