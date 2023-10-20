import zope
import HotVendingMachine


class HotDrinkVendingMachine:
    zope.interface.classImplements(HotVendingMachine)

    def __init__(self, drink):
        self.hot_drink = drink

    def get_hot_drink(self):
        return self.hot_drink

    def set_hot_drink(self, hot_drink):
        self.hot_drink = hot_drink

    def get_drink(self, name):
        for item in self.hot_drink:
            if item.getName() == name:
                return item
        return None

    def set_drink(self, name, temperature):
        for drink in self.hot_drink:
            if drink.getName() == name and drink.get_temperature() == temperature:
                return drink
        return None

    def add_hot_drink(self, hot_dink):
        self.hot_drink.append(hot_dink)
