from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, company, model, year_release):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = 0
        self.speed = 0

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass

class Car(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release)
        self.num_wheels = 4

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

class Motorcycle(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release)
        self.num_wheels = 2

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0
