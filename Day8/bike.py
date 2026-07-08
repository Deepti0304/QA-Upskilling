from vehicle import Vehicle
from drivable import Drivable

class Bike(Vehicle, Drivable):

    def drive(self):
        print(f"{self.brand} Bike Riding")