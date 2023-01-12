class Dog:
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

    def bark(self):
        print(f'{self.name} is barking')


if __name__ == "__main__":
    my_dog = Dog(2, 3, 'Jack', 1)
    my_dog.jump()
    my_dog.run()
    my_dog.bark()
    print(my_dog.name)
    print(my_dog.age)
    print(my_dog.weight)
    print(my_dog.height)

