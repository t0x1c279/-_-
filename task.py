import doctest
class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация автомобиля.

        :param make: Производитель автомобиля (например, 'Toyota').
        :param model: Модель автомобиля (например, 'Camry').
        :param year: Год выпуска автомобиля. Должен быть больше 1884, так как я рассматриваю автомобили с двигателем внутреннего сгорания, история которых началась с 1885 года.

        :raises ValueError: Если год меньше 1885.
        """
        if year < 1885:
            raise ValueError("Год выпуска не может быть меньше 1885.")

        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """Запускает двигатель автомобиля."""
        return f"{self.make} {self.model} двигатель запущен."

    def get_info(self) -> str:
        """Возвращает информацию об автомобиле.

        >>> car = Car('Toyota', 'Camry', 2015)
        >>> car.get_info()
        'Toyota Camry, 2015 год выпуска'
        """
        return f'{self.make} {self.model}, {self.year} год выпуска'


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц. Должно быть положительным числом.

        :raises ValueError: Если количество страниц не положительное.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> str:
        """
        Симулирует чтение книги.

        :param pages_read: Количество прочитанных страниц. Должно быть не больше количества страниц в книге.

        :raises ValueError: Если pages_read больше количества страниц.

        :return: Сообщение о прочитанных страницах.

        >>> book = Book('2023', 'Tom Sawyer', 288)
        >>> book.read(50)
        'Вы прочитали 50 страниц из 288.'
        """
        if pages_read > self.pages:
            raise ValueError("Нельзя прочитать больше страниц, чем есть в книге.")

        return f'Вы прочитали {pages_read} страниц из {self.pages}.'

    def get_summary(self) -> str:
        """Возвращает краткое описание книги."""
        return f'"{self.title}" написана {self.author} и содержит {self.pages} страниц.'


class Smartphone:
    def __init__(self, phone_name: str, name_of_company: str, year_of_manufacture: int, capacity: int,
                 consumption_time_1_per_cent: float):
        """
        Инициализация смартфона.

        :param phone_name: Название телефона.
        :param name_of_company: Название компании, которая выпустила телефон.
        :param year_of_manufacture: Год выпуска телефона. Должен быть больше 1991, так как я рассматриваю смартфоны.
        :param capacity: Ёмкость телефона (в мАч).

        :raises ValueError: Если год меньше 1992.
        """
        if year_of_manufacture < 1992:
            raise ValueError("Неверно указан год производства телефона!")

        self.phone_name = phone_name
        self.name_of_company = name_of_company
        self.year_of_manufacture = year_of_manufacture
        self.capacity = capacity

    def time_of_using_phone(self, hours_spent: float) -> str:
        """Возвращает время, которое вы провели в телефоне.

        >>> phone = Smartphone('Redmi Note 12 Pro', 'Xiaomi', 2023, 5000, 5.53)
        >>> phone.time_of_using_phone(4)
        'Вы провели 4 часов в телефоне!!! Может пора отвлечься???'
        """
        return f'Вы провели {hours_spent} часов в телефоне!!! Может пора отвлечься???'

    def get_info(self) -> str:
        """Возвращает характеристики телефона.

        >>> phone = Smartphone('Redmi Note 12 Pro', 'Xiaomi', 2023, 5000, 5.53)
        >>> phone.get_info()
        'Название телефона: Redmi Note 12 Pro, Производитель: Xiaomi, Год выпуска: 2023, Ёмкость: 5000 мАч'
        """
        return f'Название телефона: {self.phone_name}, Производитель: {self.name_of_company}, Год выпуска: {self.year_of_manufacture}, Ёмкость: {self.capacity} мАч'


if __name__=="__main__":
    doctest.testmod()