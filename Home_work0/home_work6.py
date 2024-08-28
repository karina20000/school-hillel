from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self, model: str, year: int, price: float):
        self.model = model
        self.year = year
        self.price = price

    @abstractmethod
    def drive(self, distance: float):
        pass

    def __str__(self):
        return f"{self.model} ({self.year}), price: {self.price:.2f} грн"

    @property
    def status(self):
        if self.price > 10_000_000:
            return "elite class"
        elif 2_000_000 <= self.price <= 10_000_000:
            return "middle class"
        else:
            return "economy class"


class Car(BaseVehicle):
    def drive(self, distance: float):
        self.price -= 10 * distance
        if self.price < 0:
            self.price = 0


car1 = Car("Mercedes-Benz S-Class", 2022, 15_000000)
car2 = Car("Toyota Corolla", 2020, 1_500000)

print(car1)
print(car1.status)

car1.drive(100)
print(car1)

print(car2)
print(car2.status)

car2.drive(500)
print(car2)
