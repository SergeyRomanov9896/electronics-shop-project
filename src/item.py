
import os

import csv

class InstantiateCSVError(Exception):
    pass

class Item:
    """
    Класс для представления товара в магазине.

    Attributes:
        pay_rate (float): Коэффициент, применяемый для расчета итоговой стоимости товара
        all (list): Список всех созданных экземпляров класса.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: [int, float], quantity: int) -> None:
        """
        Инициализирует экземпляр класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчиков.

        :return: Названия товара, цена товара и количество товара.
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строковое представление объекта для конечного пользователя.

        :return: Название товара
        """
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, path: str):
        """
        Инициализирует экземпляры класса на основе данных из CSV-файла.

        Этот метод считывает данные из указанного CSV-файла и создает экземпляры класса,
        заполняя их атрибутами из считанных данных.
        Список всех созданных экземпляров записывается в классный атрибут `cls.all`.

        :param path: Путь к CSV-файлу.
        """
        cls.all.clear()

        base_path = os.path.join(os.path.dirname(__file__), '..', path)
        file_name = os.path.basename(base_path)

        try:
            with open(base_path, encoding="windows-1251") as file_csv:
                reader = csv.DictReader(file_csv)

                if list(reader.fieldnames) != ['name', 'price', 'quantity']:
                     raise InstantiateCSVError(f'Файл {file_name} поврежден')

                items = [cls(**row) for row in reader]

            cls.all = items

        except FileNotFoundError:
            print(f'Отсутствует файл {file_name}')

    @staticmethod
    def string_to_number(string_value: str) -> int:
        """
        Преобразует строковое представление числа в целое число.

        :param string_value: Строковое представление числа.
        """
        return int(float(string_value))

    @property
    def name(self):
        """
        Возвращает название продукта.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Устанавливает название продукта.

        :param name: Новое название продукта

        Ограничения:
            - Длина названия не может превышать 10 символов.
              Если длина превышает 10 символов, название будет автоматически
              обрезано до 10 символов.
        """
        if len(name) > 10:
            self.__name = name[:10]
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

    def __add__(self, other: [int, float]):
        """
        Переопределяет оператор сложения для объектов класса.

        Складывает свойство `quantity` текущего экземпляра с другим экземпляром того же класса.

        :param other: Другой экземпляр класса для сложения.
        :return: Сумма свойства `quantity` двух экземпляров.
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
