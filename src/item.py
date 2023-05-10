from csv import DictReader
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv_
        """
        path = os.path.join("../src/", "items.csv")
        with open(path, encoding="UTF-8") as file:
            reader = DictReader(file)
            for row in reader:
                item = (cls(row["name"], row["price"], row["quantity"]))
            return item

    @staticmethod
    def string_to_number(num):
        """
        Статический метод, возвращающий число из числа-строки
        """
        num = float(num)
        num = int(num)
        return num

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Нельзя складывать Phone с другими типами кроме себя и Item")

        else:
            return self.quantity + other.quantity
