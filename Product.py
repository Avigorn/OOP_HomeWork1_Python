from abc import ABCMeta, abstractmethod, abstractproperty


class Product:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    @abstractmethod
    def __str__(self):
        return "Product{" + "name='" + self.name + '\'' + ", cost=" + str(self.cost) + '}'
