from DATA.classdata import Alu
from DATA.Number import maps


def main():
    x, y = bin(int(input())).split('0b'), bin(int(input())).split('0b')
    x, y = x[1], y[1]
    al = Alu.s_xor(x, y)
    res = int(str(maps(al)), 2)
    print(res)
