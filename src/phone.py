
from src.item import Item

class Phone(Item):
    """
    Класс, представляющий телефон, наследующий от класса Item.
    Этот класс расширяет класс Item, добавляя специфические атрибуты и методы для телефонов.
    """
    def __init__(self, name: str, price: [int, float], quantity: int, number_of_sim: int) -> None:
        """
        Инициализирует экземпляр класса Phone.

        :param name: Название телефона.
        :param price: Цена телефона.
        :param quantity: Количество телефонов в наличии.
        :param number_of_sim: Количество SIM-карт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчиков.

        :return: Название телефона, Цена, Количество в наличии и количество SIM-карт.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """
        Возвращает строковое представление объекта для конечного пользователя.

        :return: Название телефона.
        """
        return f"{self.name}"

    @property
    def number_of_sim(self):
        """
        :return: Количество SIM-карт.
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        """
        Устанавливает количество SIM-карт.

        :param value: Количество SIM-карт.
        :raises ValueError: Если значение не является положительным целым числом.
        """
        if not type(value) is int or int(value) <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._number_of_sim = value

