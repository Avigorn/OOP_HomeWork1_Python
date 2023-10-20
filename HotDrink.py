from abc import ABC
from Product import Product
from BottleOfWatter import BottleOfWater


class HotDrink(Product, ABC, BottleOfWater):
    def __init__(self, name, volume: int, temperature: int):
        super().__init__(name, volume)
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return "HotDrink{" + \
            "name = " + super().get_name() + \
            ";volume = " + str(super().get_volume() + \
                               ";temperature = " + str(self.get_temperature()) + \
                               '}')
