"""Screenshot logic, kept separate from the GUI so it is easy to test."""

import time

import pyautogui


def capture_screenshot(output_file: str, delay: float = 0) -> str:
    """Wait `delay` seconds, capture the full screen and save it.

    Returns the path the screenshot was saved to.
    """
    if delay > 0:
        time.sleep(delay)

    screenshot = pyautogui.screenshot()
    screenshot.save(output_file)
    return output_file
