# ScreenshotTool 📸

A powerful and user-friendly screenshot tool built with Python that runs in the system tray. Capture, save, and manage your screenshots with ease.

![Screenshot Tool](resources/icon.png)

## Features ✨

- **System Tray Integration**: Runs quietly in your system tray
- **Multiple Capture Modes**:
  - Full screen capture
  - Area selection with visual guide
- **Flexible Output Options**:
  - Save to clipboard
  - Auto-save to file
  - Customizable save directory
- **Customizable Hotkeys**
- **Multiple Export Formats**: PNG, JPG
- **User-Friendly Settings Interface**

## Installation 🚀

### Method 1: Run from Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/screenshot-tool.git
cd screenshot-tool
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

### Method 2: Standalone Executable

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
pyinstaller --name="ScreenshotTool" ^
            --hidden-import=pystray._win32 ^
            --hidden-import=PIL ^
            --hidden-import=customtkinter ^
            --add-data "resources;resources" ^
            --add-data "app;app" ^
            --noconsole ^
            --onefile ^
            --icon=resources/icon.ico ^
            main.py
```

3. Find the executable in the `dist` folder

## Dependencies 📦

```
customtkinter
Pillow
pyautogui
keyboard
pystray
```

## Usage 🖥️

1. Launch the application - it will appear in your system tray
2. Default hotkeys:
   - `Ctrl+Shift+C`: Full screen capture
   - `Ctrl+Shift+A`: Area selection
3. Right-click the tray icon to:
   - Access settings
   - Exit application

## Configuration ⚙️

Access settings through the tray icon to customize:
- Hotkeys
- Save directory
- File format
- Auto-save options
- Clipboard behavior

## Project Structure 📁

```
screenshot-tool/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── screenshot.py
│   ├── gui.py
│   └── tray.py
│
├── resources/
│   ├── icon.png
│   └── icon.ico
│
├── main.py
├── requirements.txt
└── README.md
```

## Development 🛠️

To contribute:
1. Fork the repository
2. Create your feature branch
3. Implement your changes
4. Submit a pull request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments 🙏

- Built with [Python](https://www.python.org/)
- UI components from [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- System tray functionality using [pystray](https://github.com/moses-palmer/pystray)

---

**Note**: Remember to create an icon.ico file from your icon.png before building the executable.

## Issues and Support 💡

If you encounter any issues or have suggestions:
1. Check the existing issues
2. Create a new issue with detailed information
3. Join the discussion

---

Made with ❤️ by Coma

Feel free to star ⭐ this repository if you find it helpful!
