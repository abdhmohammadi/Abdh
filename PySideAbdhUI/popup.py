

from PySide6.QtWidgets import QWidget, QDialog, QVBoxLayout, QLabel,QSizePolicy
from PySide6.QtCore import QTimer, QPropertyAnimation, Qt, QRect, QEasingCurve
from PySide6.QtGui import QGuiApplication, QPainter, QPainterPath, QBrush, QColor, QPen


class PopupNotifier(QWidget):

    __duration__ = 500
    __title_color__ ='#3A3A3A'
    __background__ ='#424242'
    __border_color__ = 'BLUE'
    
    def __init__(self,title_color='#3A3A3A',background_color ='#424242',border_color ='BLUE'):
        super().__init__()

        self.__title_color__ = title_color
        self.__background__ = background_color
        self.__border_color__ = border_color

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Popup)#.SubWindow)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        #self.setSizePolicy(QSizePolicy.Policy.Preferred,QSizePolicy.Policy.Preferred)
        self.setFixedSize(300, 110)  # Set the size of the popup
    
        # Layout and content
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(1, 1, 1, 1)

        self.title_label = QLabel("Notification")
        self.title_label.setFixedHeight(50)
        style = f"font-weight:bold; padding:5px; background-color:{self.__title_color__};"
        style += "border-top-left-radius:10px; border-top-right-radius:8px;border-bottom-left-radius:px; border-bottom-right-radius:0px;"
        self.title_label.setStyleSheet(style)

        self.message_label = QLabel("This is a sample message.")
        
        self.message_label.setStyleSheet("padding:5px;text-align:top; background-color:Transparent;")
        self.message_label.setMinimumHeight(100)
        self.message_label.setWordWrap(True)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.message_label)
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Animations for slide and opacity
        self.slide_animation = QPropertyAnimation(self, b"geometry")
        # Animation duration in milliseconds
        self.slide_animation.setDuration(self.__duration__)
        self.slide_animation.setEasingCurve(QEasingCurve.Type.OutBack)  # Smooth easing curve

        # Animation for opacity
        self.opacity_animation = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_animation.setDuration(self.__duration__)
        self.opacity_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)  # Smooth easing curve
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)

        #self.setFixedSize(self.title_label.sizeHint().width(),300)#.minimumSizeHint()
        # Timer for delay before closing
        self.close_timer = QTimer()
        self.close_timer.timeout.connect(self.start_close_animation)


    def show_popup(self,parent:QWidget=None, title='Notifiyer', message='', position="top-right", delay=3000):
        # Show the popup with the given title, message, position, slide direction, and delay.
        self.setParent(parent)
        parent_geometry: QRect = self.parent().geometry()
        self_size = self.size()

        self.title_label.setText(title)
        self.message_label.setText(message)

        # Set initial opacity
        self.setWindowOpacity(0)  # Start fully transparent
        self.position = position
        if position is not None:
            # Set initial position based on slide direction
            if position == "top-left":
                self.setGeometry(QRect(-self.width(), 10, self.width(), self.height()))
                end = QRect(10, 10, self.width(), self.height())
            elif position == "top-right":
                self.setGeometry(QRect(parent_geometry.width(), 10, self.width(), self.height()))
                end = QRect(parent_geometry.width() - self_size.width() - 10, 10, self.width(), self.height())
            elif position == "bottom-left":
                self.setGeometry(QRect(-self.width(), parent_geometry.height() - self_size.height() - 10, self.width(), self.height()))
                end = QRect(10, parent_geometry.height() - self_size.height() - 10, self.width(), self.height())
            elif position == "bottom-right":
                self.setGeometry(QRect(parent_geometry.width(), parent_geometry.height() - self_size.height() - 20, self.width(), self.height()))
                end = QRect(parent_geometry.width() - self_size.width() - 20, parent_geometry.height() - self_size.height() - 20, self.width(), self.height())

            # Slide-in animation
            self.show()
            self.slide_animation.setStartValue(self.geometry())
            self.slide_animation.setEndValue(end)
            self.slide_animation.start()

            # Opacity animation (fade in)
            #self.opacity_animation.setStartValue(0.0)  # Start fully transparent
            #self.opacity_animation.setEndValue(1.0)  # End fully opaque
            #self.opacity_animation.start()
        else:
            # No slide animation, just show at the specified position
            self.setGeometry(QRect((parent_geometry.width() - self_size.width()) / 2, (parent_geometry.height() - self_size.height()) / 2, self.width(), self.height()))
            
            self.setWindowOpacity(0.0)
            self.opacity_animation.start()
            #self.opacity_animation.setStartValue(0.0)
            #self.opacity_animation.setEndValue(1.0)
            self.show()
  

        # Start the delay timer for closing
        self.close_timer.start(delay)

    def start_close_animation(self):
        # Start the close animation based on the slide direction.
        if hasattr(self, "position") and self.position is not None:
            self.slide_out()
        else:
            self.fade_out()

    def slide_out(self):
        # Slide-out and fade-out animation before closing the popup.
        position = getattr(self, "position", "top-right")  # Default to "top" if not set
        parent_geometry: QRect = self.parent().geometry()
        self_size = self.size()
        if position is not None:
            if position == "top-right":
                end_geometry = QRect(parent_geometry.width(), 10, self.width(), self.height())
            elif position == "top-left":
                end_geometry = QRect(-self.width(), 10, self.width(), self.height())
            elif position == "bottom-left":
                end_geometry = QRect(-self.width(), parent_geometry.height() - self_size.height() - 10, self.width(), self.height())
            elif position == "bottom-right":
                end_geometry = QRect(parent_geometry.width(), parent_geometry.height() - self_size.height() - 10, self.width(), self.height())

            # Slide-out animation
            self.slide_animation.setStartValue(self.geometry())
            self.slide_animation.setEndValue(end_geometry)
            self.slide_animation.finished.connect(self.close)
            self.slide_animation.start()

    def fade_out(self):
        # Fade-out animation before closing the popup.
        self.opacity_animation.setStartValue(1.0)
        self.opacity_animation.setEndValue(0.0)
        self.opacity_animation.finished.connect(self.close)
        self.opacity_animation.start()

    def closeEvent(self, event):
        # Clean up when closing the popup.
        self.close_timer.stop()
        event.accept()

    def paintEvent(self, event):
        # Draw the popup with rounded corners and a shadow effect.
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw the background with rounded corners
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 10, 10)
        painter.fillPath(path, QBrush(self.__border_color__)) # border

        # Draw a shadow effect
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(self.__background__))
        painter.drawRoundedRect(self.rect().translated(2, 2), 10, 10)

    @staticmethod
    def Notify(parent:QWidget,title='Notifiyer',message:str='',position='bottom-right',delay=5000,
               title_color='#3A3A3A',background_color ='#424242',border_color ='BLUE'):
        popup = PopupNotifier(title_color,background_color,border_color)

        popup.show_popup(parent,title, message, position, delay=delay)



