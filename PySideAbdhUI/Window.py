dark_olive_stylesheet = """
QWidget {
    background-color: #2E2E2E;  /* Dark background color */
    color: #F1F1F1;  /* Light text color */
    font-family: Arial, sans-serif;
    border-radius: 8px;
    border:none
}

/* QMainWindow */
QMainWindow {
    background-color: #2E2E2E;
    border: none;
    border-radius: 8px;
}

/* QPushButton */
QPushButton {
    background-color:rgb(24, 25, 23);
    border: 1px solidrgb(20, 22, 20);
    border-radius: 5px;
    padding: 5px 10px;
    color: white;
}
QPushButton:hover {
    background-color: #558B2F;
}
QPushButton:pressed {
    background-color: #33691E;
}

QLabel { border: none; background-color: transparent; color: white; padding: 0px; }

/* QLineEdit */
QLineEdit {
    background-color: #424242;
    border: 1px solid #388E3C;
    border-radius: 5px;
    padding: 5px;
    color: #F1F1F1;
}

/* QFrame */
QFrame {
    background-color: #2E2E2E;
    border: 1px solid #558B2F;
    border-radius: 2px;
}

/* QMenuBar */
QMenuBar {
    background-color: #2E2E2E;
    border: none;
    border-radius: 2px;
}
QMenuBar::item {
    background-color: #2E2E2E;
    color: #F1F1F1;
}
QMenuBar::item:selected {
    background-color: #558B2F;
}
QMenuBar::item:pressed {
    background-color: #33691E;
}

/* QMenu */
QMenu {
    background-color: #2E2E2E;
    border: 1px solid #558B2F;
    border-radius: 2px;
}
QMenu::item {
    background-color: #2E2E2E;
    color: #F1F1F1;
}
QMenu::item:selected {
    background-color: #558B2F;
}

/* QScrollBar */
QScrollBar:horizontal {
    background-color: #2E2E2E;
    height: 15px;
    margin: 0px 20px 0 20px;
    border: 1px solid #388E3C;
    border-radius: 2px;
}
QScrollBar::handle:horizontal {
    background-color: #8BC34A;
    min-width: 20px;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    background-color: #558B2F;
    width: 20px;
    subcontrol-origin: margin;
    border-radius: 2px;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background-color: #2E2E2E;
    border-radius: 2px;
}

QScrollBar:vertical {
    background-color: #2E2E2E;
    width: 15px;
    margin: 20px 0 20px 0;
    border: 1px solid #388E3C;
    border-radius: 2px;
}
QScrollBar::handle:vertical {
    background-color: #8BC34A;
    min-height: 20px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: #558B2F;
    height: 20px;
    subcontrol-origin: margin;
    border-radius: 2px;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background-color: #2E2E2E;
    border-radius: 2px;
}

/* QCheckBox */
QCheckBox {
    background-color: #2E2E2E;
    color: #F1F1F1;
    border-radius: 2px;
}
QCheckBox::indicator {
    border: 1px solid #388E3C;
    width: 15px;
    height: 15px;
    border-radius: 2px;
}
QCheckBox::indicator:checked {
    background-color: #8BC34A;
}

/* QRadioButton */
QRadioButton {
    background-color: #2E2E2E;
    color: #F1F1F1;
    border-radius: 2px;
}
QRadioButton::indicator {
    border: 1px solid #388E3C;
    width: 15px;
    height: 15px;
    border-radius: 2px;
}
QRadioButton::indicator:checked {
    background-color: #8BC34A;
}

/* QTabBar */
QTabBar::tab {
    background-color: #8BC34A;
    color: white;
    padding: 5px;
    border: 1px solid #388E3C;
    border-radius: 2px;
}
QTabBar::tab:selected {
    background-color: #689F38;
}
QTabBar::tab:hover {
    background-color: #558B2F;
}

/* QProgressBar */
QProgressBar {
    background-color: #424242;
    border: 1px solid #388E3C;
    border-radius: 2px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #8BC34A;
    border-radius: 2px;
}

/* QToolTip */
QToolTip {
    background-color: #2E2E2E;
    color: #F1F1F1;
    border: 1px solid #558B2F;
    border-radius: 2px;
}

/* QTableWidget */
QTableWidget {
    background-color: #2E2E2E;
    color: #F1F1F1;
    gridline-color: #558B2F;
    border-radius: 2px;
}
QTableWidget::item {
    background-color: #2E2E2E;
    color: #F1F1F1;
    border-radius: 2px;
}
QTableWidget::item:selected {
    background-color: #558B2F;
    color: #F1F1F1;
    border-radius: 2px;
}
"""

close_button_stylesheet = """
            QPushButton {
            font-family:Segoe Fluent Icons;
            background-color: transparent;
            color: white;
            padding: 10px;
            border-top-left-radius: 0px;
            border-bottom-right-radius: 0px;
            border-top-right-radius: 8px;
            border-bottom-left-radius: 0px;
            border-width: 0px;
            }
            QPushButton:hover { background-color:rgb(214, 14, 14); }
            """

mx_button_stylesheet = """
            QPushButton {
            font-family:Segoe Fluent Icons;
            background-color: transparent;
            color: white;
            padding: 5px 5px 5px 5px;
            border-top-left-radius: 0px;
            border-bottom-right-radius: 0px;
            border-top-right-radius: 0px;
            border-bottom-left-radius: 0px;
            border-width: 0px;
            text-align: center;
            }
            QPushButton:hover
            {
                background-color:rgb(28, 26, 26);
            }
            """
menu_frame_stylesheet = """
QFrame {
    background-color: rgb(33, 37, 43); /* Set the background color */
    border: 1px rgb(33, 37, 43); /* Optional: Add a border */
    border-radius: 5px; /* Optional: Add rounded corners */
}
"""

side_menu_button_stylesheet ="""
QPushButton {	
	background-position: left center;
    background-repeat: no-repeat;
	border: 1px;
	border-left: 2px solid transparent;
	background-color: transparent;
	text-align: left;
	padding: 4px 8px 4px 8px;
}
QPushButton:hover {
    background-color: #2c3e50; /* Dark hover background color */
    color: #ffffff; /* Hover text color */
}"""

import os

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QStackedWidget, QFrame, QGraphicsDropShadowEffect, QSizeGrip
)

from PySide6.QtCore import Qt,QPropertyAnimation,QEasingCurve,QRect,QSize
from PySide6.QtGui import QPainter, QBrush, QColor, QPixmap,QPainterPath


#  Segoe Fluent Icons 
class window(QMainWindow):
    control_button_size = QSize(40,32)
    logo_size = QSize(24,24)
    pane_width = 250
    titlebar_height = 42

    def __init__(self, app_title='APPLICATION TITLE',style_sheet=None,titlebar_background:str='TRANSPARENT',title_logo_path=None):
        
        super().__init__()

        #self.setStyleSheet('background-color: #2d2d2d;')
        if style_sheet: self.setStyleSheet(style_sheet)

        # Load the QSS file
        # Navigation history
        self.history = []
        self.current_index = -1
        self.app_title = app_title
        self.first_show = True  # Track if the window is opening for the first time
        #self.first_show_animation_type = 'fade-in'
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint| Qt.WindowType.Window)
        # Enable transparency
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)  # Enable translucent background
        self.setWindowOpacity(0.75)  # Set opacity (0.0 = fully transparent, 1.0 = fully opaque)

        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Calculate the window dimensions based on the golden ratio
        window_width = int(screen_width * 1.618*0.5)
        window_height = int(screen_height *1.618* 0.5)
        self.resize(window_width, window_height)
        # Center the window on the screen
        self.setGeometry((screen_width - window_width) // 2, (screen_height - window_height) // 2, window_width, window_height ) 
        # Main widget and layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QGridLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0,0)
        self.main_layout.setSpacing(0)
        # Apply drop shadow effect to the main widget
        #shadow_effect = QGraphicsDropShadowEffect(self)
        #shadow_effect.setBlurRadius(20)
        #shadow_effect.setColor(QColor(0, 0, 0, 160))
        #shadow_effect.setOffset(0, 0)
        #self.main_widget.setGraphicsEffect(shadow_effect)

        # Custom title bar
        self.titlebar = self.create_titlebar(app_title, title_logo_path,background_color=titlebar_background)
        self.main_layout.addWidget(self.titlebar, 0, 0, 1, 3)

        # Left pane
        self.left_panel = QFrame(self)
        #self.left_panel .setStyleSheet(menu_frame_stylesheet)
        self.left_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_panel.setFixedWidth(self.pane_width)
        self.left_panel_layout = QVBoxLayout(self.left_panel)
        self.left_panel_layout.setContentsMargins(0,0, 0,0)
        self.left_panel_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        #Init Settings menu
        self.settings_panel = QFrame(self)
        #self.settings_panel.setStyleSheet(menu_frame_stylesheet) 

        self.settings_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.settings_panel.setFixedWidth(self.pane_width)
        self.settings_panel_layout = QVBoxLayout(self.settings_panel)
        self.settings_panel_layout.setContentsMargins(5, 5, 5, 5)
        self.settings_panel_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        #self.settings_panel_layout.addStretch()
        # Add some example settings
        #self.settings_panel_layout.addWidget(QLabel("Settings Menu", self))
        #self.settings_panel_layout.addWidget(QPushButton("Option 1", self))
        #self.settings_panel_layout.addWidget(QPushButton("Option 2", self))


        self.settings_panel.hide()
        self.main_layout.addWidget(self.settings_panel, 1, 2)

        # Toggle button for left menu
        self.toggle_button = QPushButton("\uE700", self)
        self.toggle_button.setFixedSize(30, 30)
        self.toggle_button.setStyleSheet(mx_button_stylesheet)
        self.toggle_button.clicked.connect(self.toggle_left_panel)
        self.left_panel_layout.addWidget(self.toggle_button)
        
        self.main_layout.addWidget(self.left_panel, 1, 0, 2, 1)

        # Stacked widget for pages
        self.stacked_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.stacked_widget, 1, 1)

        
        # Add QSizeGrip to corners and edges
        self.size_grips = []
        self.add_size_grip(2, 2, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)  # Bottom-right corner
        self.add_size_grip(2, 0, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)   # Bottom-left corner
        self.add_size_grip(0, 2, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)     # Top-right corner
        self.add_size_grip(0, 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)      # Top-left corner

        # Enable window resizing from sides
        self.setMouseTracking(True)
        self.resizing = False
        self.resize_direction = None

        self.is_maximized = False  # Track the current state of the window
        self.original_geometry = self.geometry()  # Store the original geometry
        self.animation = QPropertyAnimation(self, b"geometry")  # Single animation object
        self.animation.setEasingCurve(QEasingCurve.OutQuad)  # Smooth easing curve
        self.animation.setDuration(175)  # 300ms duration for smoothness

    def create_titlebar(self,title_text,title_logo,background_color:str="#0F161D"):

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        #layout.setSpacing(5)

        # Logo icon
        self.logo_label = QLabel()
        self.logo_label.setStyleSheet('border-radius:0px;padding: 0px;background-color:transparent; margin:8px 0px 4px 8px;')
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setAlignment(self.logo_label,Qt.AlignmentFlag.AlignTop)
        
        layout.addWidget(self.logo_label)        
        
        if os.path.exists(title_logo):
            
            pixmap = QPixmap(title_logo).scaled(self.logo_size,
                                                Qt.AspectRatioMode.KeepAspectRatio,
                                                Qt.TransformationMode.SmoothTransformation)
            self.logo_label.setPixmap(pixmap)

        # Navigation buttons
        self.back_button = QPushButton("\uE72B", self)
        self.back_button.setFixedSize(self.control_button_size.width(), self.control_button_size.height())
    
        self.back_button.setToolTip('Navigation back')
        self.back_button.setStyleSheet(mx_button_stylesheet)
        self.back_button.clicked.connect(self.navigate_back)
        layout.addWidget(self.back_button)
        layout.setAlignment(self.back_button,Qt.AlignmentFlag.AlignTop)
        
        self.forward_button = QPushButton("\uE72A", self)
        self.forward_button.setFixedSize(self.control_button_size)#.width(), self.control_button_size.height())
        self.forward_button.setStyleSheet(mx_button_stylesheet)
        self.forward_button.clicked.connect(self.navigate_forward)
        layout.addWidget(self.forward_button)
        layout.setAlignment(self.forward_button,Qt.AlignmentFlag.AlignTop)
        # Title label
        self.title_label = QLabel("Custom Window", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setContentsMargins(0, 4, 0, 0) 
        self.title_label.setText(title_text)
        layout.addWidget(self.title_label)
        layout.setAlignment(self.title_label,Qt.AlignmentFlag.AlignTop)
        # Spacer to push buttons to the right
        layout.addStretch()

        # Settings button
        self.settings_button = QPushButton("\uE713", self)
        self.settings_button.setFixedSize(self.control_button_size.width(), self.control_button_size.height())
        self.settings_button.setToolTip('Setting')
        self.settings_button.setStyleSheet(mx_button_stylesheet)
        self.settings_button.clicked.connect(self.toggle_settings_panel)
        layout.addWidget(self.settings_button)
        layout.setAlignment(self.settings_button,Qt.AlignmentFlag.AlignTop)
        # Minimize button
        self.minimize_button = QPushButton("\uE738", self)
        self.minimize_button.setFixedSize(self.control_button_size.width(), self.control_button_size.height())
        self.minimize_button.setStyleSheet(mx_button_stylesheet)
        self.minimize_button.clicked.connect(self.showMinimized)
        layout.addWidget(self.minimize_button)
        layout.setAlignment(self.minimize_button,Qt.AlignmentFlag.AlignTop)

        # Maximize/Restore button
        self.maximize_button = QPushButton("\uE15B", self)
        self.maximize_button.setFixedSize(self.control_button_size)#.w, self.h)
        self.maximize_button.setStyleSheet(mx_button_stylesheet)
        self.maximize_button.clicked.connect(self.toggle_maximize_restore)
        layout.addWidget(self.maximize_button)
        layout.setAlignment(self.maximize_button,Qt.AlignmentFlag.AlignTop)
        # Close button
        self.close_button = QPushButton("\uE711", self)
        self.close_button.setFixedSize(self.control_button_size)#.w, self.h)
        self.close_button.setStyleSheet(close_button_stylesheet)
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)
        layout.setAlignment(self.close_button,Qt.AlignmentFlag.AlignTop)

        titlebar = QWidget()
        titlebar.setStyleSheet(f'''background-color:{background_color};border-top-left-radius:8px;border-top-right-radius:8px;
                                  border-bottom-left-radius:0px;border-bottom-right-radius:0px;margin:0px;''')
        titlebar.setFixedHeight(self.titlebar_height)
        titlebar.setLayout(layout)

        return titlebar
    
    def update_navigation_buttons(self, can_go_back, can_go_forward):
        
        self.back_button.setVisible(can_go_back)
        self.forward_button.setVisible(can_go_forward)
        #self.back_button.setEnabled(can_go_back)
        #self.forward_button.setEnabled(can_go_forward)

    def set_app_title(self, title=None,logo_path='MyJobAssistant/resources/icons/logo-coffe2.png'):
        
        self.title_label.setText(title)

        if os.path.exists(logo_path):
            icon_path = logo_path
            pixmap = QPixmap(icon_path).scaled(self.w, self.h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.logo_label.setPixmap(pixmap)


    def add_setting_menu_item(self,item:QWidget):
        # Update the left menu button to show the PostgreSQL connection form
        #menu_item3 = QPushButton("Connect to PostgreSQL")
        #self.menu_item3.setStyleSheet(side_menu_button_stylesheet)
        #item.setStyleSheet(side_menu_button_stylesheet)
        #self.menu_item3.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        #self.menu_item3.clicked.connect(self.add_postgresql_connection_form)
        self.settings_panel_layout.addWidget(item)
        

    def add_left_panel_item(self,item:QWidget):
        # Update the left menu button to show the PostgreSQL connection form
        #menu_item3 = QPushButton("Connect to PostgreSQL")
        #self.menu_item3.setStyleSheet(side_menu_button_stylesheet)
        #item.setStyleSheet(side_menu_button_stylesheet)
        #self.menu_item3.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        #self.menu_item3.clicked.connect(self.add_postgresql_connection_form)
        self.left_panel_layout.addWidget(item)


    def toggle_maximize_restore(self):
        if self.is_maximized:
            self.animate_restore()
        else:
            self.animate_maximize()
        self.is_maximized = not self.is_maximized

    def animate_maximize(self):
        # Stop any ongoing animation
        if self.animation.state() == QPropertyAnimation.Running:
            self.animation.stop()

        # Store the original geometry before maximizing
        self.original_geometry = self.geometry()

        # Get the available screen geometry (excluding taskbar)
        screen_geometry = QApplication.primaryScreen().availableGeometry()

        # Set up the animation to expand to full screen
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(screen_geometry)

        # Start the animation
        self.animation.start()

    def animate_restore(self):
        # Stop any ongoing animation
        if self.animation.state() == QPropertyAnimation.Running:
            self.animation.stop()

        # Set up the animation to shrink to the original size
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.original_geometry)

        # Start the animation
        self.animation.start()

    def showEvent(self, event):
        # Animate the window only when it's shown for the first time
        if self.first_show:
            self.first_show = False
            self.animate_fadeIn()

        super().showEvent(event)
    
    # fade-in effect animation
    def animate_fadeIn(self):
        # Animation for opacity (fade-in effect)
        self.opacity_effect = self.graphicsEffect()
        if not self.opacity_effect:
            self.opacity_effect = self.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_animation.setDuration(500)  # 500ms duration
        self.opacity_animation.setStartValue(0.0)  # Start fully transparent
        self.opacity_animation.setEndValue(1.0)  # End fully opaque
        self.opacity_animation.setEasingCurve(QEasingCurve.OutQuad)

        # Animation for geometry (slide-in effect from the top)
        start_rect = QRect(self.x(), self.y() - 50, self.width(), self.height())  # Start 50px above
        end_rect = self.geometry()  # End at the original position
        self.geometry_animation = QPropertyAnimation(self, b"geometry")
        self.geometry_animation.setDuration(500)  # 500ms duration
        self.geometry_animation.setStartValue(start_rect)
        self.geometry_animation.setEndValue(end_rect)
        self.geometry_animation.setEasingCurve(QEasingCurve.OutQuad)

        # Start both animations
        self.opacity_animation.start()
        self.geometry_animation.start()

    def add_size_grip(self, row, col, alignment):
        size_grip = QSizeGrip(self)
        size_grip.setFixedSize(10, 10)
        size_grip.setStyleSheet("QSizeGrip { background: none; border: none; }")
        self.size_grips.append(size_grip)
        self.main_layout.addWidget(size_grip, row, col, alignment=alignment)
    
    #def paintEvent(self, event):
    #    painter = QPainter(self)
    #    painter.setRenderHint(QPainter.Antialiasing)
    #    painter.setBrush(QBrush(QColor(255, 255, 255)))
    #    painter.setPen(Qt.NoPen)
    #    painter.drawRoundedRect(self.rect(), 10, 10)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 8, 8)  # Adjust the radius as needed
        painter.fillPath(path, QBrush(QColor(255, 255, 255)))
    

    def toggle_left_panel(self):
        if self.left_panel.width() == 200:
            self.left_panel.setFixedWidth(50)  # Minimized width with icons visible
        else:
            self.left_panel.setFixedWidth(200)


    def toggle_settings_panel(self):
        if self.settings_panel.isVisible():
            self.settings_panel.hide()
        else:
            self.settings_panel.show()

    def add_page(self, page_widget):

        self.stacked_widget.addWidget(page_widget)

        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]

        self.history.append(page_widget)
        self.current_index += 1

        self.stacked_widget.setCurrentWidget(self.history[self.current_index])

    def switch_to_widget(self, widget):
        self.stacked_widget.setCurrentWidget(widget)

    def navigate_back(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.stacked_widget.setCurrentWidget(self.history[self.current_index])

    def navigate_forward(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            self.stacked_widget.setCurrentWidget(self.history[self.current_index])

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
            if self.is_on_edge(event.position().toPoint()):  # Updated line
                self.resizing = True

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.resizing:
                self.resize_window(event)
            else:
                self.move(event.globalPosition().toPoint() - self.drag_start_position)
            event.accept()
        else:
            self.set_cursor_shape(event.position().toPoint())  # Updated line
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.resizing = False
        self.setCursor(Qt.ArrowCursor)

    def resizeEvent(self, event):
        self.update()
        super().resizeEvent(event)

    def is_on_edge(self, pos):
        edge_distance = 10
        rect = self.rect()
        on_edge = False
        if pos.x() < edge_distance:
            self.resize_direction = 'left'
            on_edge = True
        elif pos.x() > rect.width() - edge_distance:
            self.resize_direction = 'right'
            on_edge = True
        elif pos.y() < edge_distance:
            self.resize_direction = 'top'
            on_edge = True
        elif pos.y() > rect.height() - edge_distance:
            self.resize_direction = 'bottom'
            on_edge = True
        return on_edge

    def set_cursor_shape(self, pos):
        if self.is_on_edge(pos):
            if self.resize_direction == 'left':
                self.setCursor(Qt.SizeHorCursor)
            elif self.resize_direction == 'right':
                self.setCursor(Qt.SizeHorCursor)
            elif self.resize_direction == 'top':
                self.setCursor(Qt.SizeVerCursor)
            elif self.resize_direction == 'bottom':
                self.setCursor(Qt.SizeVerCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

    def resize_window(self, event):
        rect = self.geometry()
        if self.resize_direction == 'left':
            new_width = rect.width() - (event.globalPosition().x() - rect.left())
            if new_width > self.minimumWidth():
                rect.setLeft(event.globalPosition().x())
        elif self.resize_direction == 'right':
            new_width = event.globalPosition().x() - rect.left()
            if new_width > self.minimumWidth():
                rect.setWidth(new_width)
        elif self.resize_direction == 'top':
            new_height = rect.height() - (event.globalPosition().y() - rect.top())
            if new_height > self.minimumHeight():
                rect.setTop(event.globalPosition().y())
        elif self.resize_direction == 'bottom':
            new_height = event.globalPosition().y() - rect.top()
            if new_height > self.minimumHeight():
                rect.setHeight(new_height)
        self.setGeometry(rect)

    def apply_style(self,style_sheet): self.setStyleSheet(style_sheet)


    def load_style(self,file_name ='default'):
    
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        else:
            print(f"❌     Stylesheet not found: {file_name}")
            return ""




"""
class CustomTitleBar(QWidget):
    w = 40
    h = 32
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.parent = parent
        self.is_maximized = False
        self.setup_ui()

    def setup_ui(self):

        self.setStyleSheet('background-color:red;border:2px')

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 0, 0, 5)
        #layout.setSpacing(5)

        # Logo icon
        self.logo_label = QLabel(self)
        self.logo_label.setStyleSheet('border-radius:0px;padding: 0px; margin:4px 0px 4px 4px;')
        
        layout.addWidget(self.logo_label) 

        # Navigation buttons
        self.back_button = QPushButton("\uE72B", self)
        self.back_button.setFixedSize(self.w, self.h)
    
        self.back_button.setToolTip('Navigation back')
        self.back_button.setStyleSheet(mx_button_stylesheet)
        self.back_button.clicked.connect(self.parent.navigate_back)
        layout.addWidget(self.back_button)

        self.forward_button = QPushButton("\uE72A", self)
        self.forward_button.setFixedSize(self.w, self.h)
        self.forward_button.setStyleSheet(mx_button_stylesheet)
        self.forward_button.clicked.connect(self.parent.navigate_forward)
        layout.addWidget(self.forward_button)
        # Title label
        self.title_label = QLabel("Custom Window", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setContentsMargins(0, 0, 0, 0) 
        layout.addWidget(self.title_label)

        # Spacer to push buttons to the right
        layout.addStretch()

        # Settings button
        self.settings_button = QPushButton("\uE713", self)
        self.settings_button.setFixedSize(self.w, self.h)
        self.settings_button.setToolTip('Setting')
        self.settings_button.setStyleSheet(mx_button_stylesheet)
        self.settings_button.clicked.connect(self.parent.toggle_settings_panel)
        layout.addWidget(self.settings_button)
        layout.setAlignment(self.settings_button,Qt.AlignmentFlag.AlignTop)
        # Minimize button
        self.minimize_button = QPushButton("\uE738", self)
        self.minimize_button.setFixedSize(self.w, self.h)
        self.minimize_button.setStyleSheet(mx_button_stylesheet)
        self.minimize_button.clicked.connect(self.parent.showMinimized)
        layout.addWidget(self.minimize_button)
        layout.setAlignment(self.minimize_button,Qt.AlignmentFlag.AlignTop)

        # Maximize/Restore button
        self.maximize_button = QPushButton("\uE15B", self)
        self.maximize_button.setFixedSize(self.w, self.h)
        self.maximize_button.setStyleSheet(mx_button_stylesheet)
        self.maximize_button.clicked.connect(self.parent.toggle_maximize_restore)
        layout.addWidget(self.maximize_button)
        layout.setAlignment(self.maximize_button,Qt.AlignmentFlag.AlignTop)
        # Close button
        self.close_button = QPushButton("\uE711", self)
        self.close_button.setFixedSize(self.w, self.h)
        self.close_button.setStyleSheet(close_button_stylesheet)
        self.close_button.clicked.connect(self.parent.close)
        layout.addWidget(self.close_button)
        layout.setAlignment(self.close_button,Qt.AlignmentFlag.AlignTop)


    def set_app_title(self, title=None,logo_path='MyJobAssistant/resources/icons/logo-coffe2.png'):
        
        self.title_label.setText(title)

        if os.path.exists(logo_path):
            icon_path = logo_path
            pixmap = QPixmap(icon_path).scaled(self.w, self.h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.logo_label.setPixmap(pixmap)

    def update_navigation_buttons(self, can_go_back, can_go_forward):
        print(can_go_back,can_go_forward)
        self.back_button.setVisible(can_go_back)
        self.forward_button.setVisible(can_go_forward)
        #self.back_button.setEnabled(can_go_back)
        #self.forward_button.setEnabled(can_go_forward)
"""