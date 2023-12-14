#Assignment 9
#Fundamentals_of_Object-Oriented_Programming

import random

#1
class Car:
    def __init__(self, regis_num, max_speed, current_speed=0, travelled_distance=0):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance


car1 = Car("ABC-123","142 km/h" )
print(f"Registration number: {car1.regis_num}\nMaximum speed: {car1.max_speed}\n"
      f"Current speed: {car1.current_speed}\nTravelled distance: {car1.travelled_distance}")

#2
class Car:
    current_speed = 0
    def __init__(self, regis_num, max_speed, travelled_distance=0):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.travelled_distance = travelled_distance

    def accelerate(self,new_speed):
        self.new_speed = new_speed
        Car.current_speed = Car.current_speed + self.new_speed
        # print(f"Add {self.new_speed} Current {Car.current_speed} ")
        if Car.current_speed < 0:
           Car.current_speed = 0
           print(f"Emergency brake {self.new_speed} km/h\n"
                 f"Current Speed: {Car.current_speed} ")
        else:
            print(f"+{self.new_speed} km/h Current Speed: {Car.current_speed} ")

        if Car.current_speed >= self.max_speed:
            Car.current_speed = self.max_speed
            return print(f"Your current speed is the maximum {self.max_speed} km/h")

car1 = Car("ABC-123",142 )
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)

#3
class Car:
    current_speed = 60
    def __init__(self, regis_num, max_speed, travelled_distance=0):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.travelled_distance = travelled_distance

    def accelerate(self,new_speed):
        self.new_speed = new_speed
        Car.current_speed = Car.current_speed + self.new_speed
        # print(f"Add {self.new_speed} Current {Car.current_speed} ")
        if Car.current_speed < 0:
           Car.current_speed = 0
           print(f"Emergency brake {self.new_speed} km/h\n"
                 f"Current Speed: {Car.current_speed} ")
        else:
            print(f"+{self.new_speed} km/h Current Speed: {Car.current_speed} ")

        if Car.current_speed >= self.max_speed:
            Car.current_speed = 0
            return print(f"Your current speed is over the maximum {self.max_speed} km/h")

    def drive(self,hours):
        self.hours = hours
        self.new_distance = Car.current_speed * self.hours
        self.travelled_distance = self.travelled_distance + self.new_distance
        print(f"Drive for {self.hours} hours\n"
              f"Current speed is {Car.current_speed} km/h\n"
              f"Travelled distance is {self.travelled_distance} km.")

car1 = Car("ABC-123",142, 2000)
car1.drive(1.5)

#4
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.distance_travelled = 0
        self.speed = 0

    def accelerate(self):
        self.speed += random.randint(-10, 15)
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed

    def drive(self):
        self.distance_travelled += self.speed

# Creating a list of 10 cars
cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car = Car(registration_number, max_speed)
    cars.append(car)

# Race simulation
while True:
    for car in cars:
        car.accelerate()
        car.drive()

    # Checking if any car has traveled 10,000 kilometers
    if any(car.distance_travelled >= 10000 for car in cars):
        break

print(f"{'Registration Number':<20} {'Max Speed (km/h)':<20} {'Distance Travelled (km)':<25}")
for car in cars:
    print(f"{car.registration_number:<20} {car.max_speed:<20} {car.distance_travelled:<25}")




