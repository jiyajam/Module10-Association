########################1

class Elevator:
    def __init__(self,bottom_floor,top_floor):

        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.floor_now = bottom_floor


    def go_to_floor(self,floor_needed):
        if floor_needed >self.top_floor or floor_needed <self.bottom_floor:
            return f"This floor does not exist."

        while self.floor_now < floor_needed:
            self.floor_up()
        while self.floor_now > floor_needed:
            self.floor_down()

        return f"This floor is available for elevation and can take you to the {self.floor_now}th floor."
    def floor_up(self):
        if self.floor_now < self.top_floor:
            self.floor_now += 1
            print (f"you have reached {self.floor_now}")

    def floor_down(self):
        if self.floor_now > self.bottom_floor:
            self.floor_now -= 1
            print (f"you have reached {self.floor_now}")

h= Elevator(1,10)
print(h.go_to_floor(5))
print(h.go_to_floor(1))
print(h.go_to_floor(50))


###########################2

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.floor_now = bottom_floor

    def go_to_floor(self, floor_needed):
        if floor_needed > self.top_floor or floor_needed < self.bottom_floor:
            return f"This floor does not exist."

        while self.floor_now < floor_needed:
            self.floor_up()
        while self.floor_now > floor_needed:
            self.floor_down()

        return f"Elevator is now at floor {self.floor_now}."

    def floor_up(self):
        if self.floor_now < self.top_floor:
            self.floor_now += 1
            print(f"You have reached floor {self.floor_now}")

    def floor_down(self):
        if self.floor_now > self.bottom_floor:
            self.floor_now -= 1
            print(f"You have reached floor {self.floor_now}")


class Building:
    def __init__(self, bottom_floor, top_floor, no_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = {}


        for i in range(no_of_elevators):
            self.elevators[i+1] = Elevator(bottom_floor, top_floor)

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number in self.elevators:
            elevator = self.elevators[elevator_number]
            print(f"Running elevator {elevator_number} to floor {destination_floor}")
            result = elevator.go_to_floor(destination_floor)
            print(result)
        else:
            print("The elevator number is unavailable.")



building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 5)
building.run_elevator(5, 3)

##########################3
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.floor_now = bottom_floor

    def go_to_floor(self, floor_needed):
        if floor_needed > self.top_floor or floor_needed < self.bottom_floor:
            return f"This floor does not exist."

        while self.floor_now < floor_needed:
            self.floor_now += 1
            print(f"You have reached floor {self.floor_now}")

        while self.floor_now > floor_needed:
            self.floor_now -= 1
            print(f"You have reached floor {self.floor_now}")

        return f"Elevator is now at floor {self.floor_now}."

    def current_location(self):
        return f"The elevator is currently at floor {self.floor_now}"


class Building:
    def __init__(self, bottom_floor, top_floor, no_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = {}

        for i in range(no_of_elevators):
            self.elevators[i] = Elevator(bottom_floor, top_floor)

    def run_elevator(self, elevator_number, destination_floor):
        # Ensure the elevator_number exists
        if elevator_number in self.elevators:
            elevator = self.elevators[elevator_number]
            print(f"Running Elevator {elevator_number + 1} to floor {destination_floor}")
            result = elevator.go_to_floor(destination_floor)
            print(result)
        else:
            print("The elevator number is unavailable.")

    def fire_alarm(self):
        print("Fire Alarm has been activated! Moving all elevators to the bottom floor.")
        for elevator_number, elevator in self.elevators.items():
            print(f"Moving Elevator {elevator_number + 1} to the bottom floor.")
            elevator.go_to_floor(self.bottom_floor)

building = Building(bottom_floor=1, top_floor=10, no_of_elevators=2)

#
building.run_elevator(0, 7)

elevator1 = building.elevators[0]

elevator2 = building.elevators[1]


building.run_elevator(1, 3)

building.fire_alarm()

for elevator_number in building.elevators:
    elevator = building.elevators[elevator_number]
    print(f"Elevator {elevator_number + 1} current location: {elevator.current_location()}")


#####################4
import random

class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance = 0

    def drive(self):
        self.speed += random.randint(-10, 20)
        if self.speed < 0:
            self.speed = 0
        self.distance += self.speed
    def __str__(self):
        return f"{self.name}: {self.distance} km"


class Race:
    def __init__(self, name, total_distance, cars):
        self.name = name
        self.total_distance = total_distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.drive()

    def print_status(self):
        print(f"{self.name} - Race Status:")
        for car in self.cars:
            print(car)

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.total_distance:
                return True
        return False

cars = [Car(f"Car {i+1}") for i in range(10)]

race = Race("Grand Demolition Derby", 8000, cars)


hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()

race.print_status()
for car in race.cars:
    if car.distance >= race.total_distance:
        print(f"{car.name} wins the race after {hours} hours!")
        break


