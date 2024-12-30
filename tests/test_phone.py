
import  pytest

from src.phone import Phone

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_item_creation(phone1):
    """Проверка создания экземпляра класса Phone"""
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

def test_repr(phone1):
    """Проверка представления экземпляра класса в виде строки"""
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str(phone1):
    """Проверка представления экземпляра класса в виде текстовой строки"""
    assert str(phone1) == 'iPhone 14'

def test_number_of_sim(phone1):
    """Проверка корректности количества SIM-карт"""
    if not type(phone1.number_of_sim) is int or int(phone1.number_of_sim) <= 0:
        with pytest.raises(ValueError):
            assert phone1.number_of_sim == 'Количество физических SIM-карт должно быть целым числом больше нуля.'
