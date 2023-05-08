import pytest
from src.keyboard import KeyBoard


def test_keyboard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_language():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    with pytest.raises(AttributeError, match="property 'language' of 'KeyBoard' object has no setter"):
        kb.language = "CH"
        assert kb.language == AttributeError


test_keyboard()
test_language()
