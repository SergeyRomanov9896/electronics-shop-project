"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

ITEM1 = Item(name="Смартфон", price=10000, quantity=20)
ITEM2 = Item(name="Ноутбук", price=20000, quantity=5)

def test_init():
     """Тестирование инициализации объекта."""
     assert ITEM1.name == "Смартфон"
     assert ITEM1.price == 10000
     assert ITEM1.quantity == 20

     assert ITEM2.name == "Ноутбук"
     assert ITEM2.price == 20000
     assert ITEM2.quantity == 5

def test_calculate_total_price():
     """Тестирование метода расчета общей стоимости."""
     assert ITEM1.calculate_total_price() == ITEM1.price * ITEM1.quantity
     assert ITEM2.calculate_total_price() == ITEM2.price * ITEM2.quantity

def test_apply_discount():
     """Тестирование применения скидки."""
     Item.pay_rate = 0.8
     ITEM1.apply_discount()
     assert ITEM1.price == float(8000)

def test_all_items():
     """Тестирование списка всех товаров."""
     assert len(Item.all) == 2
     assert ITEM1 in Item.all
     assert ITEM2 in Item.all