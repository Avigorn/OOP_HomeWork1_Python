from VendingMachine import VendingMachine
import zope
from zope.interface import implementedBy
from zope.interface import providedBy


class BottleOfWaterVendingMachine():
    zope.interface.classImplements(VendingMachine)

    def __init__(self, products):
        self.bottleOfWatters = products

    def getBottleOfWatters(self):
        return self.bottleOfWatters

    def setBottleOfWatters(self, bottleOfWatters):
        self.bottleOfWatters = bottleOfWatters

    def getProduct(self, name):
        for item in self.bottleOfWatters:
            if item.getName() == name:
                return item
        return None

    def setProduct(self, name, volume):
        for bottle in self.bottleOfWatters:
            if bottle.getName() == name and bottle.getVolume() == volume:
                return bottle
        return None

    def addBottleOfWater(self, bottleOfWatter):
        self.bottleOfWatters.append(bottleOfWatter)
