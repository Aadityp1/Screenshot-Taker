# Problem Statement

## Title
Screenshot Taker — A Simple Desktop Screenshot Utility

## Problem
Taking a clean screenshot often requires memorising keyboard shortcuts or
installing heavy software. The application window itself can also end up in
the screenshot, which is unwanted.

## Objective
Build a lightweight desktop application that captures the full screen with a
single click, hides its own window during capture, and saves the result to an
image file.

## Scope
- In scope: full-screen capture, delay before capture, saving as PNG,
  user feedback through message boxes.
- Out of scope (possible future work): region selection, custom save
  location, multiple monitors, clipboard copy, hotkeys.

## Functional Requirements
1. Show a window with a title and a "Take Screenshot" button.
2. On click, hide the window and wait 2 seconds.
3. Capture the entire screen and save it as `screenshot.png`.
4. Restore the window and show a success message.
5. Show an error message if capture fails.

## Non-Functional Requirements
- Simple, fixed-size, easy-to-use interface
- Runs on Windows, macOS and Linux
- Modular code (UI, logic and configuration separated)

## Technologies
| Purpose            | Tool        |
|--------------------|-------------|
| Language           | Python 3    |
| GUI                | Tkinter     |
| Screen capture     | PyAutoGUI   |
| Image handling     | Pillow      |

## Expected Output
A `screenshot.png` file containing the full screen at the moment of capture,
without the application window visible.

## Diagrams
See the `diagrams/` folder (flowchart, architecture, use case).
