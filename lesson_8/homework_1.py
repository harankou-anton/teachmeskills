class Car:
    brand = None
    model = None
    year = None
    speed = None

    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        self.speed -= 5

    def stop_car(self):
        self.speed = 0

    def show_speed(self):
        print(self.speed)

    def reverse_speed(self):
        self.speed = -self.speed
