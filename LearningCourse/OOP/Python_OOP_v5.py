#Multiple inheritance : Method Resolution Order(MRO)
class Car:
    def start(self):
        print("Start the car")

    def go(self):
        print("Going")

class Flyable:
    def start(self):
        print("Starting the flyable object")

    def fly(self):
        print("Flying")

class FlyingCar(Flyable, Car): #if order would have been(Car, Flyable), then o/p: Start the car
    def start(self):
        super().start()

if __name__ == '__main__':
    car = FlyingCar()
    car.start() #o/p:Starting the flyable object

# -----------------------------------------------------
#Multiple inheritance and super
class Car:
    def __init__(self, door, wheel):
        self.door = door
        self.wheel = wheel

    def start(self):
        print('Start the Car')

    def go(self):
        print('Going')

class Flyable:
    def __init__(self, wing):
        print('Calling init of flyable class')
        self.wing = wing

    def start(self):
        print('Start the Flyable object')

    def fly(self):
        print('Flying')

class FlyingCar(Flyable, Car):
    def __init__(self, door, wheel, wing):
        super().__init__(wing)
        self.door = door
        self.wheel = wheel

    def start(self):
        super().start()

if __name__ == '__main__':
    car = FlyingCar('door','wheel','wing')
    car.start() #o/p:Starting the flyable object