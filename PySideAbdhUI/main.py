
import sys
import os
PACKAGE_NAME = 'PySideAbdhUI'
PACKAGE_VERSION = 1.0
# Get the path of the running executable
if getattr(sys, 'frozen', False):
    # If the application is run as a bundled executable (e.g., PyInstaller)
    application_path = os.path.dirname(sys.executable)
else:
    # If the application is run as a script
    application_path = os.path.dirname(os.path.abspath(__file__))


icon_path = application_path + "/resources/icons/logo-book-coffe.png"
default_style_path = application_path + "/resources/styles/blue.qss"

# To prevent from write permission we save settings.json in the LOCALAPPDATA directory
# Get the AppData directory
appdata_dir = os.getenv('LOCALAPPDATA')
app_dir = os.path.join(appdata_dir, PACKAGE_NAME)
# Create the directory if it doesn't exist
os.makedirs(app_dir, exist_ok=True)
# Path to the settings file
settings_path = os.path.join(app_dir, 'settings.json')

# Our customized UI modules is imported from PySidePyQtUI
# PySidePyQtUI is placed in abdh/PySidePyQtUI/ directory
# This lines ensures our custom modules can be imported from 'PySideQtUI' 
sys.path.append(os.path.dirname(application_path))
from Abdh import Json
from PySideAbdhUI import Window
from PySideAbdhUI import style_manager as st
# Local moduls in main.py directory must be imported
#from MyJobAssistant.views import forms
#from MyJobAssistant.utils import Json
#from MyJobAssistant.utils import style_manager as sm

# PySide6 moduls
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication,QPushButton,QFileDialog,QLabel
from PySide6.QtCore import Qt
accent_color = 'blue'
titlebar_background = 'TRANSPARENT'
# Opens settings.json
settings_manager = Json.JSONManager(settings_path)
class PySideAbdhUIApp:

    def __init__(self):

        self.connection = None

        self.app = QApplication(sys.argv)
        # lookup for a key named 'style sheet' in the settings.json
        # this key stores the path of qss file as custom theme file. 
        # settings.json is avilable in LOCALAPPDATA directory
        style_path = settings_manager.find_value('style sheet')
        # If we could not find style path throw settings.json, we try read 
        # styles from application_path + "/resources/styles/blue.qss"
        style_path = default_style_path if style_path is None else style_path
        # Using QtStyleSheetManager to manage custom styles
        # QtStyleSheetManager has defined in MyJobAssistant/utils/style_manager.py
        style_manager = st.QtStyleSheetManager(style_path)                            
        style_manager.load_stylesheet()
        check, value = style_manager.check_accent_color_placeholder()
                    
        if check: style_manager.replace_placeholder(value)
        
        # Our custom ICON is available in application_path + "/resources/icons/
        self.app.setWindowIcon(QIcon(icon_path))
        # Create the main customized UI window
        self.window = Window.window(app_title= 'PySideAbdhtUI | Customized UI for python application',
                                    title_logo_path= icon_path,
                                    titlebar_background=titlebar_background)
        self.window.load_style(style_path)
        
        self.create_left_pane()

        self.create_settings_pane()
        
        label = QLabel('This is HOME page\n YOU CAN LOAD YOUR PAGES HERE')
        label.setStyleSheet('font-size:24pt;text-align:center;font-weight:bold;color: YELLOW')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.window.add_page(label)

    def load_page1(self):
        label = QLabel('This is FIRST page\n USE NAVIGATION BUTTONS ON TITLEBAR')
        label.setStyleSheet('font-size:24pt;text-align:center;font-weight:bold;color:green')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.window.add_page(label)

    def load_page2(self):
        label = QLabel('This is SECOND page\n USE NAVIGATION BUTTONS ON TITLEBAR')
        label.setStyleSheet('font-size:24pt;text-align:center;font-weight:bold; color:lightgreen')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.window.add_page(label)

    def apply_style(self):
            dialog = QFileDialog(self.window,directory= application_path + '/resources/styles')
            dialog.setFileMode(QFileDialog.ExistingFiles)
            dialog.setNameFilter("style sheet files(*.qss)")
        
            if dialog.exec():
                fileName = dialog.selectedFiles()
                
                if fileName:                    
                    self.window.load_style(file_name=fileName[0])
                    setting = {"style sheet": fileName[0]}
                    settings_manager.write(setting)

    def create_left_pane(self):
        # Init left pane

        left_item = QPushButton('Page 1')
        left_item.clicked.connect(lambda:self.load_page1())
        
        left_item.setStyleSheet(st.menu_button_style)
        self.window.add_left_panel_item(left_item)

        left_item = QPushButton('Page 2')
        left_item.clicked.connect(lambda:self.load_page2())
        
        left_item.setStyleSheet(st.menu_button_style)
        self.window.add_left_panel_item(left_item)

    def create_settings_pane(self):
                
        setting = QLabel('SETTINGS')
        setting.setStyleSheet("font-size: 14px;font-weight:bold;margin:10px 0px 0px 10px")
        self.window.add_setting_menu_item(setting)

        ### Init settings menu

        btn = QPushButton(text='CHANGE STYLE')
        self.window.add_setting_menu_item(btn)
        btn.clicked.connect(self.apply_style)
        btn.setStyleSheet(st.menu_button_style)

        btn = QPushButton(text='CUSTOM COMMAND 1')
        self.window.add_setting_menu_item(btn)
        #btn.clicked.connect(self.open_document)
        btn.setStyleSheet(st.menu_button_style)
        
        btn = QPushButton(text='CUSTOM COMMAND 2')
        self.window.add_setting_menu_item(btn)
        #btn.clicked.connect(self.open_document)
        btn.setStyleSheet(st.menu_button_style)

        github = QLabel('https://github.com/abdhmohammadi/')
        self.window.add_setting_menu_item(github)
        github.setStyleSheet("font-size: 10pt;margin:10px 0px 0px 0px")          

    def run(self):

        self.window.show()

        sys.exit(self.app.exec())

        if self.connection:
            self.connection.cursor().close()
            self.connection.close()


if __name__ == "__main__":

    app = PySideAbdhUIApp()
    app.run()
