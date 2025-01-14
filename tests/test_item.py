"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def some_item():
    return Item("Alcatel", 1000, 5)


def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 5000


def test_apply_discount(some_item):
    assert some_item.apply_discount() == 1000.0


def test_name(some_item):
    assert some_item.name == "Alcatel"
    with pytest.raises(Exception, match="Длина наименования товара превышает 10 символов."):
        some_item.name = "SuperAlcatel"
        assert some_item.name == Exception


def test_string_to_number():
    num = "223.2342"
    assert Item.string_to_number(num) == 223


def test_instantiate_from_csv():
    # Item.instantiate_from_csv()
    # assert len(Item.all) == 10
    with pytest.raises(Exception, match="Файл item.csv поврежден"):

        assert Item.instantiate_from_csv() == Exception


def test_repr(some_item):
    assert repr(some_item) == "Item('Alcatel', 1000, 5)"


def test_str(some_item):
    assert str(some_item) == "Alcatel"


def test_add():
    phone1 = Phone("Alcatel", 1200, 2, 2)
    phone2 = Item("Siemens", 1000, 5)
    assert phone1 + phone2 == 7
    assert phone1 + phone1 == 4
