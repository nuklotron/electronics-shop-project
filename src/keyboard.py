from src.item import Item


class MixinLanguage:
    """
    Отдельный классе-миксин,
    который “подмешивается” в цепочку наследования класса `Keyboard`
    """
    def __init__(self):
        self.__language = "EN"

    def change_lang(self):

        for v in ["RU", "EN"]:

            if self.__language != v:
                self.__language = v
                break

        return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLanguage):
    """
    Класс `Keyboard` для товара “клавиатура”
    """

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
