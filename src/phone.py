from src.item import Item


class Phone(Item):
    """
    `Phone` содержит все атрибуты класса `Item` и дополнительно атрибут,
    содержащий количество поддерживаемых сим-карт
    """

    def __init__(self, name, price, quantity, number_of_sim: int):
        super().__init__(name, price, quantity)

        if number_of_sim > 0 and number_of_sim == int(number_of_sim):
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        if number_of_sim > 0 and number_of_sim == int(number_of_sim):
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("нельзя складывать Phone с другими типами кроме себя и Item")
        else:
            return self.quantity + other.quantity
