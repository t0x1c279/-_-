# TODO: описать базовый класс
class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Attributes:
        make (str): Производитель транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска транспортного средства.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        Args:
            make (str): Производитель.
            model (str): Модель.
            year (int): Год выпуска.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление транспортного средства."""
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"

# TODO: описать дочерний класс
class Car(Vehicle):
    """
    Класс для легковых автомобилей, наследующий от Vehicle.

    Attributes:
        fuel_type (str): Тип топлива, используемого автомобилем.
    """

    def __init__(self, make: str, model: str, year: int, fuel_type: str) -> None:
        """
        Инициализация легкового автомобиля.

        Args:
            make (str): Производитель.
            model (str): Модель.
            year (int): Год выпуска.
            fuel_type (str): Тип топлива.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self.__fuel_type = fuel_type  # Непубличный атрибут для инкапсуляции

    def get_fuel_type(self) -> str:
        """Возвращает тип топлива автомобиля."""
        return self.__fuel_type

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} (Fuel Type: {self.__fuel_type})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление легкового автомобиля."""
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, fuel_type='{self.__fuel_type}')"

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        Returns:
            str: Сообщение о запуске двигателя.
        """
        return f"The engine of the {self.make} {self.model} is now running."

    def start_engine_with_mode(self, mode: str) -> str:
        """
        Запускает двигатель автомобиля с заданным режимом.

        Args:
            mode (str): Режим запуска (например, 'eco', 'sport').

        Returns:
            str: Сообщение о запуске двигателя в заданном режиме.

        Raises:
            ValueError: Если режим не поддерживается.

        Обоснование перегрузки метода:
        Перегрузка метода start_engine позволяет пользователю выбирать режим запуска двигателя,
        что может быть полезно для оптимизации расхода топлива или повышения производительности.
        """
        if mode not in ['eco', 'sport']:
            raise ValueError("Unsupported mode. Choose 'eco' or 'sport'.")

        return f"The engine of the {self.make} {self.model} is now running in '{mode}' mode."


# Пример использования классов
if __name__ == "__main__":
    # Создаем экземпляр легкового автомобиля
    my_car = Car("Toyota", "Camry", 2021, "Gasoline")

    # Выводим информацию об автомобиле
    print(my_car)  # Использует перегруженный метод __str__
    print(repr(my_car))  # Использует перегруженный метод __repr__

    # Запускаем двигатель
    print(my_car.start_engine())  # Стандартный запуск двигателя
    print(my_car.start_engine_with_mode("sport"))  # Запуск в спортивном режиме