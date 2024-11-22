
import csv
from pathlib import Path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int, add=True) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        if add:
            Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, path: str) -> list:
        """Загружает данные из файла csv"""
        base_path = Path(__file__).parent.parent / 'src' / 'items.csv'

        with open(base_path, encoding="windows-1251") as file_csv:
            reader = csv.DictReader(file_csv)

            return [cls(**row) for row in reader]

    @staticmethod
    def string_to_number(string_value: str) -> int:
        """Возвращает число из числа строки"""
        return int(float(string_value))

    @property
    def name(self):
        """Возвращает название продукта."""
        return self.__name

    @name.setter
    def name(self, value):
        """Если названия больше 10 символов, то оно обрезается"""
        if len(self.__name) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
