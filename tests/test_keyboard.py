
import pytest

from src.keyboard import Keyboard

@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_item_creation(kb):
    """Проверка создания экземпляра класса Keyboard"""
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5

def test_repr(kb):
    """Проверка представления экземпляра класса в виде строки"""
    assert repr(kb) == 'Keyboard(Dark Project KD87A, 9600, 5)'

def test_str(kb):
    """Проверка представления экземпляра класса в виде текстовой строки"""
    assert str(kb) == 'Dark Project KD87A'

def test_change_lang(kb):
    """Проверка изменения языка клавиатуры"""
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"

def test_error_message(kb):
    """Проверка обработки ошибки при попытке установить неверное значение языка"""
    if kb.language == 'CH':
        with pytest.raises(ValueError):
            assert kb.language == "AttributeError: property 'language' of 'Keyboard' object has no setter"



