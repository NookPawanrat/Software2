#Assignment 10
#Association

#1

class Elevator():
    floorsNow = 0
    def __init__(self,bottom_fl,top_fl):
        self.bottom_fl = bottom_fl
        self.top_fl = top_fl
        Elevator.floorsNow = bottom_fl

    def go_to_floor(self,floorToGo):
        self.floor = floorToGo
        print(f"You're in floor {self.bottom_fl} and want to go to floor {self.floor}")
        while floorToGo != Elevator.floorsNow:
            self.floor_up()
        print(f"You are at {floorToGo} floor now. The elevator will go down")
        self.floor_down()

    def floor_up(self):
        Elevator.floorsNow += 1
        print(f"Elevator is going up, Now floors {Elevator.floorsNow} ")

    def floor_down(self):
        while Elevator.floorsNow != self.bottom_fl:
            Elevator.floorsNow -= 1
            print(f"Elevator is going down, Now floors {Elevator.floorsNow} ")


elevator = Elevator(1,12)
elevator.go_to_floor(8)

#2
class Elevator():
    floorsNow = 0
    def __init__(self,bottom_fl,top_fl):
        self.bottom_fl = bottom_fl
        self.top_fl = top_fl
        Elevator.floorsNow = bottom_fl

    def go_to_floor(self,floorToGo):
        self.floor = floorToGo
        print(f"You're in bottom floor {Elevator.floorsNow} and want to go to floor {self.floor}")
        while floorToGo != Elevator.floorsNow:
            self.floor_up()
        print(f"You are at {floorToGo} floor now. The elevator will go down")
        self.floor_down()

    def floor_up(self):
        Elevator.floorsNow += 1
        print(f"Elevator is going up, Now floors {Elevator.floorsNow} ")

    def floor_down(self):
        while Elevator.floorsNow != self.bottom_fl:
            Elevator.floorsNow -= 1
            print(f"Elevator is going down, Now floors {Elevator.floorsNow} ")

class Building():
    def __init__(self,num_elevator,bottom_fl,top_fl):
        self.num_elevator = num_elevator
        self.bottom_fl = bottom_fl
        self.top = top_fl
        self.elevator = []
        for i in range(num_elevator):
            self.elevator.append(Elevator(bottom_fl,top_fl))

    def run_elevator(self,elevator_num,des_fl):
        elevator = self.elevator[elevator_num-1]
        print(f"Run Elevator {elevator_num} to floor {des_fl}")
        elevator.go_to_floor(des_fl)

#Main
building = Building(1,3,15)
building.run_elevator(1,10)

#3
class Elevator():
    floorsNow = 0
    def __init__(self,bottom_fl,top_fl):
        self.bottom_fl = bottom_fl
        self.top_fl = top_fl
        Elevator.floorsNow = bottom_fl

    def go_to_floor(self,floorToGo):
        self.floor = floorToGo
        if floorToGo == self.bottom_fl:
            print(f"Fire Alarm Floor! Elevator Number  now is {self.floorsNow}")
        else:
            print(f"You're in bottom floor {Elevator.floorsNow} and want to go to floor {self.floor}")
            while floorToGo != Elevator.floorsNow:
                self.floor_up()
            print(f"You are at {floorToGo} floor now. The elevator will go down")
            self.floor_down()

    def floor_up(self):
        Elevator.floorsNow += 1
        print(f"Elevator is going up, Now floors {Elevator.floorsNow} ")

    def floor_down(self):
        while Elevator.floorsNow != self.bottom_fl:
            Elevator.floorsNow -= 1
            print(f"Elevator is going down, Now floors {Elevator.floorsNow} ")

class Building():
    def __init__(self,num_elevator,bottom_fl,top_fl):
        self.num_elevator = num_elevator
        self.bottom_fl = bottom_fl
        self.top = top_fl
        self.elevator = []
        for i in range(num_elevator):
            self.elevator.append(Elevator(bottom_fl,top_fl))

    def run_elevator(self,elevator_num,des_fl):
        self.des_fl = des_fl
        elevator = self.elevator[elevator_num-1]
        print(f"Run Elevator {elevator_num} to floor {des_fl}")
        elevator.go_to_floor(self.des_fl)

    def fire_alarm(self):
        for i in self.elevator:
            i.go_to_floor(self.bottom_fl)

#Main
building = Building(5,3,15)
building.run_elevator(1,10)
building.fire_alarm()

#4

import random
class Car:
    def __init__(self, regis_num, max_speed):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.travelled_distance = 0
        self.current_speed = 0

    def accelerate(self,speed_change):
        if speed_change >= 0:
            self.current_speed = min(self.current_speed + speed_change, self.max_speed)
        else:
            self.current_speed = max(self.current_speed + speed_change, 0)

    def drive(self,hours):
        self.travelled_distance += self.current_speed * hours


    def printInfo(self):
        print(f"Car number: {self.regis_num}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Current Speed:{self.current_speed} km/h")
        print(f"Travelled_distance: {self.travelled_distance} km.\n")

class Race:
    def __init__(self,name,distance,cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10,15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration Number':<20} {'Maximum Speed (km/h)':<20} {'Travelled Distance (km)':<25}")
        for car in self.cars:
            print(f"{car.regis_num:<20} {car.max_speed:<20} {car.travelled_distance:<25}")
        print("\n")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

cars_for_race = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car = Car(registration_number, max_speed)
    cars_for_race.append(car)


grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars_for_race)
hours_elapsed = 0
while not grand_demolition_derby.race_finished():
    if hours_elapsed % 10 == 0:
        print(f"Race status after {hours_elapsed} hours:")
        grand_demolition_derby.print_status()
    grand_demolition_derby.hour_passes()
    hours_elapsed += 1


print(f"Final race status after {hours_elapsed} hours:")
grand_demolition_derby.print_status()