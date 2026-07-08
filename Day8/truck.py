from vehicle import Vehicle
from drivable import Drivable

class Truck(Vehicle, Drivable):

    def drive(self):
        print(f"{self.brand} Truck Moving")