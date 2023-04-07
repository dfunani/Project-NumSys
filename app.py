from pyinputplus import inputChoice, inputNum, inputRegexStr
import re, sys

KEY = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
       '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def main(args):
    print(args)


def bin_dec(n: str):
    res = 0
    n.replace("0b", "")
    for i, val in enumerate(reversed(n)):
        res += (2 ** i) * int(val)
    return res


def bin_hex(n: str):
    res = ""
    for i in range(0, len(n), len(n) // 2):
        res += list(KEY.keys())[bin_dec(n[i: i + len(n) // 2])]
    return res


def hex_bin(n: str):
    res = ""
    n = n.replace("0x", "")
    for i in list(n):
        res += dec_bin(KEY[i])
    return res


def hex_dec(n: str):
    binary = hex_bin(n)
    return bin_dec(binary)


def dec_bin(n: int):
    res = ""
    for i in range(7 * ((n // 128) + 1), -1, -1):
        if n >= 2 ** i:
            res += "1"
            n -= 2 ** i
        else:
            res += "0"
    return (res[res.find("1"):])


def dec_hex(n: int):
    binary = dec_bin(n)
    return bin_hex(binary)


if __name__ == '__main__':
    PROCESSES = {
    'b-d': bin_dec,
    'b-h': bin_hex,
    'h-b': hex_bin,
    'h-d': hex_dec,
    'd-b': dec_bin,
    'd-h': dec_hex,
}
    choice = inputChoice(prompt="Conversion Type (eg: bin-dec or hex-bin):\n", choices=list(PROCESSES.keys()))
    if choice[0] == "d":
        value = inputNum(prompt='Provide the Decimal Value:\n')
    elif choice[0] == 'h':
        value = inputRegexStr(prompt="Provide the Hexadecimal Value:\n", allowRegexes=[re.compile(r"^0?x?[A-F0-9]+$")])
    else:
        value = inputRegexStr(prompt="Provide the Binary Value:\n", allowRegexes=[re.compile(r"^0?b?[0-1]+$")])
    main(PROCESSES[choice](value))
