# Advanced Keylogger with Clipboard Monitoring
This Python script implements an advanced keylogger that captures keyboard inputs, mouse clicks, and clipboard changes. It is designed to work across different operating systems, including Windows and Linux, and logs the captured data into a text file for later analysis.

# Key Features:
## Cross-Platform Compatibility:
The script detects the operating system (Windows, Linux, or macOS) and adjusts its functionality accordingly, particularly for retrieving the active window title and keyboard layout.
## Active Window Detection:
The get_active_window() function retrieves the title of the currently active window, allowing the keylogger to log which application the user is interacting with at any given time.
## Keyboard Layout Detection:
The get_keyboard_layout() function identifies the current keyboard layout, which is useful for understanding the context of the logged keystrokes.
## Key Logging:
The on_press() function captures each key press, logging the timestamp, active window title, the key pressed, and the keyboard layout to a specified log file (advanced_key_log.txt).
Special keys (like Shift, Ctrl, etc.) are also logged appropriately.
## Mouse Click Logging:
The on_click() function logs mouse click events, including the coordinates of the click and the button pressed, along with the active window title and timestamp.
## Clipboard Monitoring:
The monitor_clipboard() function continuously monitors the clipboard for changes. When new content is detected, it logs the new clipboard content along with the active window title and timestamp.
## Threading:
Clipboard monitoring runs in a separate thread, allowing it to operate concurrently with the keyboard and mouse listeners without blocking their execution.
## Graceful Exit:
The keylogger can be stopped by pressing the Escape key, which triggers the on_release() function to exit the listener.
# Usage:
To run the script, ensure you have the required libraries installed (pynput, pygetwindow, pyperclip, and psutil).
Execute the script in a Python environment. It will start logging keyboard and mouse events, as well as clipboard changes, to the specified log file.
# Important Note:
This script is intended for educational purposes only. Unauthorized use of keyloggers can violate privacy and legal regulations. Always ensure you have permission to monitor any system or user activity.
