from vehicle import Vehicle
from drivable import Drivable

class Car(Vehicle, Drivable):

    def drive(self):
        print(f"{self.brand} Car Driving")