# Число 125874 и результат умножения его на 2 — 251748 можно получить друг из
# друга перестановкой цифр.
#
# Найдите наименьшее положительное натуральное x такое, что числа 4*x, 5*x
# можно получить друг из друга перестановкой цифр.


def is_palindrome(number4x, number5x):
    return sorted(str(number4x)) == sorted(str(number5x))


def solve():
    number = 1
    while True:
        number4x = number*4
        number5x = number*5
        if is_palindrome(number4x, number5x):
            return number, number4x, number5x
        number += 1


def main():  # pragma: no cover
    """
    Prints the result to a console
    """
    print(solve())

if __name__ == '__main__':  # pragma: no cover
    main()
