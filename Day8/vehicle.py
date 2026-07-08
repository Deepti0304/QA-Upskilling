class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} Started")

    def stop(self):
        print(f"{self.brand} Stopped")