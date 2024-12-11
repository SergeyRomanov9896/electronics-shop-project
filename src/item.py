
import csv
from pathlib import Path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, path: str) -> list:
        """Загружает данные из CSV-файла и создает экземпляры класса."""
        base_path = Path(__file__).parent.parent / 'src' / 'items.csv'

        with open(base_path, encoding="windows-1251") as file_csv:
            reader = csv.DictReader(file_csv)

            return [cls.all.append(cls(**row)) for row in reader]

    @staticmethod
    def string_to_number(string_value: str) -> int:
        """Преобразует строковое представление числа в целое число."""
        return int(float(string_value))

    @property
    def name(self):
        """Возвращает название продукта."""
        return self.__name

    @name.setter
    def name(self, name: str):
        """Устанавливает название товара, обрезая его, если оно превышает 10 символов."""
        if len(self.__name) > 10:
            raise ValueError("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price = self.price * Item.pay_rate

    def __add__(self, other):
        return self.quantity + other.quantity

