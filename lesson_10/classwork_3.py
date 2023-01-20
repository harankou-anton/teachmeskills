"""
Создать генератор и/или итератор простой геометрической прогрессии.
"""


def generator(start, stop, step):
    el = start
    while el <= stop:
        yield el
        el *= step


my_gen = generator(2, 20, 2)
for el in my_gen:
    print(el)


class SimpleIterator:
    def __init__(self, start, stop, step):
        self.start, self.stop, self.step = start, stop, step
        self.counter = self.start

    def __next__(self):
        if self.counter < self.stop:
            self.counter *= self.step
            return 1
        else:
            raise StopIteration


my_iter = SimpleIterator(2, 20, 3)
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
