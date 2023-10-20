from typing import List


class BottleOfWater:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class BottleOfWaterVendingMachine:
    def __init__(self, bottles: List[BottleOfWater]):
        self.bottles = bottles

    def addBottleOfWater(self, bottle: BottleOfWater):
        self.bottles.append(bottle)

    def getProduct(self, name: str, quantity: int) -> str:
        for bottle in self.bottles:
            if bottle.name == name:
                if bottle.price >= quantity:
                    bottle.price -= quantity
                    return f"Product: {name}, Quantity: {quantity}, Price: {quantity * bottle.price}"
                else:
                    return "Not enough quantity available"
        return "Product not found"

    def getBottleOfWaters(self):
        return self.bottles()


class HotDrink:
    def __init__(self, name: str, volume: int, temperature: int):
        self.name = name
        self.volume = volume
        self.temperature = temperature


class HotDrinkVendingMachine:
    def __init__(self, drink: List[HotDrink]):
        self.drink = drink

    def add_hot_drink(self, drink: HotDrink):
        self.drink.append(drink)

    def get_drink(self, name: str, quantity: int, temperature: int) -> str:
        for drink in self.drink:
            if drink.name == name:
                return f"Product: {name}, Quantity: {quantity}, Temperature: {temperature}"
        return "Product not found"

    def get_hot_drink(self):
        return self.drink()


b1 = BottleOfWater("Pepsi", 1, 1)
b2 = BottleOfWater("CC", 2, 2)
b3 = BottleOfWater("Aqua", 4, 3)
b4 = BottleOfWater("Spiritus", 123, 1)
a1 = HotDrink("Coffee", 1, 60)
a2 = HotDrink("Tea", 2, 80)

vendingMachine = BottleOfWaterVendingMachine([])
vendingMachine.addBottleOfWater(b1)
vendingMachine.addBottleOfWater(b2)
vendingMachine.addBottleOfWater(b3)
vendingMachine.addBottleOfWater(b4)

hot_vending_machine = HotDrinkVendingMachine([])
hot_vending_machine.add_hot_drink(a1)
hot_vending_machine.add_hot_drink(a2)

print(hot_vending_machine.get_drink("Coffee", 1, 60))
print(hot_vending_machine.get_drink("Tea", 2, 80))

print(vendingMachine.getProduct("Spiritus", 5))
print(vendingMachine.getProduct("CC", 100))
# for b in vendingMachine.getBottleOfWaters():
#     print(b)
