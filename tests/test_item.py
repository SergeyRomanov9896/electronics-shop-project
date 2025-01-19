
import os

import pytest
import csv

from src.item import Item
from src.item import InstantiateCSVError
from src.phone import Phone

@pytest.fixture
def item1():
     return Item(name="Смартфон", price=10000, quantity=20)

@pytest.fixture
def item2():
     return Item(name="Ноутбук", price=20000, quantity=5)

@pytest.fixture
def item3():
     return Item(name='Телефон', price=10000, quantity=5)

@pytest.fixture
def phone1():
     return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def csv_reader():
    base_path = os.path.join(os.path.dirname(__file__), '..','src', 'items.csv')

    with open(base_path, encoding="windows-1251") as file_csv:
        yield file_csv

@pytest.fixture(autouse=True)
def clear_items():
    yield
    Item.all.clear()

def test_item_creation(item1, item2, item3):
     """Проверка создания экземпляров класса Item"""
     assert item1.name == "Смартфон"
     assert item1.price == 10000
     assert item1.quantity == 20

     assert item2.name == "Ноутбук"
     assert item2.price == 20000
     assert item2.quantity == 5

     assert item3.name == "Телефон"
     assert item3.price == 10000
     assert item3.quantity == 5

def test_repr(item1, item2, item3):
     """Проверка представления экземпляра класса в виде строки"""
     assert repr(item1) == "Item('Смартфон', 10000, 20)"
     assert repr(item2) == "Item('Ноутбук', 20000, 5)"
     assert repr(item3) == "Item('Телефон', 10000, 5)"

def test_str(item1, item2, item3):
     """Проверка представления экземпляра класса в виде текстовой строки"""
     assert str(item1) == 'Смартфон'
     assert str(item2) == 'Ноутбук'
     assert str(item3) == 'Телефон'

def test_calculate_total_price(item1, item2):
     """Проверка расчета общей стоимости товаров"""
     assert item1.calculate_total_price() == 200000
     assert item2.calculate_total_price() == 100000

def test_apply_discount(item1, item2):
     """Проверка установленной скидки на конкретный товар"""
     Item.pay_rate = 0.8
     item1.apply_discount()
     assert item1.price == 8000.0
     assert item2.price == 20000

def test_number_added_instances(item1, item2):
     """Проверка количества экземпляров класса в атрибуте all"""
     assert len(Item.all) == 2
     assert item1 in Item.all
     assert item2 in Item.all

def test_csv_file_data(csv_reader):
     """Проверка чтения csv файла"""
     rows = csv_reader.readlines()
     assert len(rows) == 6
     assert rows[0].strip().split(',') == ['name', 'price', 'quantity']
     assert rows[1].strip().split(',') == ['Смартфон', '100', '1']
     assert rows[2].strip().split(',') == ['Ноутбук', '1000', '3']
     assert rows[3].strip().split(',') == ['Кабель', '10', '5']
     assert rows[4].strip().split(',') == ['Мышка', '50', '5']
     assert rows[5].strip().split(',') == ['Клавиатура', '75', '5']

def test_csv_items():
     """Проверка того что все данные в csv файле внесены в список all"""
     Item.instantiate_from_csv('src/item.py')
     assert len(Item.all) == 5

def test_name_setter_error(item3):
     """Проверка установки слишком длинного названия"""
     item3.name = "СуперСмартфон"

     if len(item3.name) > 10:
          with pytest.raises(AssertionError):
               assert item3.name == 'Название товара слишком длинное. Оно будет обрезано до 10 символов.'

def test_name_setter_crop(item3):
     """Проверка обрезания названия при установке слишком длинного"""
     item3.name = "СуперСмартфон"
     assert item3.name == 'СуперСмарт'

     item3.name = 'Телефон'
     assert item3.name == 'Телефон'

def test_string_to_number():
     """Проверка того что при получении str будет возвращаться int"""
     assert Item.string_to_number('5') == 5
     assert Item.string_to_number('5.0') == 5
     assert Item.string_to_number('5.5') == 5

def test_add_classes(item1, phone1):
     """Проверяет сложение экземпляров классов Item и Phone"""
     assert item1 + phone1 == 25
     assert phone1 + phone1 == 10

def test_csv_file_errors(csv_reader):
     """Проверка обработки ошибок при чтении csv файла"""
     x = [i for i in csv.DictReader(csv_reader)]
     if len(x) != 5:
          with pytest.raises(InstantiateCSVError):
               print(f'Файл item.csv поврежден')

     if csv_reader is None:
          with pytest.raises(FileNotFoundError):
               print('Отсутствует файл item.csv')


