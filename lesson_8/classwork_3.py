class Cat:
    height = None
    weight = None
    name = None
    age = None

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f'{self.name} is jumping')

    def run(self):
        print(f'{self.name} is running')

    def meow(self):
        print(f'{self.name} is meowing')

    def change_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    my_cat = Cat(2, 3, 'Tom', 1)
    print(my_cat.name)
    my_cat.change_name('Jerry')
    print(my_cat.name)