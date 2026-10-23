import base64, time, os, sys
from tkinter import messagebox
import string
import random
import codecs
import datetime
import subprocess
import ast

try:
    from cryptography.fernet import Fernet
except Exception:
    os.startfile('install.bat')
    time.sleep(10)
    try:
        from cryptography.fernet import Fernet
    except Exception as e:
        print(f"Error: {e}\nRestart programm")
        messagebox.showerror("Obfuscator", "Restart programm")
        sys.exit(0)




key = Fernet.generate_key()
encoded_key = base64.b16encode(key).decode()

cipher = Fernet(key)

var = ""
result = ""

type_char = 1
chars1 = ['O', '0', 'Q']
char = ''

def generate_var(len = 15000):
    global var, type_char, char, new_var
    var = "_LO"
    for i in range(1, len):
        if type_char == 1:
            if i == 1:
                var += random.choice(['L', 'I'])
            else:
                var += random.choice(['L', 'I', '1'])

            type_char = 2


        else:
            char = random.choice(chars1)
            var += char
            type_char = 1
    result = var

    
    var = ""
    type_char = 1
    return result


def obfuscation1(variable1, variable2, variable3, encoded_variable1, encoded_variable2, encoded_variable3):
    global result, code
    result = f"""{variable1}=__import__('{encoded_variable1}');{variable2}=getattr({variable1},'{encoded_variable2}');exec({variable2}('{encoded_variable3}'))"""
    code = "exec("
    for char in result:
        code += "+".join(repr(ch) for ch in char)
    code += ')'
    return code


def obfuscation2(content, variable1, variable2, variable2_encoded, variable1_encoded, variable3, variable4, variable5):
    global result
    #cryptography = __import__('cryptography')
    #fernet = getattr(cryptography, 'fernet')
    #decrypt = getattr(fernet, 'decrypt')
    #c = getattr(fernet, 'Fernet')
    #cipher = c(key)
    #content = ""
    #exec(cipher.decrypt(content))
    

    result = f"""{variable1}=__import__('{variable2_encoded}')
    {variable2}=getattr({variable1}, '{variable1_encoded}')
    {variable3}={variable2}({variable4})
    {variable5}='''{content}'''
    exec({variable3}({variable5}))"""
    code = "exec("
    for char in result:
        code += "+".join(repr(ch) for ch in char)
    code += ')'
    return code

# def obfuscate_file():
#     global obfuscate_result
#     obfuscation_result = obfuscation2(obfuscation_result1, generate_var(), generate_var(), crypt, fern, generate_var(), decr, generate_var())
#     return obfuscation_result1


def decode_content(content: str):
    decoded_bytes = codecs.decode(content, 'unicode_escape')
    return decoded_bytes

def encode_content(content: str):
    return ''.join(f'\\x{b:02x}' for b in content.encode("utf-8"))



def protect_code(obfuscated_file_path: str, obfuscated_content: str):
    if not(os.path.exists(obfuscated_file_path)):
        messagebox.showerror("Obfuscation engine", "File not found")
        return ""

    
    target_dir = os.path.dirname(obfuscated_file_path)
    env_path = os.path.join(target_dir, ".env")
    gitignore_path = os.path.join(target_dir, ".gitignore")
    
    
    file_name = generate_var(17)
    encrypted_path = os.path.join(target_dir, file_name + ".txt")
    
    code = f"""import sys;from cryptography import fernet;from dotenv import load_dotenv;import os, time;os.system('cls');base=getattr(sys, '_MEIPASS', os.getcwd());load_dotenv(os.path.join(base,'.env'));file=os.path.join(base,'{file_name + ".txt"}');_key = os.getenv("key");_cipher = fernet.Fernet(_key);_content=open(file, 'rb').read();_result=_cipher.decrypt(_content);exec(_result);sys.exit(0)""" # Доделать

    result = encode_content(code)

    protected_content = f'''
#   Protected
# time: {datetime.datetime.now()}
exec("{result}")'''
    output = ""
    for char in protected_content:
        output += "+".join(repr(ch) for ch in char)
    output += ')'

    key_env = Fernet.generate_key().decode()

    cipher2 = Fernet(key_env)
    with open(env_path, "w", encoding="utf-8") as env:
        env.write(f"key={key_env}")
    
    with open(gitignore_path, "w", encoding="utf-8") as gitignore:
        gitignore.write(".env\n")



    encrypted = cipher2.encrypt(obfuscated_content.encode("utf-8"))
    with open(encrypted_path, 'w', encoding="utf-8") as protected_file:
        protected_file.write(encrypted.decode("utf-8"))

    print("\rFile protected", end="")
    print()
    return protected_content, encrypted_path, env_path, gitignore_path

def get_imports(not_obfuscated_path=""):
    try:
        with open(not_obfuscated_path, 'r', encoding="utf-8") as f:
            tree = ast.parse(f.read())
    except Exception as e:
        print(f"Can't parse file\nError: {e}")
        return []

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return list(imports)

def _generate_args(add_files, target_script, enable_console, add_modules=[], encrypted_txt_path="", env_path="", not_obfuscated_path=""):
    """Generating args for compiling\nadd_files - add files to exe (dict)\ntarget_script - path to target script (str)\nenable console - show console (bool)\nadd_modules - add modules to exe\nencrypted_txt_path - required for compile file\nenv_path - required to compile file\nnot_obfuscated_file - required to extract import"""
    heavy_libs = {"tkinter", "PIL", "numpy", "pandas"}

    imports = get_imports(not_obfuscated_path)
    all_imports = set(imports + add_modules)


    args = [
                    "python",
                    "-m", "PyInstaller", "--onefile",
                    "--collect-all=cryptography",
                    "--collect-all=dotenv",
                    "--clean",
                    "-i", "NONE",
                    "--name=main"
            ]

    
    for module in all_imports:
        if module in heavy_libs:
            args.append(f"--collect-all={module}")
        else:
            args.append(f"--hidden-import={module}")
        
    args.append(f"--add-data={os.path.normpath(env_path)};.")
    args.append(f"--add-data={os.path.normpath(encrypted_txt_path)};.")

    
    for file in add_files:
        args.append(f'--add-data={file};.')
    if not(enable_console):
        args.append('--noconsole')

    target_dir = os.path.dirname(os.path.normpath(target_script))
    args.append(f"--paths={target_dir}")
    args.append(os.path.normpath(target_script))
    # print(args)
    return args

def protected_compile(path, noconsole=False, add_files=[], add_modules=[], txt_path="", env_path="", not_obfuscated_path="", show_log=True, gitignore_path=""):
    """Compiling obfuscated file\nadd_files - add files to exe (dict)\ntarget_script - path to target script (str)\nenable console - show console (bool)\nadd_modules - add modules to exe\nencrypted_txt_path - required for compile file\nenv_path - required to compile file\nnot_obfuscated_file - required to extract import\nshow_log - show compiling log"""
    try:
        target_dir = os.path.dirname(os.path.normpath(path))
        if show_log:
            proc = subprocess.Popen(
                args=_generate_args(add_files, path, noconsole, add_modules, txt_path, env_path, not_obfuscated_path), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=target_dir, bufsize=1
            )
            for line in proc.stdout:
                print(line, end='')
            proc.wait()
        else:
            r = subprocess.run(
                args=_generate_args(add_files, path, noconsole, add_modules, txt_path, env_path, not_obfuscated_path), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=target_dir
            )
        os.remove(txt_path)
        os.remove(env_path)
        os.remove(gitignore_path)
        
        return True
    
    except Exception as e:
        print(e)
    return False



def main(path: str, compile = False, noconsole = True, add_files = [], add_modules=[], show_log=False, icon="NONE"):
    global er
    if path == "":
        return 0, "File not selected"
    if not(os.path.exists(path)):
        return 0, "File not exists"

    try:
        with open(path, 'r', encoding="utf-8") as file:
            content = file.read()
    except Exception as er:
        print(f"Error: {er}")
        return 0, er


    file_name, file_ext = os.path.splitext(path)
    new_name = file_name + '_obfuscated' + file_ext

    print("\rObfuscating...", end='')
    time.sleep(0.2)

    encoded_content1 = base64.b16encode(content.encode("utf-8")).decode("ascii")

    encrypted_content1 = cipher.encrypt(content.encode("utf-8"))
    encrypted_content2 = cipher.encrypt(encoded_content1.encode("utf-8"))



    var1 = generate_var()
    var2 = generate_var()
    var3 = generate_var()

    crypt = ''.join(f'\\x{b:02x}' for b in b"cryptography")
    fern = ''.join(f'\\x{b:02x}' for b in b"Fernet")
    decr = ''.join(f'\\x{b:02x}' for b in b"decrypt")

    encoded_var1 = ''.join(f'\\x{b:02x}' for b in b"base64")
    encoded_var2 = ''.join(f'\\x{b:02x}' for b in b"b16decode") #base64.b16encode(b"b16decode").decode("utf-8")

    
    

    result1 = obfuscation1(var1, var2, var3, encoded_var1, encoded_var2, encoded_content1)
    obfuscation_result = "exec('" + encode_content(result1) + "')"

    protected, encrypted_path, env_path, gitignore_path = protect_code(path, obfuscation_result)

    print("\rFile obfuscated", end="")
    print()
    print("\rProtecting...", end="")

    
    
    try:
        with open(new_name, 'w', encoding="utf-8") as file:
            file.write(protected)
        print("\rFile protected", end="")
        print()
        if compile:
            print("Compiling...")
            if protected_compile(new_name, noconsole, add_files, add_modules, encrypted_path, env_path, path, show_log):
                print("File compilied")
            else:
                print("Can't compile file, check log")
            print()
        return 1, new_name # new_name - path to file

    except Exception as er:
        print(f"Error: {er}")
        return 0, er