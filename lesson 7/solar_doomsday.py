import math


def get_length_width(sq):
    length = 0
    width = 0
    for i in range(math.floor(sq**0.5), 0, -1):
        if sq % i == 0:
            length, width = i, int(sq/i)
            break
    return length, width


def get_squares(sq):
    list_of_squares = []
    x, y = get_length_width(sq)
    while sum(list_of_squares) != sq:
        if x == y:
            list_of_squares.append(x**2)
        elif x == 1 and y != 1:
            list_of_squares = list_of_squares + [x]*y
        elif x != 1 and y == 1:
            list_of_squares = list_of_squares + [y]*x
        elif x < y:
            list_of_squares.append(x**2)
            y -= x
        elif y < x:
            list_of_squares.append(y**2)
            x -= y
    return list_of_squares


if __name__ == "__main__":
    print(get_squares(85))
