"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).

Переопределить магические методы сложения, вычитания, умножения на число.

Создать метод, который выводит на экран отформатированное время (HH:MM:SS).

Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.

Создать второй объект класса MyTime, найти разницу с первым, добавить к нему 7 часов и 45 минут, вывести на печать результат.

Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить новые атрибуты: day, month, year. “Исправить” все магические методы для этого класса.

Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""

from datetime import datetime

class MyTime:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.timestamp = seconds + minutes*60 + hours*60*60

    def __eq__(self, other) -> bool:
        return self.timestamp == other.timestamp

    def __ne__(self, other) -> bool:
        return self.timestamp != other.timestamp

    def __ge__(self, other) -> bool:
        return self.timestamp >= other.timestamp

    def __le__(self, other) -> bool:
        return self.timestamp <= other.timestamp

    def __gt__(self, other) -> bool:
        return self.timestamp > other.timestamp

    def __lt__(self, other) -> bool:
        return self.timestamp < other.timestamp


    def from_timestamp_to_hms(self, changed_timestamp) -> tuple:
        hours = changed_timestamp // (60 * 60)
        minutes = changed_timestamp % (60 * 60) // 60
        seconds = changed_timestamp % 60
        return hours, minutes, seconds

    def __add__(self, other):
        timestamp = self.timestamp + other
        return MyTime(*self.from_timestamp_to_hms(timestamp))

    def __sub__(self, other):
        timestamp = self.timestamp - other
        return MyTime(*self.from_timestamp_to_hms(timestamp))

    def __mul__(self, other):
        timestamp = self.timestamp * other
        return MyTime(*self.from_timestamp_to_hms(timestamp))

    def __str__(self):
        return f'Time - {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


class MyDateTime (MyTime):

    def __init__(self, day, month, year, hours, minutes, seconds):
        super().__init__(hours, minutes, seconds)
        self.day = day
        self.month = month
        self.year = year
        self.dt = datetime(self.year, self.month, self.day, self.hours, self.minutes, self.seconds)
        self.timestamp = datetime.timestamp(self.dt)



if __name__ == "__main__":
    my_time_1 = MyTime(1, 1, 31)
    my_time_2 = MyTime(0, 0, 31)
    # print(my_time_1 * 2)
    # print(my_time_1 - my_time_2.timestamp + MyTime(7, 45, 0).timestamp)
    my_new_time_1 = MyDateTime(20, 4, 1997, 12, 1, 35)
    my_new_time_1.get_day_time()
