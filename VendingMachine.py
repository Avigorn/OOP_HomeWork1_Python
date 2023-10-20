from Product import Product
from typing import List
import zope.interface


class VendingMachine(zope.interface.Interface):
    def getProduct(self, name: str, volume: float) -> Product:
        pass
