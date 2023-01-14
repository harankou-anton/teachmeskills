from homework_1 import Car
my_car = Car("Mercedes", "E500", 2000)

while my_car.speed != 100:
    my_car.increase_speed()
    print(f'Current speed: {my_car.speed}')
