# Run this command to create pyInstaller exe
#  C:\Users\AbdhM\AppData\Roaming\Python\Python313\Scripts\pyinstaller  pyinstaller/spec/TeacherAssistant.spec
# Use InnoSetup tool to create windows installer

import shutil
import sys
import os

# Get the path of the running executable
# If exe is located in C:\Program Files\Abdh\TeacherAssistant\TeacherAssistant.exe,
# the output will be the running executable or script is located in: C:\Program Files\Abdh\TeacherAssistant\
if getattr(sys, 'frozen', False):
    # If the application is run as a bundled executable (e.g., PyInstaller)
    application_path = os.path.dirname(sys.executable)
else:
    # If the application is run as a script
    application_path = os.path.dirname(os.path.abspath(__file__))


font_SegoeIcons_path =  application_path +'/resources/fonts/SegoeIcons.ttf'

icon_path = application_path + "/resources/icons/book-coffe.png"

default_style_path = application_path + "/resources/styles/blue.qss"

# To prevent from write permission we save settings.json in the LOCALAPPDATA directory
appdata_dir = os.getenv('LOCALAPPDATA')
appdata_dir = os.path.join(appdata_dir, 'Abdh\\TeacherAssistant')
# Create the directory if it doesn't exist
os.makedirs(appdata_dir, exist_ok=True)
# Path to the settings file
settings_path = os.path.join(appdata_dir, 'settings.json')

# Our customized UI modules is imported from PySidePyQtUI
# PySidePyQtUI is placed in abdh/PySidePyQtUI/ directory
# This lines ensures our custom modules can be imported from 'PySideAbdhUI' 
sys.path.append(os.path.dirname(application_path))

from Abdh import Json
from PySideAbdhUI import Window
from PySideAbdhUI.popup import PopupNotifier
from PySideAbdhUI import style_manager as sm
import TeacherAssistant 
from TeacherAssistant import DPI,ToolTips
# Local moduls in main.py directory must be imported
from TeacherAssistant.views import forms, EduResourcesViewer as edu_viewer
from TeacherAssistant.views import EducationalResourceEditor as edu_editor

# PySide6 moduls
from PySide6.QtCore import QSize ,Qt
from PySide6.QtGui import QIcon,QFont,QFontDatabase
from PySide6.QtWidgets import (QApplication,QPushButton,QFileDialog,QLabel,QComboBox,QRadioButton, QHBoxLayout,QWidget)

#accent_color = 'red'
titlebar_background = 'TRANSPARENT'

TeacherAssistant.application_path = application_path
# Opens settings.json
settings_manager = Json.JSONManager(settings_path)

style_manager = sm.QtStyleSheetManager('@accent-color')


def create_font(path,point_size=12):

    font_id = QFontDatabase.addApplicationFont(path)
    if font_id == -1:
        print("Failed to load the font file.")

    # Get the font family name
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

    # Create a QFont object
    return QFont(font_family,point_size)  # Font family and size


def apply_style():
    
    dialog = QFileDialog(window,directory = appdata_dir)
    dialog.setFileMode(QFileDialog.ExistingFiles)
    dialog.setNameFilter("style sheet files(*.qss)")
       
    if dialog.exec():
        fileName = dialog.selectedFiles()
                
        if fileName:
            filename = fileName[0].replace('/','\\')
            print(os.path.dirname(filename) == appdata_dir,os.path.dirname(filename) , appdata_dir)
            if not os.path.dirname(filename) == appdata_dir:
                shutil.copy(filename,appdata_dir)
                filename = os.path.join(appdata_dir,os.path.basename(filename))
            
            style_manager = sm.QtStyleSheetManager()
            style_manager.load_stylesheet(filename)
            #check, value = style_manager.check_accent_color_placeholder()
                    
            #if check:
            #    style_manager.stylesheet = style_manager.replace_placeholder(accent_color)
                    
                    
            app.setStyleSheet(style_manager.stylesheet)

            settings_manager.write({"style sheet":filename})


def on_font_changed(sender:QComboBox):
    # Get the text of the selected item 
    selected_text = sender.itemText(sender.currentIndex())
    
    style_manager.add_property_to_widget('QWidget','font-family',selected_text)
    style_manager.add_property_to_widget('QWidget','font-size',12)
        
    settings_list = [('family',selected_text),('size',12)]
    # Create a dictionary with the list elements as key-value pairs under 'connection'
    settings = {"font": dict(settings_list)}
    settings_manager.write(settings)

    window.setStyleSheet(style_manager.stylesheet)


# Creates a vertical panel on the right edge of the mian window
# This panel is used to settings porpose
def create_settings_pane():

        window.add_right_panel_item(QLabel('Language'))
        combo1 = QComboBox()
        combo1.setPlaceholderText('-- Choose language --')
        combo1.setToolTip(ToolTips['Language'])
        # Currently the language feature is not used in global scope
        # It is used in the future updates  
        combo1.addItems(['English','فارسی']) 
        window.add_right_panel_item(combo1)
        # Changes language in global scope
        combo1.currentIndexChanged.connect(lambda _: setattr(TeacherAssistant, 'Language', 
                                                     combo1.currentText() if combo1.currentText() =='English' else 'Persian'))
        combo1.setCurrentIndex(0)
        
        window.add_right_panel_item(QLabel('Font'))
        # Global Font in the application domain 
        fonts = QFontDatabase.families()
               

        combo2 = QComboBox()
        combo2.setPlaceholderText("Select font")
        combo2.addItems(fonts)
        current_font = settings_manager.find_value('font')
        if current_font:
            combo2.setCurrentText(dict(current_font)['family'])
        else:
            combo2.setCurrentText('Times New Roman')

        window.add_right_panel_item(combo2)
        # Changes the application font, this change affects all objects in the application
        combo2.currentIndexChanged.connect(lambda _,sender=combo2: on_font_changed(sender))

        # Page direction options: It is provided Left-to-Right
        # The direction is applied on the mantent of main frame, and titlebar,
        # left panel and right panel are not affected currently.
        hlayout = QHBoxLayout()
        
        radio1 = QRadioButton('Right to Left')
        radio1.clicked.connect(lambda _, d=Qt.LayoutDirection.RightToLeft: toggle_direction(d))
        hlayout.addWidget(radio1)

        radio2 = QRadioButton('Left to Right')
        radio2.setChecked(True)
        radio2.clicked.connect(lambda _, d= Qt.LayoutDirection.LeftToRight: toggle_direction(d))
        hlayout.addWidget(radio2)
        
        w = QWidget()
        w.setToolTip(ToolTips['Direction'])
        w.setLayout(hlayout)
        window.add_right_panel_item(w)

        # There are a number of custom styles can be applied to the UI.
        # Changing it will affects all UI objects of the application.
        btn = QPushButton(text='CHANGE STYLE')
        window.add_right_panel_item(btn)
        btn.setObjectName('MenuItem')
        btn.setToolTip(ToolTips['StyleSheet'])
        btn.clicked.connect(apply_style)

        setting = QLabel('LATEX SETTINGS')
        setting.setProperty('class','subtitle')
        setting.setToolTip(ToolTips['LaTeX Settings'])
        window.add_right_panel_item(setting)

        github = QLabel('\n https://github.com/abdhmohammadi/')
        window.add_right_panel_item(github)
        github.setProperty('class','hyperlink')          


def create_left_pane():
    # Init left pane
    #menu_button_style = sm.menu_button_style
    #menu_button_style = menu_button_style.replace('@accent-color',accent_color)
 
    left_item = QPushButton('Student list')
    left_item.setObjectName('MenuItem')
    left_item.setIconSize(QSize(24,24))
    left_item.setIcon(QIcon(application_path +'/resources/icons/logo-coffe2.png'))
    left_item.clicked.connect(lambda:load_students_page())
        
    window.add_left_panel_item(left_item)

    left_item = QPushButton('Edu resources')
    left_item.setObjectName('MenuItem')
    left_item.setIconSize(QSize(24,24))
    left_item.setIcon(QIcon(application_path + '/resources/icons/logo-book-coffe.png'))
    left_item.clicked.connect(lambda: load_EduResourcesViewer())
        
    window.add_left_panel_item(left_item)


    left_item = QPushButton('Edu resource Editor')
    left_item.setObjectName('MenuItem')
    left_item.setIconSize(QSize(24,24))
    left_item.setIcon(QIcon(application_path + '/resources/icons/logo-book-coffe.png'))
    left_item.clicked.connect(lambda: load_EduResourceEditor())
        
    window.add_left_panel_item(left_item)
  
def toggle_direction(direction:Qt.LayoutDirection): window.set_direction(direction)

def load_EduResourceEditor(): window.add_page(edu_editor.EducationalResourceEditor())

def load_students_page(): window.add_page(forms.PersonalInfoListViewWidget(parent=window))

def load_EduResourcesViewer():

    # Fetch data from the table
    #cursor = TeacherAssistant.db_connection.cursor()
    
    #cursor.execute("SELECT content_description_	FROM public.educational_resources;")
    
    #data = cursor.fetchall()
    
    viewer = edu_viewer.EduResourcesViewer()
    
    #viewer.load_data()

    window.add_page(viewer)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    TeacherAssistant.icon_font = create_font(font_SegoeIcons_path,12)

    # reads global font from settings.json
    font = settings_manager.find_value('font')
    # checking validation
    if font:
        font_family = font['family']
        size = int(font['size'])
    else:
        font_family = 'Times New Roman'
        size = 12
    # lookup for a key named 'style sheet' in the settings.json
    # this key stores the path of qss file as custom theme file. 
    # settings.json is avilable in LOCALAPPDATA directory
    style_path = settings_manager.find_value('style sheet')
    # If we could not find style path throw settings.json, we try read 
    # styles from application_path + "/resources/styles/blue.qss"
    style_path = default_style_path if style_path is None else style_path
    # Using QtStyleSheetManager to manage custom styles
    # QtStyleSheetManager has defined in TeacherAssistant/utils/self.style_manager.py
    style_manager.load_stylesheet(style_path)
    
    # Update style sheet with font values, then is appled on the application
    style_manager.add_property_to_widget('QWidget','font-family',font_family)
    style_manager.add_property_to_widget('QWidget','font-size',size)
        
    check, value = style_manager.check_accent_color_placeholder()
                    
    if check: style_manager.replace_placeholder(value)
    # Apply stylesheet on the application
    app.setStyleSheet(style_manager.stylesheet)

    connection_settings = settings_manager.find_value('connection')
    
    host = 'localhost' if connection_settings is None else connection_settings["host"]
    port = '5432' if connection_settings is None else connection_settings["port"]
    database = '' if connection_settings is None else connection_settings["database"]
    user = 'postgres' if connection_settings is None else connection_settings["user"]
    password = '' if connection_settings is None else connection_settings["password"]

    # We can load the connection dialog before we create the main window,
        # but if we done it, selected theme is not applyed.
    connection_dialog = forms.PostgreSqlConnectionWidget(host,port,database,user,password)

    status, settings = connection_dialog.show_dialog()

    if not settings or not status:
        exit('Unsuccess connection or user ignored')
    
    # Update settings.json by new connection values
    settings_manager.write(settings)  
    
    # Our custom ICON is available in application_path + "/resources/icons/
    #self.app.setWindowIcon(QIcon(icon_path))
    # Create the main customized UI window
    window = Window.PySideAbdhWindow()

    window.initUI(app_title= 'MY JOB ASSISTANT | ' + TeacherAssistant.__version__,
                  titlebar_background='transparent', 
                  title_logo_path=icon_path, 
                  direction=Qt.LayoutDirection.LeftToRight)
    
    create_left_pane()
    create_settings_pane()
    load_students_page()

    window.show()
    
    PopupNotifier.Notify(window,"Wellcome!", "Job assistant is in your service.", 'bottom-right', delay=5000,
                         background_color='#353030',border_color="#2E7D32")
    
    app.exec()
    
    if TeacherAssistant.db_connection:
        TeacherAssistant.db_connection.cursor().close()
        TeacherAssistant.db_connection.close()

    exit()