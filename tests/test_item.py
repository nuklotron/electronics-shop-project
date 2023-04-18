"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def some_item():
    return Item("Alcatel", 1000, 5)


def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 5000


def test_apply_discount(some_item):
    assert some_item.apply_discount() == 1000.0
