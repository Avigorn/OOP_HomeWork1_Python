from Product import Product
from typing import List
import zope.interface


class HotVendingMachine(zope.interface.Interface):
    def getProduct(self, name: str, volume: float, temperature: int) -> Product:
        pass
