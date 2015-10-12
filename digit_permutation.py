# Число 125874 и результат умножения его на 2 — 251748 можно получить друг из
# друга перестановкой цифр.
#
# Найдите наименьшее положительное натуральное x такое, что числа 4*x, 5*x
# можно получить друг из друга перестановкой цифр.

import argparse


def solve(i, j):
    number = 1
    while True:
        number_ix = number*i
        number_jx = number*j
        if sorted(str(number_ix)) == sorted(str(number_jx)):
            return number, number_ix, number_jx
        number += 1


def arg_parse():  # pragma: no cover
    """
    Parse console arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("i", action="store")
    parser.add_argument("j", action="store")
    args = parser.parse_args()
    return int(args.i), int(args.j)


def main():  # pragma: no cover
    """
    Prints the result to a console
    """
    i, j = arg_parse()
    number, number_ix, number_jx = solve(i, j)
    print('Наименьшее положительное натуральное число: %s' % number)
    print('x = %s, y = %s' % (number_ix, number_jx,))

if __name__ == '__main__':  # pragma: no cover
    main()
