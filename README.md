# Teacher Assistant project
# PySydeAbdhUI

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
