# miniterm
A mini terminal used to run scripts (BAT / CMD / EXE / ASM05*)
# Usage
- CMD exact commands
    - `!cd`: show directory
    - `!cd {dir}`: change directory
    - `!dir`: list current directory
    - `!dir {dir}`: list `{dir}`'s directory
    - `!cls`: clear screen
    - `!exit`: exit
- Commands
    - `!help` or `help`: show help
    - `!reset`: clear command
    - `!runcmd`: run the script
    - `!runcmd {bat-or-cmd-or-exe--file}`: run the file
    - `!runasm`: run the script
    - `!runasm {asm--file}`: run the file
- ASM05-exclusive commands:
    - Functions:
        - `sti reg, value`: set reg `{reg}` to `{value}` (int)
        - `sts reg, value`: set reg `{reg}` to `{value}` (str) (hex)
        - `otv reg`: print reg `{reg}`
        - `ots hex`: print `{hex}` converted to string
        - `in reg`: set input to `{reg}` (let `{reg}` input)
        - `add regA, regB, regDist`: add `{regA}` to `{regB}`, set result to `{regDist}`
        - `sub regA, regB, regDist`: sub `{regA}` to `{regB}`, set result to `{regDist}`
        - `mul regA, regB, regDist`: mul `{regA}` to `{regB}`, set result to `{regDist}`
        - `div regA, regB, regDist`: div `{regA}` to `{regB}`, set result to `{regDist}`
        - `exp regA, regB, regDist`: exp `{regA}` to `{regB}`, set result to `{regDist}`
        - `and regA, regB, regDist`: and `{regA}` and `{regB}`, set result to `{regDist}`
        - `not regA, regDist`: not `{regA}`, set result to `{regDist}`
        - `nnd regA, regB, regDist`: nand `{regA}` and `{regB}`, set result to `{regDist}`
        - `or regA, regB, regDist`: or `{regA}` and `{regB}`, set result to `{regDist}`
        - `nor regA, regB, regDist`: nor `{regA}` and `{regB}`, set result to `{regDist}`
        - `xor regA, regB, regDist`: xor `{regA}` and `{regB}`, set result to `{regDist}`
        - `equ regA, regB, regDist`: if `{regA}` == `{regB}`, set 1 to `{regDist}` else 0
        - `grt regA, regB, regDist`: if `{regA}` > `{regB}`, set 1 to `{regDist}` else 0
        - `lss regA, regB, regDist`: if `{regA}` < `{regB}`, set 1 to `{regDist}` else 0
        - `jmp line`: jump to line `{line}`
        - `jif line, reg`: jump to line `{line}` if `{reg}` == 1
        - `var reg`: make reg `{reg}`
        - `bol reg, regDist`: turn `{reg}` to boolean, set result to `{regDist}` 
        - `apn regA regB regDist`: `{regDist}` = `{regA}` + `{regB}`
        - `inc reg`: `{reg}` += 1
        - `dec reg`: `{reg}` -= 1
        - `; comment` (semicolon symbol): comment
    - Broken functions:
        - `mod regA regB regDist`: `{regA}` % `{regB}` -> `{regDist}`
        - `flr regA regB regDist`: `{regA}` // `{regB}` -> `{regDist}`
    - Errors:
        - RE: RegError (access a reg that doesn't exist)
        - TE: TypeError (not the type it expected)
        - FE: FuncError (invalid func)
        - PE: ParamError (invalid params)
- Notes
    *: Go to [ASM05](https://github.com/Kin1009/ASM05) for more detail. This is integraded to this program.
