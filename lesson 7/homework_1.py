first_figure = [5, 7]
second_figure = [3, 6]


def check_figures():
    if abs(first_figure[0] - second_figure[0]) == 2 and abs(first_figure[1] - second_figure[1]) == 1:
        print('Yes')
    elif abs(first_figure[0] - second_figure[0]) == 1 and abs(first_figure[1] - second_figure[1]) == 2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    check_figures()