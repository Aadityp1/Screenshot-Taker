"""Tkinter user interface for the Screenshot Taker app."""

from tkinter import Button, Frame, Label, messagebox

import config
from screenshot_service import capture_screenshot


class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self._setup_window()
        self._build_widgets()

    def _setup_window(self):
        self.root.title(config.APP_TITLE)
        self.root.geometry(config.WINDOW_SIZE)
        self.root.resizable(False, False)

    def _build_widgets(self):
        frame = Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        title = Label(frame, text=config.APP_TITLE, font=config.TITLE_FONT)
        title.pack(pady=10)

        btn = Button(
            frame,
            text="📸 Take Screenshot",
            font=config.BUTTON_FONT,
            width=20,
            height=2,
            command=self.take_screenshot,
        )
        btn.pack(pady=20)

    def take_screenshot(self):
        self.root.withdraw()   # Window hide
        self.root.update()

        try:
            capture_screenshot(config.OUTPUT_FILE, config.DELAY_SECONDS)
        except Exception as exc:
            self.root.deiconify()
            messagebox.showerror("Error", f"Could not take screenshot:\n{exc}")
            return

        self.root.deiconify()  # Window show
        messagebox.showinfo(
            "Success", f"Screenshot saved as {config.OUTPUT_FILE}"
        )
