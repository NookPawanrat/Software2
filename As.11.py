#Assignment 10
#Inheritance

#1
class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name,autor,page_count):
        self.autor = autor
        self.page_count = page_count
        super().__init__(name)
    def print_Info(self):
        print(f"Book Name {self.name}")
        print(f"Autor: {self.autor}")
        print(f"Page Count: {self.page_count} pages")

class Magazine(Publication):
    def __init__(self,name,chief_name):
        self.chief_name = chief_name
        super().__init__(name)

    def print_Info(self):
        print(f"Magazine Name {self.name}")
        print(f"Chief Name: {self.chief_name}")


magazine1 = Magazine("Donald Duck","Aki Hyyppä")
book1 = Book("Compartment No.6","Rosa Liksom",192)

magazine1.print_Info()
book1.print_Info()

#2

import random
class Car:
    def __init__(self, regis_num, max_speed):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.travelled_distance = 0
        self.current_speed = 0

    def accelerate(self):
        self.current_speed += random.randint(-10,50)
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.hours = hours
        self.travelled_distance += self.current_speed * self.hours

    def printInfo(self):
        print(f"Car number: {self.regis_num}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled_distance: {self.travelled_distance} km.")
        if self.regis_num == "ABC-15" :
            print((f"Battery: {self.battery}\n"))
        else:
            print((f"Volume of the tank: {self.liters}\n"))

class ElectricCar(Car):
    def __init__(self,regis_num, max_speed,battery):
        super().__init__(regis_num, max_speed)
        self.battery = battery
    def info_ElectricCar(self):
        super().printInfo()
        print(f"Capacity of the battery: {self.battery} kWh.\n")
class GasolineCar(Car):
    def __init__(self,regis_num, max_speed,liters):
        super().__init__(regis_num, max_speed)
        self.liters = liters
    def info_GasolineCar(self):
        super().printInfo()
        print(f"Volume of the tank: {self.liters} l.\n")


car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = GasolineCar("ACD-123", 165, 32.3)
car1.accelerate()
car2.accelerate()

car1.drive(3)
car2.drive(3)

car1.info_ElectricCar()
car2.info_GasolineCar()