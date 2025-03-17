# TeacherAssistant/__init__.py
# Package initialization for TeacherAssistant

# Optional: Import key modules for easier access
import enum
from PySide6.QtGui import QFont
import psycopg2.extensions 

# Optional: Define __all__ to control what gets imported with `from TeacherAssistant import *`
__all__ = ['TeacherAssistant']

__version__ = "0.1.0-pre-alpha" 
application_path = ''
icon_font :QFont = None
EDU_CONTENT_WIDTH = 6.19 # inches
DPI = 90
db_connection:psycopg2.extensions.connection = None 
Language = 'Persian'

class DocumentType(enum.Flag):

    PlainText = ...  # 0x0 
    RTF       = ...  # 0x1
    LaTeX     = ...  # 0x2
    Html      = ...  # 0x3
    Image     = ...  # 0x4

ToolTips = {
    'Language':'Currently this feature is not used much,\n it will be used in future updates.',
    'StyleSheet':'There are a number of custom styles can be applied to the UI.\nChanging it will affects all UI objects of the application.',
    'Direction':'Page direction options: It is provided Left-to-Right and Right-to-Left.\nThe direction is applied on the content of main frame,\nTitlebar, left panel and right panel are not affected currently.',
    'LaTeX Settings':'Will be supported in future updates!'
}
