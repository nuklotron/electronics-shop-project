"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.phone import Phone, Item


def test_repr():
    item1 = Phone("Alcatel", 1000, 5, 2)
    print(repr(item1))
    assert repr(item1) == "Phone('Alcatel', 1000, 5, 2)"


def test_str():
    item1 = Phone("Alcatel", 1000, 5, 2)
    assert str(item1) == "Alcatel"


def test_number_of_sim():
    item1 = Phone("Alcatel", 1000, 5, 1)
    assert item1.number_of_sim == 1
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        item1.number_of_sim = 2.1
        assert item1.number_of_sim == ValueError
        item1.number_of_sim = -1
        assert item1.number_of_sim == ValueError


def test_add():
    item1 = Item("Alcatel", 1000, 5)
    phone1 = Phone("Siemens", 1000, 5, 1)
    with pytest.raises(ValueError, match="Нельзя складывать Phone с другими типами кроме себя и Item"):
        assert item1 + phone1 == 10
        assert item1 + item1 == 10
        assert item1 + 10 == ValueError
