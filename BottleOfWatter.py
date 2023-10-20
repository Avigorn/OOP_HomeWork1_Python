from Product import Product
from abc import ABC


class BottleOfWater(Product, ABC):
    def __init__(self, name, cost, volume):
        super().__init__(name, cost)
        self.volume = volume

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def __str__(self):
        return "BottleOfWater{" + \
            "name = " + super().get_name() + \
            ";volume = " + str(self.volume) + \
            ";cost = " + str(super().get_cost()) + \
            '}'
