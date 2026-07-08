from abc import ABC, abstractmethod

class Drivable(ABC):

    @abstractmethod
    def drive(self):
        pass