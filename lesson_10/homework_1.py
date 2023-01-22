"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3.
На стержень 1 надета пирамидка из n дисков различного диаметра в порядке возрастания диаметра.
Диски можно перекладывать с одного стержня на другой строго по одному,
при этом диск нельзя класть на диск меньшего диаметра.
Необходимо переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает последовательность перекладываний,
необходимую для решения головоломки.
"""


def hanoi_tower(disk_numbers: int, stick_from: int = 1, stick_to: int = 3):
    if disk_numbers == 1:
        print(f'Move disk {disk_numbers} from stick {stick_from} to stick {stick_to}')
    else:
        temp_stick = 6 - stick_from - stick_to
        hanoi_tower(disk_numbers-1, stick_from, temp_stick)
        print(f'Move disk {disk_numbers} from stick {stick_from} to stick {stick_to}')
        hanoi_tower(disk_numbers - 1, temp_stick, stick_to)


hanoi_tower(4)
