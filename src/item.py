import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int, add_to_all=True) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        if add_to_all:
            Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, path: str):
        """Загружает данные из файла csv"""
        with open(path, encoding="windows-1251") as file_csv:
            reader = csv.DictReader(file_csv)

            return [cls(**row) for row in reader]

    @property
    def product_name(self):
        """Возвращает название продукта."""
        return self.__name

    @product_name.setter
    def product_name(self, value):
        """Если названия больше 10 символов, то оно обрезается"""
        if len(self.__name) > 10:
            self.__name = value[:10]

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
