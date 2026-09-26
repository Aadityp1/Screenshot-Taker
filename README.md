# 📸 Screenshot Taker

A simple desktop app built with Python, Tkinter and PyAutoGUI. Click one
button, the window hides itself, and a full-screen screenshot is saved as
`screenshot.png`.

## Features
- Clean, fixed-size Tkinter window
- Hides itself before capturing so it does not appear in the shot
- 2-second delay so you can arrange your screen
- Success / error message boxes

## Project Structure
```
screenshot_taker/
├── main.py                 # Entry point
├── gui.py                  # Tkinter interface (ScreenshotApp)
├── screenshot_service.py   # Screenshot capture logic
├── config.py               # Titles, fonts, delay, output file
├── requirements.txt        # Python dependencies
├── statement.md            # Problem statement
├── README.md               # This file
├── diagrams/               # Diagram placeholders
│   ├── flowchart.md
│   ├── architecture.md
│   └── use_case.md
└── screenshots/            # Place UI screenshots for your report here
```

## Requirements
- Python 3.8+
- Tkinter (bundled with Python; on Linux: `sudo apt install python3-tk`)
- Packages in `requirements.txt`

## Installation
```bash
# (optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Usage
```bash
python main.py
```
Click **Take Screenshot**. The image is saved as `screenshot.png` in the
folder you ran the command from.

## Configuration
Edit `config.py` to change the delay, output file name, window size or fonts.

## Platform Notes
- **Linux:** install `scrot` (`sudo apt install scrot`) and `python3-tk`.
  Wayland sessions may block screen capture; use an X11 session.
- **macOS:** grant Screen Recording permission to your terminal/IDE in
  System Settings → Privacy & Security.
- **Windows:** works out of the box.

## How It Works
1. User clicks the button.
2. The window is hidden.
3. The app waits 2 seconds.
4. PyAutoGUI captures the screen and saves the file.
5. The window is shown again and a success message appears.

See the `diagrams/` folder for the flowchart and architecture.
