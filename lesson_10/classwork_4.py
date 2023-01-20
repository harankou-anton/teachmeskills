"""
Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + NxM.
"""


def get_sum(n: int, m: int):
    for number in range(1, m+1):
        yield int(str(n) * number)


def main():
    return sum(get_sum(2, 6))


if __name__ == "__main__":
    print(main())
