"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture
def item1():
     return Item(name="Смартфон", price=10000, quantity=20)

@pytest.fixture
def item2():
     return Item(name="Ноутбук", price=20000, quantity=5)

@pytest.fixture
def load_csv():
     return Item.instantiate_from_csv('src/item.py')

@pytest.fixture(autouse=True)
def clear_items():
    yield
    Item.all.clear()

def test_init_homework_1(item1, item2):
     """Тестирование инициализации объекта класса."""
     assert item1.name == "Смартфон"
     assert item1.price == 10000
     assert item1.quantity == 20

     assert item2.name == "Ноутбук"
     assert item2.price == 20000
     assert item2.quantity == 5

def test_calculate_total_price(item1, item2):
     """Проверка суммы общей стоимости конкретного товара в магазине"""
     assert item1.calculate_total_price() == 200000
     assert item2.calculate_total_price() == 100000

def test_apply_discount(item1, item2):
     """Проверка установленной скидки на конкретный товар"""
     Item.pay_rate = 0.8
     item1.apply_discount()
     assert item1.price == 8000.0
     assert item2.price == 20000

def test_all(item1, item2):
     """Проверка количества экземпляров класса в атрибуте all"""
     assert len(Item.all) == 2
     assert item1 in Item.all
     assert item2 in Item.all

def test_character_length(load_csv):
     """Проверяет что бы длина наименования товара была не больше 10 символов"""
     load_csv = Item.all[0]
     assert load_csv.name == load_csv.name[:10]

     load_csv = Item.all[1]
     assert load_csv.name == load_csv.name[:10]

     load_csv = Item.all[2]
     assert load_csv.name == load_csv.name[:10]

     load_csv = Item.all[3]
     assert load_csv.name == load_csv.name[:10]

     load_csv = Item.all[4]
     assert load_csv.name == load_csv.name[:10]

def test_name_setter(item2):
     if len(item2.name) > 10:
          with pytest.raises(ValueError):
               assert item2.name == 'СуперСмартфон'

def test_all_csv(load_csv):
     """Проверка того что все данные в csv файле внесены в список all"""
     assert len(Item.all) == 5

def test_string_to_number():
     """Проверка того что при получении str будет возвращаться int"""
     assert Item.string_to_number('5') == 5
     assert Item.string_to_number('5.0') == 5
     assert Item.string_to_number('5.5') == 5

def test_homework_3():
     """Тестирование инициализации объекта"""
     item1 = Item("Смартфон", 10000, 20)

     assert repr(item1) == "Item('Смартфон', 10000, 20)"
     assert str(item1) == 'Смартфон'

def test_homework_4():
     phone1 = Phone("iPhone 14", 120_000, 5, 2)
     item1 = Item("Смартфон", 10000, 20)

     assert str(phone1) == 'iPhone 14'
     assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
     assert phone1.number_of_sim == 2

     assert item1 + phone1 == 25
     assert phone1 + phone1 == 10

     if phone1.number_of_sim <= 0:
          with pytest.raises(ValueError):
               print('Количество физических SIM-карт должно быть целым числом больше нуля.')
     else:
          assert phone1.number_of_sim > 0