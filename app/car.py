from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: 9.9

    def km_cost(self) -> float:
        return self.fuel_consumption / 100
