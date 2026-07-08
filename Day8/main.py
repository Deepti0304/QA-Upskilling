from car import Car
from bike import Bike
from truck import Truck

vehicles = [
    Car("BMW"),
    Bike("Yamaha"),
    Truck("Volvo")
]

for vehicle in vehicles:
    vehicle.start()
    vehicle.drive()
    vehicle.stop()
    print("-" * 30)