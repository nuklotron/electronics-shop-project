"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.phone import Phone


def test_repr():
    item1 = Phone("Alcatel", 1000, 5, 2)
    print(repr(item1))
    assert repr(item1) == "Phone('Alcatel', 1000, 5, 2)"


def test_str():
    item1 = Phone("Alcatel", 1000, 5, 2)
    assert str(item1) == "Alcatel"


def test_number_of_sim():
    item1 = Phone("Alcatel", 1000, 5, 2)
    assert item1.number_of_sim == 2
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        item1.number_of_sim = 2.1
        assert item1.number_of_sim == ValueError


test_number_of_sim()
