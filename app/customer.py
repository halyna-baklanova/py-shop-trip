import math

from dataclasses import dataclass

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def distance(self, shop: Shop) -> int | float:
        return math.dist(self.location, shop.location) * 2

    def cost_distance(self, shop: Shop, fuel_price: float) -> int | float:
        return (self.distance(shop)
                * (self.car["fuel_consumption"] / 100)
                * fuel_price
                )

    def calculate_product_cost(
            self,
            shop: Shop,
            product: str,
            quantity: int
    ) -> float:
        if product in self.product_cart:
            return quantity * self.product_cart[product]

    def cost_products(self, shop: Shop) -> float:
        total_cost = 0
        for product, quantity in shop.products.items():
            total_cost += self.calculate_product_cost(shop, product, quantity)
        return total_cost

    def total_costs(self, shop: Shop, fuel_price: float) -> float:
        return round(
            self.cost_products(shop)
            + self.cost_distance(shop, fuel_price), 2
        )
