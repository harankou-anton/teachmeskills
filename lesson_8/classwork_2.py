from classwork_4 import Animal


class Dog(Animal):

    def bark(self):
        print(f'{self.name} is barking')


if __name__ == "__main__":
    my_dog = Dog(2, 3, 'Jerry', 1)
    print(my_dog.name)
    my_dog.bark()
    my_dog.jump()
