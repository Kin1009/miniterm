import subprocess
import os
from getpass import *
import colorama
import ctypes
import sys
ctypes.windll.kernel32.SetConsoleTitleW("BAT / CMD / EXE / ASM05 Runner")
commands = []
def isAdmin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0
def run_console_file(file_path):
    subprocess.run(file_path, shell=True)
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
        print(colorama.Back.RED + error)
        if stopwhenerror == 1:
            sys.exit()
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
def execute_commands():
    global commands
    user = getuser()
    file = open(f"C:\\Users\\{user}\\AppData\\Local\\MiniTerminalTempCode.cmd", "w")
    file.write("@echo off\n")
    for i in commands:
        file.write(i + "\n")
    file.close()
    subprocess.run(f"cmd /c C:\\Users\\{user}\\AppData\\Local\\MiniTerminalTempCode.cmd", shell=True)
    os.remove(f"C:\\Users\\{user}\\AppData\\Local\\MiniTerminalTempCode.cmd")
def main():
    global commands
    subprocess.run("echo > nul", shell=True)
    print(colorama.Back.GREEN + "BAT / CMD / EXE / ASM05 Runner [Version 0.2]\nType \"!help\" or \"help\" for help.")
    while True:
        current_dir = os.getcwd()
        a = colorama.Fore.RESET
        if isAdmin():
            a = colorama.Back.GREEN
        else:
            a = colorama.Back.RED
        command = input(a + getuser() + colorama.Back.RESET + ": " + colorama.Back.BLUE + current_dir + colorama.Back.RESET + " > ")
        if command.lower() == "!exit":
            break
        elif command.lower().startswith("!run"):
            if len(command.split(" ")) > 1:
                if os.path.isfile(''.join(command.split(" ")[1:])):
                    if ''.join(command.split(" ")[1:]).lower().endswith(".bat") or ''.join(command.split(" ")[1:]).lower().endswith(".cmd") or ''.join(command.split(" ")[1:]).lower().endswith(".exe"):
                        run_console_file(''.join(command.split(" ")[1:]))
                    elif ''.join(command.split(" ")[1:]).lower().endswith(".asm05"):
                        run_asm05(''.join(command.split(" ")[1:]))
                else:
                    print(colorama.Back.RED + "The system cannot find the path specified.")
            else:
                execute_commands()
                commands = []
        elif command.lower().startswith("!cd"):
            if len(command.split(" ")) > 1:
                try:
                    os.chdir("".join(command.split(" ")[1:]))
                except:
                    print(colorama.Back.RED + "The system cannot find the path specified.")
            else:
                print(os.getcwd())
        elif command.lower().startswith("!dir"):
            if len(command.split(" ")) > 1:
                try:
                    subprocess.run(["dir", "".join(command.split(" ")[1:])], shell=True, stderr=subprocess.PIPE)
                except subprocess.CalledProcessError as e:
                    print(colorama.Back.RED + e.stderr)
            else:
                os.system("dir")
        elif command.lower() == "!cls":
            os.system("cls")
        elif command.lower() in ("help", "!help"):
            print("Help:\n!cls: clear screen\n!exit: exit\n!run: run\n!cd: change dir\n!dir: show dir\n!run (filename).bat: run (filename).bat\n!run (filename).cmd: run (filename).cmd\n!run (filename).exe: run (filename).exe\n!run (filename).asm05: run (filename).asm05")
        else:
            commands.append(command)

if __name__ == "__main__":
    main()
