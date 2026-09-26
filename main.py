"""Entry point: run `python main.py` to start the Screenshot Taker."""

from tkinter import Tk

from gui import ScreenshotApp


def main():
    root = Tk()
    ScreenshotApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
