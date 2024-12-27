class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        # Инициализация атрибутов книги: название и автор
        self._name = name
        self._author = author

    @property
    def name(self):
        # Свойство для получения названия книги
        return self._name

    @property
    def author(self):
        # Свойство для получения автора книги
        return self._author

    def __str__(self):
        # Метод для строкового представления объекта (для print)
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        # Метод для представления объекта в виде строки (для отладки)
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для печатной книги. """

    def __init__(self, name: str, author: str, pages: int):
        # Инициализация атрибутов печатной книги, включая количество страниц
        super().__init__(name, author)  # Вызов конструктора базового класса
        self.pages = pages  # Установка количества страниц через свойство

    @property
    def pages(self):
        # Свойство для получения количества страниц
        return self._pages

    @pages.setter
    def pages(self, value: int):
        # Сеттер для установки количества страниц с проверками
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value  # Установка значения количества страниц

    def __str__(self):
        # Переопределение метода для строкового представления объекта
        return f"{super().__str__()}. Страниц: {self.pages}"


class AudioBook(Book):
    """ Класс для аудиокниги. """

    def __init__(self, name: str, author: str, duration: float):
        # Инициализация атрибутов аудиокниги, включая длительность
        super().__init__(name, author)  # Вызов конструктора базового класса
        self.duration = duration  # Установка длительности через свойство

    @property
    def duration(self):
        # Свойство для получения длительности аудиокниги
        return self._duration

    @duration.setter
    def duration(self, value: float):
        # Сеттер для установки длительности с проверками
        if not isinstance(value, (float, int)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")
        self._duration = float(value)  # Установка значения длительности

    def __str__(self):
        # Переопределение метода для строкового представления объекта
        return f"{super().__str__()}. Длительность: {self.duration} часов"


# Пример использования классов
if __name__ == "__main__":
    try:
        paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
        print(paper_book)  # Вывод информации о печатной книге

        audio_book = AudioBook("Война и мир", "Лев Толстой", 60.5)
        print(audio_book)  # Вывод информации об аудиокниге

        # Пробуем установить некорректные значения
        paper_book.pages = -10  # Это вызовет ValueError
    except (TypeError, ValueError) as e:
        print(e)  # Обработка исключений и вывод сообщения об ошибке