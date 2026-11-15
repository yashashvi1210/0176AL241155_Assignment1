# Multilevel inheritance: Vehicle -> Car -> ElectricCar

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats

    def drive(self):
        print(f"Driving a {self.brand} car with {self.seats} seats.")

class ElectricCar(Car):
    def __init__(self, brand, seats, battery_kwh):
        super().__init__(brand, seats)
        self.battery_kwh = battery_kwh

    def charge(self):
        print(f"Charging the {self.battery_kwh} kWh battery.")

tesla = ElectricCar("Tesla", 5, 75)
tesla.start()
tesla.drive()
tesla.charge()
