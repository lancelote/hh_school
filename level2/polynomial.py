# Дано выражение, содержащее скобки, операции сложения, вычитания, умножения,
# возведения в константную степень и одну переменную, например:
# (x - 5)(2x^3 + x(x^2 - 9)).
#
# Представьте это выражение в развёрнутом виде, например:
# 3x^4 - 15x^3 - 9x^2 + 45x

import argparse


def simplify(polynomial):
    """
    Simplifies polynomial

    :param polynomial: string representation of a complex polinomial
    :return: string representation of a simplified polinomial
    """
    return polynomial


def arg_parse():  # pragma: no cover
    """
    Parse console arguments
    """
    parser = argparse.ArgumentParser(description="Simplify polynomial")
    parser.add_argument("polynomial", action="store")
    args = parser.parse_args()
    return args.polynomial


def main():  # pragma: no cover
    """
    Prints the result to a console
    """
    polynomial = arg_parse()
    result = simplify(polynomial)
    print(result)

if __name__ == '__main__':  # pragma: no cover
    main()
