
class LanguageMixin:
    """
    Класс для изменения раскладки клавиатуры

    Attributes:
        __LANGUAGE (str): Приватный атрибут, хранящий текущую раскладку клавиатуры (EN или RU).
    """
    EN = "EN"  # Константа для английской раскладки
    RU = "RU"  # Константа для русской раскладки

    __LANGUAGE = "EN"

    def change_lang(self):
        """Меняет текущую раскладку клавиатуры на противоположную."""
        self.__LANGUAGE = self.RU if self.__LANGUAGE == self.EN else self.EN

    @property
    def language(self):
        """Возвращает текущую раскладку клавиатуры."""
        return self.__LANGUAGE

class Keyboard(LanguageMixin):
    """
    Класс для описания клавиатуры с возможностью изменения раскладки.
    """

    def __init__(self, name: str, price: [int, float], quantity: int) -> None:
        """
        Инициализатор экземпляр класса Keyboard

        :param name: Название клавиатуры.
        :param price: Цена клавиатуры.
        :param quantity: Количество клавиатур.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчиков.

        :return: Название клавиатуры, Цена и Количество.
        """
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строковое представление объекта для конечного пользователя

        :return: Название клавиатуры.
        """
        return self.name


