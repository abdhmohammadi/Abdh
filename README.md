# Teacher Assistant

A modern, user-friendly teacher assistance application built with PySide6 (Qt for Python).
This application helps educational resources managment and student information with a beautiful, customizable interface.
This project is currently in its early stages...

[🔍 Version history](https://htmlpreview.github.io/?https://github.com/abdhmohammadi/Abdh/blob/main/version-history.html)

## Features

- 🎨 **Customizable UI**
  - Multiple theme support
  - Customizable fonts
  - RTL/LTR layout support
  - Modern, clean interface

- 📚 **Educational Resource Management**
  - View and manage educational resources
  - Resource editor for creating and modifying content
  - Support PDF, Image, HTML and LaTeX in resource editor
  - Organized educational contents 
  - Producing tests in two formats: classroom quizzes and formal exams
  - Ability to distribute tests in PDF and HTML format
  - Snipping tool to import image resources

- 👥 **Student Management**
  - Student list management
  - Personal information tracking
  - Easy navigation between student records
  - Tracking student's behavioral events in order to achieve educational 

- 🌐 **Multilingual Support** (in progress)
  - English and Persian language support
  - RTL/LTR text direction handling
  - Localized interface elements

- ⚙️ **Customizable Settings** 
  - Font selection
  - Theme customization
  - Layout direction preferences
  - LaTeX document settings (in progress)

- ## Next phase of the project
  - Organizing student groups
  - Assigning tests to students in groups and individually
  - Getting answers back from students in image and PDF format for assigned tests


## Building Executable

To create a standalone executable:

```bash
pyinstaller pyinstaller/spec/TeacherAssistant.spec
```

For Windows installer creation, use InnoSetup with the provided script.

## Project Structure
  
```
abdh/
├── TeacherAssistant/  # Main application folder
│   ├── __init__.py
│   ├── main.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── database_tools.py
│   │   ├── font_tools.py
│   │   ├── helpers.py
│   │   ├── image_tools.py
│   │   └── ThemeManager.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── # all data layer models come here
│   ├── view_models/
│   │   ├── __init__.py
│   │   └── # View Models(Intermediary between View and Model)
│   ├── views/
│   │   ├── __init__.py
│   │   └──  # Views (UI Layer)
│   └── resources/
│       ├── fonts/
│       │     ├── SegoeIcons.py
│       │     └── SegoeIcons.ttf
│       ├── icons/
│       │     ├── book-coffe.png (application icon)
│       │     ├── logo-coffe1.png
│       │     └── logo-coffe2.png
│       ├── images/
│       │     └── background.png
│       ├── styles/
│       │     ├── chrome-semi-dark/
│       │     │       ├── global.qss
│       │     │       └── classes.qss
│       │     └── light/
│       │             ├── global.qss
│       │             └── classes.qss
│       └── templates/
│             ├── 01-Quiz-config.json
│             ├── 01-Quiz-Template.html
│             ├── 02-Formal-Exam-config.json
│             └── 02-Formal-Exam-Template.html
├── PySideAbdhUI/   # Customized GUI
│   ├── __init__.py
│   ├── popup.py
│   ├── style_sheets.py
│   ├── TableWidget.py
│   ├── Window.py
│   └── styles/
│       ├── default-dark.qss
│       └── default-light.qss
├── pyinstaller/                                  # PyInstaller
│   ├── build/
│   ├── dist/
│   └── spec/
│       └── TeacherAssistant.spec
├── requirements.txt
└── README.md

```

## Dependencies

- PySide6
- PostgreSQL (for database)
- Other dependencies listed in requirements.txt

## Configuration

The application stores settings in the user's LOCALAPPDATA directory:
- `%LOCALAPPDATA%/MyJobAssistant/settings.json`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Abdullah Mohammadi
- GitHub: [abdhmohammadi](https://github.com/abdhmohammadi)

## Acknowledgments

- Built with PySide6 (Qt for Python)
- Uses PostgreSQL database
- Uses custom UI components from PySideAbdhUI
- Icons and resources are custom-designed
