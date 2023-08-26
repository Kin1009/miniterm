import base64
import copy
import ctypes
import json
import os
from base64 import (b16decode, b16encode, b32decode, b32encode, b64decode,
                    b64encode, b85decode, b85encode)
from getpass import getuser
from os import chdir, getcwd, remove, system
from os.path import basename, isdir, isfile
from random import randint
from shutil import make_archive, move
from subprocess import PIPE, CalledProcessError, run
from sys import argv, exit
from zipfile import ZipFile

import colorama

try:
    chdir(argv[1])#chdir(' '.join(argv[1:]))
except:
    pass
ctypes.windll.kernel32.SetConsoleTitleW("BAT / CMD / EXE / ASM05 Runner")
commands = []
def isAdmin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0
def run_cmd(file_path):
    run(file_path, shell=True)
def pack16(input_path, output_path):
    print("Packing: " + input_path)
    string = ""
    try:
        for i in range(10):
            string += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[randint(0, len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") - 1)]
        if isfile(input_path):
            with ZipFile(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'w') as zipf:
                zipf.write(input_path, basename(input_path))
        elif isdir(input_path):
            make_archive(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}", 'zip', input_path)
        else:
            print(colorama.Back.RED + "Invalid path." + colorama.Back.RESET)
        with open(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'rb') as zip_file:
            base64_data = b16encode(zip_file.read())
        with open(output_path, 'wb') as output_file:
            output_file.write(base64_data)
        remove(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip")
    except Exception as e:
        print(colorama.Back.RED + str(e).replace("\\\\", "\\"))
def extract16(input_path, output_path):
    print("Extracting: " + input_path)
    try:
        with open(input_path, 'rb') as input_file:
            base64_data = input_file.read()
        string = ""
        for i in range(10):
            string += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[randint(0, len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") - 1)]
        with open(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'wb') as zip_file:
            zip_file.write(b16decode(base64_data))
        if output_path.endswith('.zip'):
            move(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", output_path)
        else:
            with ZipFile(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'r') as zip_ref:
                zip_ref.extractall(output_path)
        remove(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip")
    except Exception as e:
        print(colorama.Back.RED + str(e).replace("\\\\", "\\") + colorama.Back.RESET)
def pack32(input_path, output_path):
    print("Packing: " + input_path)
    string = ""
    try:
        for i in range(10):
            string += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[randint(0, len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") - 1)]
        if isfile(input_path):
            with ZipFile(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'w') as zipf:
                zipf.write(input_path, basename(input_path))
        elif isdir(input_path):
            make_archive(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}", 'zip', input_path)
        else:
            print(colorama.Back.RED + "Invalid path." + colorama.Back.RESET)
        with open(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'rb') as zip_file:
            base64_data = b32encode(zip_file.read())
        with open(output_path, 'wb') as output_file:
            output_file.write(base64_data)
        remove(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip")
    except Exception as e:
        print(colorama.Back.RED + str(e).replace("\\\\", "\\"))
def extract32(input_path, output_path):
    print("Extracting: " + input_path)
    try:
        with open(input_path, 'rb') as input_file:
            base64_data = input_file.read()
        string = ""
        for i in range(10):
            string += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[randint(0, len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") - 1)]
        with open(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'wb') as zip_file:
            zip_file.write(b32decode(base64_data))
        if output_path.endswith('.zip'):
            move(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", output_path)
        else:
            with ZipFile(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'r') as zip_ref:
                zip_ref.extractall(output_path)
        remove(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip")
    except Exception as e:
        print(colorama.Back.RED + str(e).replace("\\\\", "\\") + colorama.Back.RESET)
def pack64(input_path, output_path):
    print("Packing: " + input_path)
    string = ""
    try:
        for i in range(10):
            string += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[randint(0, len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") - 1)]
        if isfile(input_path):
            with ZipFile(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'w') as zipf:
                zipf.write(input_path, basename(input_path))
        elif isdir(input_path):
            make_archive(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}", 'zip', input_path)
        else:
            print(colorama.Back.RED + "Invalid path." + colorama.Back.RESET)
        with open(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'rb') as zip_file:
            base64_data = b64encode(zip_file.read())
        with open(output_path, 'wb') as output_file:
            output_file.write(base64_data)
        remove(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip")
    except Exception as e:
        print(colorama.Back.RED + str(e).replace("\\\\", "\\"))
def extract64(input_path, output_path):
    print("Extracting: " + input_path)
    try:
        with open(input_path, 'rb') as input_file:
            base64_data = input_file.read()
        string = ""
        for i in range(10):
            string += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[randint(0, len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") - 1)]
        with open(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'wb') as zip_file:
            zip_file.write(b64decode(base64_data))
        if output_path.endswith('.zip'):
            move(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", output_path)
        else:
            with ZipFile(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'r') as zip_ref:
                zip_ref.extractall(output_path)
        remove(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip")
    except Exception as e:
        print(colorama.Back.RED + str(e).replace("\\\\", "\\") + colorama.Back.RESET)
def pack85(input_path, output_path):
    print("Packing: " + input_path)
    string = ""
    try:
        for i in range(10):
            string += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[randint(0, len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") - 1)]
        if isfile(input_path):
            with ZipFile(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'w') as zipf:
                zipf.write(input_path, basename(input_path))
        elif isdir(input_path):
            make_archive(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}", 'zip', input_path)
        else:
            print(colorama.Back.RED + "Invalid path." + colorama.Back.RESET)
        with open(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'rb') as zip_file:
            base64_data = b85encode(zip_file.read())
        with open(output_path, 'wb') as output_file:
            output_file.write(base64_data)
        remove(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip")
    except Exception as e:
        print(colorama.Back.RED + str(e).replace("\\\\", "\\"))
def extract85(input_path, output_path):
    print("Extracting: " + input_path)
    try:
        with open(input_path, 'rb') as input_file:
            base64_data = input_file.read()
        string = ""
        for i in range(10):
            string += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"[randint(0, len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") - 1)]
        with open(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'wb') as zip_file:
            zip_file.write(b85decode(base64_data))
        if output_path.endswith('.zip'):
            move(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", output_path)
        else:
            with ZipFile(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip", 'r') as zip_ref:
                zip_ref.extractall(output_path)
        remove(f"C:/Users/{getuser()}/AppData/Local/Temp/{string}.zip")
    except Exception as e:
        print(colorama.Back.RED + str(e).replace("\\\\", "\\") + colorama.Back.RESET)
def run_asm05(path):
    code = open(path, "r").read()
    stopwhenerror = 0
    def error(type):
        error = ""
        match type:
            case "0": #regerror
                error = "RegError: "
            case "1":
                error = "TypeError: "
            case "2":
                error = "FuncError: "
            case "3":
                error = "ParamError: "
        error += "at line " + str(counter) + ", code: " + code[counter]
        print(colorama.Back.RED + error + colorama.Back.RESET)
        if stopwhenerror == 1:
            exit()
    RE = "0"
    TE = "1"
    FE = "2"
    PE = "3"
    counter = 0
    vars = {}
    hextable = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    code = code.split("\n")
    while counter < len(code):
        command = code[counter]
        command = command.split(" ")
        if len(command):
            try:
                match command[0]:
                    case "var":
                        vars[command[1]] = "0"
                    case "sti":
                        if command[1] in vars:
                            int(command[2])
                            vars[command[1]] = command[2]
                        else:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "sts":
                        string = command[2]
                        res = ""
                        for i in range(0, len(string), 2):
                            res += chr(hextable[string[i]] * 16 + hextable[string[i + 1]])
                        if command[1] in vars:
                            vars[command[1]] = res
                        else:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "otv":
                        if command[1] in vars:
                            print(vars[command[1]])
                        else:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "ots":
                        string = command[1]
                        res = ""
                        for i in range(0, len(string), 2):
                            try:
                                res += chr(hextable[string[i - 1]] * 16 + hextable[string[i]])
                            except:
                                error(TE)
                                if stopwhenerror == 0: break
                        print(res)
                    case "in":
                        if command[1] in vars:
                            vars[command[1]] = input(">>> ")
                        else:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "apn":
                        command[1], command[2], command[3]
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        vars[command[3]] = vars[command[1]] + vars[command[2]]
                    case "add":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE) 
                            if stopwhenerror == 0: break
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a + b if (a + b) % 1 > 0 else int(a + b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "sub":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE) 
                            if stopwhenerror == 0: break
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a - b if (a - b) % 1 > 0 else int(a - b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "mul":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a * b if (a * b) % 1 > 0 else int(a * b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "div":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE) 
                            if stopwhenerror == 0: break
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a / b if (a / b) % 1 > 0 else int(a / b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "exp":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break 
                        try:
                            a, b = float(vars[command[1]]), float(vars[command[2]])
                            vars[command[3]] = str(a ** b if (a ** b) % 1 > 0 else int(a ** b))
                        except:
                            error(TE)
                            if stopwhenerror == 0: break
                    case "bol":
                        try:
                            command[1], command[2]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            a = bool(vars[command[1]])
                            vars[command[2]] = str(int(a))
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                    case "and":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a & b))
                    case "not":
                        try:
                            command[1], command[2]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a = bool(vars[command[1]])
                        vars[command[2]] = str(int(not a))
                    case "nnd":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(not (a & b)))
                    case "or":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a or b))
                    case "nor":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(not (a or b)))
                    case "xor":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a ^ b))
                    case "equ":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = vars[command[1]], vars[command[2]]
                        vars[command[3]] = str(int(a == b))
                    case "grt":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a > b))
                    case "lss":
                        try:
                            command[1], command[2], command[3]
                        except:
                            error(PE)
                            if stopwhenerror == 0: break
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        a, b = bool(vars[command[1]]), bool(vars[command[2]])
                        vars[command[3]] = str(int(a < b))
                    case "jmp":
                        counter = int(command[1]) - 1
                    case "jif":
                        try:
                            vars[command[2]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        if vars[command[2]] == "1":
                            counter = int(command[1]) - 1
                    case "inc":
                        try:
                            vars[command[1]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        _ = vars[command[1]]
                        _ = float(_)
                        _ += 1
                        vars[command[1]] = str(_ if _ % 1 > 0 else int(_))
                    case "dec":
                        try:
                            vars[command[1]]
                        except:
                            error(RE)
                            if stopwhenerror == 0: break
                        _ = vars[command[1]]
                        _ = float(_)
                        _ -= 1
                        vars[command[1]] = str(_ if _ % 1 > 0 else int(_))
                    case "mod":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                            res = int(vars[command[1]]) % int(vars[command[2]])
                            vars[command[3]] = str(res)
                        except KeyError:
                            error(RE)
                        except TypeError:
                            error(TE)
                    case "flr":
                        try:
                            vars[command[1]], vars[command[2]], vars[command[3]]
                            res = int(vars[command[1]]) // int(vars[command[2]])
                            vars[command[3]] = str(res)
                        except KeyError:
                            error(RE)
                        except TypeError:
                            error(TE)
                    case ";":
                        pass
            except:
                error(PE)
                if stopwhenerror == 0: break
            if command[0] not in ("sti", "sts", "otv", "ots", "in", "var", "apn", "add", "sub", "bol", "inc", "dec", "mul", "div", "exp", "equ", "grt", "lss", "jmp", "jif", "and", "not", "nnd", "or", "nor", "xor", ";", "mod", "flr", ""):
                error(FE)
                if stopwhenerror == 0: break
        counter += 1
def exec_cmd():
    global commands
    file = open(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.cmd", "w")
    file.write("@echo off\n")
    for i in commands:
        file.write(i + "\n")
    file.close()
    run(f"cmd /c C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.cmd", shell=True)
    remove(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.cmd")
def exec_asm05():
    code = open(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05", "w")
    a = ""
    for i in commands:
        a += i + "\n"
    a = a[:-1]
    code.write(a)
    code.close()
    run_asm05(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05")
    remove(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05")
run("echo > nul", shell=True)
print(colorama.Back.GREEN + "BAT / CMD / EXE / ASM05 Runner [Version 0.2]\nType \"!help\" or \"help\" for help." + colorama.Back.RESET)
while True:
    current_dir = getcwd()
    a = colorama.Back.RESET
    if isAdmin():
        a = colorama.Back.GREEN
    else:
        a = colorama.Back.RED
    command = input(a + getuser() + colorama.Back.RESET + ": " + colorama.Back.BLUE + current_dir + colorama.Back.RESET + " > ")
    if command.lower() == "!exit":
        break
    elif command.lower().startswith("!runcmd"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])):
                if ' '.join(command.split(" ")[1:]).lower().endswith(".bat") or ' '.join(command.split(" ")[1:]).lower().endswith(".cmd") or ''.join(command.split(" ")[1:]).lower().endswith(".exe"):
                    run_cmd(' '.join(command.split(" ")[1:]))
                else:
                    print(colorama.Back.RED + "Invalid format. The file must be with .bat, .cmd or .exe extension.")
            else:
                print(colorama.Back.RED + "The system cannot find the path specified.")
        else:
            exec_cmd()
            commands = []
    elif command.lower().startswith("!runasm"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])):
                if ' '.join(command.split(" ")[1:]).lower().endswith(".asm05"):
                    run_asm05(' '.join(command.split(" ")[1:]))
                else:
                    print(colorama.Back.RED + "Invalid format. The file must be with .asm05 extension." + colorama.Back.RESET)
            else:
                print(colorama.Back.RED + "The system cannot find the path specified." + colorama.Back.RESET)
        else:
            code = open(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05", "w")
            a = ""
            for i in commands:
                a += i + "\n"
            a = a[:-1]
            code.write(a)
            code.close()
            run_asm05(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05")
            remove(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05")
            commands = []
    elif command.lower().startswith("!cd"):
        if len(command.split(" ")) > 1:
            try:
                chdir(" ".join(command.split(" ")[1:]))
            except:
                print(colorama.Back.RED + "The system cannot find the path specified." + colorama.Back.RESET)
        else:
            print(getcwd())
    elif command.lower().startswith("!dir"):
        if len(command.split(" ")) > 1:
            try:
                run(["dir", " ".join(command.split(" ")[1:])], shell=True, stderr=PIPE)
            except CalledProcessError as e:
                print(colorama.Back.RED + e.stderr + colorama.Back.RESET)
        else:
            system("dir")
    elif command.lower() == "!cls":
        system("cls")
    elif command.lower() == "!reset":
        commands = []
    elif command.lower().startswith("!pack16"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])) or isdir(' '.join(command.split(" ")[1:])):
                pack16(' '.join(command.split(" ")[1:]), ' '.join(command.split(" ")[1:]) + ".ins16")
            else:
                print(colorama.Back.RED + "Invalid path." + colorama.Back.RESET)
        else:
            print(colorama.Back.RED + "Invalid parameters." + colorama.Back.RESET)
    elif command.lower().startswith("!extract16"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])) or isdir(' '.join(command.split(" ")[1:])):
                if ' '.join(command.split(" ")[1:]).endswith(".ins16"):
                    extract16(' '.join(command.split(" ")[1:]), ' '.join(command.split(" ")[1:])[:-5])
                else:
                    print(colorama.Back.RED + "Invalid file type." + colorama.Back.RESET)
            else:
                print(colorama.Back.RED + "Invalid path.") + colorama.Back.RESET
        else:
            print(colorama.Back.RED + "Invalid parameters." + colorama.Back.RESET)
    elif command.lower().startswith("!pack32"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])) or isdir(' '.join(command.split(" ")[1:])):
                pack32(' '.join(command.split(" ")[1:]), ' '.join(command.split(" ")[1:]) + ".ins32")
            else:
                print(colorama.Back.RED + "Invalid path." + colorama.Back.RESET)
        else:
            print(colorama.Back.RED + "Invalid parameters." + colorama.Back.RESET)
    elif command.lower().startswith("!extract32"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])) or isdir(' '.join(command.split(" ")[1:])):
                if ' '.join(command.split(" ")[1:]).endswith(".ins32"):
                    extract32(' '.join(command.split(" ")[1:]), ' '.join(command.split(" ")[1:])[:-5])
                else:
                    print(colorama.Back.RED + "Invalid file type." + colorama.Back.RESET)
            else:
                print(colorama.Back.RED + "Invalid path.") + colorama.Back.RESET
        else:
            print(colorama.Back.RED + "Invalid parameters." + colorama.Back.RESET)
    elif command.lower().startswith("!pack64"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])) or isdir(' '.join(command.split(" ")[1:])):
                pack64(' '.join(command.split(" ")[1:]), ' '.join(command.split(" ")[1:]) + ".ins64")
            else:
                print(colorama.Back.RED + "Invalid path." + colorama.Back.RESET)
        else:
            print(colorama.Back.RED + "Invalid parameters." + colorama.Back.RESET)
    elif command.lower().startswith("!extract64"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])) or isdir(' '.join(command.split(" ")[1:])):
                if ' '.join(command.split(" ")[1:]).endswith(".ins64"):
                    extract64(' '.join(command.split(" ")[1:]), ' '.join(command.split(" ")[1:])[:-5])
                else:
                    print(colorama.Back.RED + "Invalid file type." + colorama.Back.RESET)
            else:
                print(colorama.Back.RED + "Invalid path.") + colorama.Back.RESET
        else:
            print(colorama.Back.RED + "Invalid parameters." + colorama.Back.RESET)
    elif command.lower().startswith("!pack85"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])) or isdir(' '.join(command.split(" ")[1:])):
                pack85(' '.join(command.split(" ")[1:]), ' '.join(command.split(" ")[1:]) + ".ins85")
            else:
                print(colorama.Back.RED + "Invalid path." + colorama.Back.RESET)
        else:
            print(colorama.Back.RED + "Invalid parameters." + colorama.Back.RESET)
    elif command.lower().startswith("!extract85"):
        if len(command.split(" ")) > 1:
            if isfile(' '.join(command.split(" ")[1:])) or isdir(' '.join(command.split(" ")[1:])):
                if ' '.join(command.split(" ")[1:]).endswith(".ins85"):
                    extract85(' '.join(command.split(" ")[1:]), ' '.join(command.split(" ")[1:])[:-5])
                else:
                    print(colorama.Back.RED + "Invalid file type." + colorama.Back.RESET)
            else:
                print(colorama.Back.RED + "Invalid path.") + colorama.Back.RESET
        else:
            print(colorama.Back.RED + "Invalid parameters." + colorama.Back.RESET)
    elif command.lower() == "!asm05":
        c = ""
        print("ASM0.5 [Version 1.2]\nType \"help\" for help.")
        while True:
            inp = input("> ")
            match inp:
                case "run":
                    with open(f"C:\\Users\\{getuser()}\\AppData\\Local\\Temp\\asm05.asm05", "w") as file:
                        file.write(c[:-1])
                    run_asm05(f"C:\\Users\\{getuser()}\\AppData\\Local\\Temp\\asm05.asm05")
                    remove(f"C:\\Users\\{getuser()}\\AppData\\Local\\Temp\\asm05.asm05")
                    c = ""
                case "exit":
                    break
                case "help":
                    print("""
ASM05 help:
1. Functions:
sti reg, value            set reg <reg> to <value> (int)
sts reg, value            set reg <reg> to <value> (str) (hex)
otv reg                   print reg <reg>
ots hex                   print <hex> converted to string
in reg                    set input to <reg> (let <reg> input)
add regA, regB, regDist   add <regA> to <regB>, set result to <regDist>
sub regA, regB, regDist   sub <regA> to <regB>, set result to <regDist>
mul regA, regB, regDist   mul <regA> to <regB>, set result to <regDist>
div regA, regB, regDist   div <regA> to <regB>, set result to <regDist>
exp regA, regB, regDist   exp <regA> to <regB>, set result to <regDist>
and regA, regB, regDist   and <regA> and <regB>, set result to <regDist>
not regA, regDist         not <regA>, set result to <regDist>
nnd regA, regB, regDist   nand <regA> and <regB>, set result to <regDist>
or regA, regB, regDist    or <regA> and <regB>, set result to <regDist>
nor regA, regB, regDist   nor <regA> and <regB>, set result to <regDist>
xor regA, regB, regDist   xor <regA> and <regB>, set result to <regDist>
equ regA, regB, regDist   if <regA> == <regB>, set 1 to <regDist> else 0
grt regA, regB, regDist   if <regA> > <regB>, set 1 to <regDist> else 0
lss regA, regB, regDist   if <regA> < <regB>, set 1 to <regDist> else 0
jmp line                  jump to line <line>
jif line, reg             jump to line <line> if <reg> == 1
var <reg>                 make reg <reg>
bol reg, regDist          turn <reg> to boolean, set result to <regDist> 
apn regA regB regDist     <regDist> = <regA> + <regB>
inc reg                   <reg> += 1
dec reg                   <reg> -= 1
mod regA regB regDist     <regA> % <regB> -> <regDist>
flr regA regB regDist     <regA> % <regB> -> <regDist>
;                         comment

2. Errors:
RE         RegError (access a reg that doesn't exist)
TE         TypeError (not the type it expected)
FE         FuncError (invalid func)
PE         ParamError (invalid params) 

3. Console commands:
run        run code
exit       exit
help       help""")
                case _:
                    c += inp + "\n"
    elif command.lower() == "!minifs":
        class Exit(Exception):
            pass
        class FileSys:
            current_drive = "c"  # Default drive
            drive_folder_path = os.path.join(os.path.expandvars("%LOCALAPPDATA%"), "minifs")
            VER = "Mini Filesystem [B3F5 (Import / export folders update)] (Bugfix 3 Features 5)"
            def __init__(self):
                self.current_path = []
                self.drive = {}
                self.load_drive(self.drive_folder_path + "\\" + self.current_drive)
            def cd(self, target_path=None):
                if target_path:
                    target_folders = target_path.split("\\")
                    current = self.drive
                    for i in self.current_path:
                        current = current[i]
                    for i in target_folders:
                            if (i in current) and isinstance(current[i], dict):
                                current = current[i]
                                self.current_path.append(i)
                            elif i == "..":
                                self.current_path.pop()
                                current = self.drive
                                for i in self.current_path:
                                    current = current[i]
                            else:
                                print("Target directory not found.")
                                return
                else:
                    print(self.current_drive + "\\" + "\\".join(self.current_path))

            def dir(self, target_path=None):
                if not target_path:
                    target_folders = ""
                else:
                    target_folders = target_path.split("\\")
                current = self.drive
                current_path = copy.deepcopy(self.current_path)
                for i in self.current_path:
                    current = current[i]
                for i in target_folders:
                        if (i in current) and isinstance(current[i], dict):
                            current = current[i]
                            self.current_path.append(i)
                        elif i == "..":
                            self.current_path.pop()
                            current = self.drive
                            for i in self.current_path:
                                current = current[i]
                        else:
                            print("Target directory not found.")
                            self.current_path = current_path
                            return
                folders, files = [], []
                for item in current.keys():
                    if isinstance(current[item], dict):
                        folders.append(item)
                    elif isinstance(current[item], str):
                        files.append(item)
                for file in files:
                    print(f"file {file}")
                for folder in folders:
                    print(f"folder {folder}")
                self.current_path = current_path
            def read(self, target):
                current = self.drive
                for folder in self.current_path:
                    current = current[folder]
                if target in current and isinstance(current[target], str):
                    print(current[target])
                else:
                    print("Target is not a file.")
            def save_drive(self):
                path = os.path.join(drive_folder_path, f"{self.current_drive}")
                drive_json = json.dumps(self.drive, indent=4)
                drive_b64 = base64.b64encode(drive_json.encode("utf-8"))
                with open(path, "wb") as f:
                    f.write(drive_b64)

            def load_drive(self, path):
                if os.path.exists(path):
                    with open(path, "r") as f:
                        drive_b64 = f.read()
                        try:
                            drive_json = base64.b64decode(drive_b64).decode("utf-8")
                            self.drive = json.loads(drive_json)
                        except Exception as e:
                            print("Error loading drive:", e)
                            self.drive = {}
                else:
                    print("Drive file not found, starting with empty drive.")

            def new_drive(self, drive_name):
                self.save_drive()  # Save the current drive before creating a new one
                self.drive = {}
                self.current_path = []
                self.current_drive = drive_name
                self.save_drive()

            def new_folder(self, folder_name):
                current = self.drive
                for folder in self.current_path:
                    current = current[folder]
                current[folder_name] = {}

            def delete_item(self, item_name):
                current = self.drive
                for folder in self.current_path:
                    current = current[folder]
                if item_name in current:
                    del current[item_name]
                else:
                    print("Item not found.")

            def delete_drive(self, drive_name):
                drive_file_path = os.path.join(drive_folder_path, f"{drive_name.lower()}")
                if os.path.exists(drive_file_path):
                    os.remove(drive_file_path)
                    if self.current_drive == drive_name:
                        self.current_drive = "c"
                else:
                    print("Invalid drive.")
            def write(self, filename):
                try:
                    current = self.drive
                    for folder in self.current_path:
                        current = current[folder]
                    a = base64.b16decode(input("Enter base-16 string: ").encode(), True)
                    res = ""
                    for i in a: res += chr(i)
                    current[filename] = res
                except Exception as e:
                    print("Error writing file: " + str(e))

            def write_(self, filename, a):
                current = self.drive
                for folder in self.current_path:
                    current = current[folder]
                res = ""
                for i in a: res += chr(i)
                current[filename] = res
            def path_to_dict(self, path, d={}):
                name = os.path.basename(path)
                if os.path.isdir(path):
                    if name not in d:
                        d[name] = {}
                    for x in os.listdir(path):
                        self.path_to_dict(os.path.join(path, x), d[name])
                else:
                    try:
                        with open(path, 'r') as file:
                            d[name] = file.read()
                    except Exception as e:
                        print("Error: " + str(e))
                return d
            def import_(self, path):
                if os.path.isfile(path):
                    self.write_(os.path.basename(path), open(path, "rb").read())
                elif os.path.isdir(path):
                    data = self.path_to_dict(path=path)
                    current = self.drive
                    for i in self.current_path:
                        current = current[i]
                    current.update(data)
                else:
                    print("Invalid path.")
            def export(self, file, dist):
                def one_directory(dic, path):
                    for name, info in dic.items():
                        next_path = path + "/" + name
                        if isinstance(info, dict):
                            next_path = os.path.abspath(next_path)
                            os.mkdir(next_path)
                            one_directory(info, next_path)
                        else:
                            try:
                                with open(os.path.abspath(os.path.join(next_path)), "w") as f:
                                    f.write(info)
                            except Exception as e:
                                print("Error: " + str(e))
                try:
                    current = self.drive
                    for folder in self.current_path:
                        current = current[folder]
                    if file not in current:
                        print("Invalid path.")
                    elif isinstance(current[file], str):
                        a = open(dist, "w")
                        a.write(current[file])
                        a.close()
                    else:
                        one_directory(current, dist)
                except Exception as e:
                    print("Error: " + str(e))
            def run(self, code_) -> int:
                code_ = code_.splitlines() if "\n" in code_ else [code_]
                for i in code_:
                    try:
                        command = i.split(" ")
                        if not command: pass
                        elif command[0] == "dir":
                            if len(command) > 1:
                                self.dir(" ".join(command[1:]))
                            else:
                                self.dir()
                        elif command[0] == "cd":
                            if len(command) > 1:
                                self.cd(" ".join(command[1:]))
                            else:
                                self.cd()
                        elif command[0] == "read":
                            if len(command) > 1:
                                self.read(" ".join(command[1:]))
                        elif command[0] == "mkdrv":
                            if len(command) > 1:
                                if not "\\" in " ".join(command[1:]):
                                    self.new_drive(" ".join(command[1:]))
                                else:
                                    print("Drive name mustn't contain backslashes")
                        elif command[0] == "drv":
                            self.save_drive()
                            if len(command) > 1:
                                drive_file_path = os.path.join(drive_folder_path, f"{command[1].lower()}")
                                if os.path.exists(drive_file_path):
                                    self.load_drive(drive_file_path)
                                    self.current_drive = command[1]
                                else:
                                    print("Drive not found.")
                        elif command[0] == "mkdir":
                            if len(command) > 1:
                                if not "\\" in " ".join(command[1:]):
                                    self.new_folder(" ".join(command[1:]))
                                else:
                                    print("Path mustn't contain backslashes")
                        elif command[0] == "del":
                            if len(command) > 1:
                                self.delete_item(" ".join(command[1:]))
                        elif command[0] == "deldrv":
                            if len(command) > 1:
                                if command[1].lower() == "c":
                                    print("Cannot delete the default 'c' drive.")
                                else:
                                    self.delete_drive(command[1])
                        elif command[0] == "write":
                            if len(command) > 1:
                                filename = " ".join(command[1:]).split("|", 1)[0]
                                if "\\" in filename:
                                    print("Path mustn't contain backslashes.")
                                else:
                                    data = " ".join(command[1:]).split("|", 1)[1]
                                    self.write_(filename=filename, a=data)
                            if len(command) > 1:
                                if not "\\" in " ".join(command[1:]):
                                    self.write(" ".join(command[1:]))
                                else:
                                    print("Path mustn't contain backslashes")
                        elif command[0] == "import":
                            if len(command) > 1:
                                self.import_(" ".join(command[1:]))
                        elif command[0] == "export":
                            if len(command) > 1:
                                self.export(" ".join(command[1:]).split("|")[0], " ".join(command[1:]).split("|")[1])
                        elif command[0] == "run":
                            if len(command) > 1:
                                return self.runfile(" ".join(command[1:]))
                        elif command[0] == "exit":
                            self.save_drive()
                            raise Exit 
                        elif command[0] == "cls":
                            os.system("cls")
                        elif command[0] == "ver":
                            print(self.VER)
                        elif command[0] == "help":
                            print("""Help:
        Basic:
            help: help
            exit: exit
            cls: clear
            ver: show version
        Create:
            mkdir <folder_name>: make folder
            mkdrv <drive_name>: make drive
            import <file_on_u_computer>: import that file / folder, store it at current dir
        Delete:
            del <file_or_folder>: delete file / folder
            deldrv <drive_name>: delete drive
        View:
            dir: show current dir files / folders, support "\\" and ".."
            dir <folder>: show that dir files / folders, support "\\" and ".."
            cd: show current dir, support "\\" and ".."
            cd <folder>: go to that dir, support "\\" and ".."
            read <file>: show file contents
            drv <drive_name>: go to that drive
        Other:
            export <file_in_this_prog>|<output_file_on_u_computer>: export to your computer ("|" included, example: "export a|c\\d")
            run <file>: run the file using this set of command""")
                        else:
                            print("Unknown command: \"" + command[0] + "\"")
                    except Exit as e:
                        return 1
                    except Exception as e:
                        print("Error: " + str(e))
                    self.save_drive()
                return 0
            def runfile(self, file):
                current = self.drive
                for i in self.current_path:
                    current = current[i]
                if (file in current) and isinstance(current[file], str):
                    return self.run(current[file])
                else:
                    print("Invalid item.")
        # Define the drive folder path (Windows-specific)
        drive_folder_path = os.path.join(os.path.expandvars("%LOCALAPPDATA%"), "minifs")
        os.makedirs(drive_folder_path, exist_ok=True)

        # Example usage
        self = FileSys()
        print(f"{self.VER}\nType \"help\" to get help.")
        while True:
            current_dir = os.path.abspath(os.path.join(drive_folder_path, *self.current_path))
            SEP = "\\"
            prompt = f"{self.current_drive}> " if not self.current_path else f"{self.current_drive}\\{SEP.join(self.current_path)}> "
            inp = input(prompt)
            if self.run(inp) == 1:
                break
    elif command.lower() in ("help", "!help"):
        print("""Help:
CMD-like commands:
!cd: show directory
!cd <dir>: change directory
!dir: list current directory
!dir <dir>: list <dir>'s directory
!cls: clear screen
!exit: exit
              
Commands:
!help or help: show help
!reset: clear command
!runcmd: run the script
!runcmd <bat-or-cmd-or-exe-file>: run the file
!runasm: run the script
!runasm <asm-file>: run the file
              
Offline installer-exclusive commands (Extended):
!pack16 <path-to-file-or-dir>: pack the file
!extract16 <path-to-ins16-file>: extract the file
!pack32 <path-to-file-or-dir>: pack the file
!extract32 <path-to-ins32-file>: extract the file
!pack64 <path-to-file-or-dir>: pack the file
!extract64 <path-to-ins64-file>: extract the file
!pack85 <path-to-file-or-dir>: pack the file
!extract85 <path-to-ins85-file>: extract the file
              
ASM05-exclusive commands:
!asm05: open ASM05 shell
Functions:
    sti reg, value: set reg <reg> to <value> (int)
    sts reg, value: set reg <reg> to <value> (str) (hex)
    otv reg: print reg <reg>
    ots hex: print <hex> converted to string
    in reg: set input to <reg> (let <reg> input)
    add regA, regB, regDist: add <regA> to <regB>, set result to <regDist>
    sub regA, regB, regDist: sub <regA> to <regB>, set result to <regDist>
    mul regA, regB, regDist: mul <regA> to <regB>, set result to <regDist>
    div regA, regB, regDist: div <regA> to <regB>, set result to <regDist>
    exp regA, regB, regDist: exp <regA> to <regB>, set result to <regDist>
    and regA, regB, regDist: and <regA> and <regB>, set result to <regDist>
    not regA, regDist: not <regA>, set result to <regDist>
    nnd regA, regB, regDist: nand <regA> and <regB>, set result to <regDist>
    or regA, regB, regDist: or <regA> and <regB>, set result to <regDist>
    nor regA, regB, regDist: nor <regA> and <regB>, set result to <regDist>
    xor regA, regB, regDist: xor <regA> and <regB>, set result to <regDist>
    equ regA, regB, regDist: if <regA> == <regB>, set 1 to <regDist> else 0
    grt regA, regB, regDist: if <regA> > <regB>, set 1 to <regDist> else 0
    lss regA, regB, regDist: if <regA> < <regB>, set 1 to <regDist> else 0
    jmp line: jump to line <line>
    jif line, reg: jump to line <line> if <reg> == 1
    var <reg>: make reg <reg>
    bol reg, regDist: turn <reg> to boolean, set result to <regDist> 
    apn regA regB regDist: <regDist> = <regA> + <regB>
    inc reg: <reg> += 1
    dec reg: <reg> -= 1
    mod regA regB regDist: <regA> % <regB> -> <regDist>
    flr regA regB regDist: <regA> % <regB> -> <regDist>
    ; (semicolon symbol): comment
              
Errors:
    RE: RegError (access a reg that doesn't exist)
    TE: TypeError (not the type it expected)
    FE: FuncError (invalid func)
    PE: ParamError (invalid params)

Mini Filesystem-exclusive commands:
!minifs: open Mini Filesystem's shell
Basic:
    help: help
    exit: exit
    cls: clear
    ver: show version
Create:
    mkdir <folder_name>: make folder
    mkdrv <drive_name>: make drive
    import <file_on_u_computer>: import that file / folder, store it at current dir
Delete:
    del <file_or_folder>: delete file / folder
    deldrv <drive_name>: delete drive
View:
    dir: show current dir files / folders, support "\\" and ".."
    dir <folder>: show that dir files / folders, support "\\" and ".."
    cd: show current dir, support "\\" and ".."
    cd <folder>: go to that dir, support "\\" and ".."
    read <file>: show file contents
    drv <drive_name>: go to that drive
Other:
    export <file_in_this_prog>|<output_file_on_u_computer>: export to your computer ("|" included, example: "export a|c\\d")
    run <file>: run the file using this set of command""")
    else:
        commands.append(command)