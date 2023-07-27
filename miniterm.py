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
def run_cmd(file_path):
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
def exec_cmd():
    global commands
    file = open(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.cmd", "w")
    file.write("@echo off\n")
    for i in commands:
        file.write(i + "\n")
    file.close()
    subprocess.run(f"cmd /c C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.cmd", shell=True)
    os.remove(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.cmd")
def exec_asm05():
    code = open(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05", "w")
    a = ""
    for i in commands:
        a += i + "\n"
    a = a[:-1]
    code.write(a)
    code.close()
    run_asm05(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05")
    os.remove(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05")
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
        elif command.lower().startswith("!runcmd"):
            if len(command.split(" ")) > 1:
                if os.path.isfile(''.join(command.split(" ")[1:])):
                    if ''.join(command.split(" ")[1:]).lower().endswith(".bat") or ''.join(command.split(" ")[1:]).lower().endswith(".cmd") or ''.join(command.split(" ")[1:]).lower().endswith(".exe"):
                        run_cmd(''.join(command.split(" ")[1:]))
                    else:
                        print(colorama.Back.RED + "Invalid format. The file must be with .bat, .cmd or .exe extension.")
                else:
                    print(colorama.Back.RED + "The system cannot find the path specified.")
            else:
                exec_cmd()
                commands = []
        elif command.lower().startswith("!runasm"):
            if len(command.split(" ")) > 1:
                if os.path.isfile(''.join(command.split(" ")[1:])):
                    if ''.join(command.split(" ")[1:]).lower().endswith(".asm05"):
                        run_asm05(''.join(command.split(" ")[1:]))
                    else:
                        print(colorama.Back.RED + "Invalid format. The file must be with .asm05 extension.")
                else:
                    print(colorama.Back.RED + "The system cannot find the path specified.")
            else:
                code = open(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05", "w")
                a = ""
                for i in commands:
                    a += i + "\n"
                a = a[:-1]
                code.write(a)
                code.close()
                run_asm05(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05")
                os.remove(f"C:\\Users\\{getuser()}\\AppData\\Local\\MiniTerminalTempCode.asm05")
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
        elif command.lower() == "!reset":
            commands = []
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
    !runcmd <bat-or-cmd-or-exe-extension-file>: run the file
    !runasm: run the script
    !runasm <asm-extension-file>: run the file
ASM05-exclusive commands:
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
        PE: ParamError (invalid params) """)
        else:
            commands.append(command)

if __name__ == "__main__":
    main()
