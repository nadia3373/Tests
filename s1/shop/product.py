class Product:
    def __init__(self, cost: int, title: str):
        self._cost = cost
        self._title = title

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._cost = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
