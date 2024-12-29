class Vehicle:
    """ Базовый класс для транспортных средств. """

    def __init__(self, make: str, model: str, year: int):
        """
        Конструктор для транспортного средства.

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self._make = make  # Непубличный атрибут, чтобы не изменять его случайно
        self._model = model  # Непубличный атрибут
        self._year = year  # Непубличный атрибут

    def start_engine(self) -> str:
        """ Запускает двигатель транспортного средства. """
        return f"{self._make} {self._model} engine started."

    def __str__(self) -> str:
        return f"{self._year} {self._make} {self._model}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, year={self._year!r})"


class Car(Vehicle):
    """ Класс легкового автомобиля, наследующий от Vehicle. """

    def __init__(self, make: str, model: str, year: int, doors: int):
        """
        Конструктор для легкового автомобиля.

        :param make: Производитель легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(make, model, year)
        self._doors = doors  # Непубличный атрибут

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового автомобиля.

        Переопределяем метод, чтобы добавить индивидуальное сообщение, специфичное для легкового автомобиля.
        """
        return f"{super().start_engine()} (Car with {self._doors} doors)"

    def __str__(self) -> str:
        return f"{super().__str__()} (Car with {self._doors} doors)"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, year={self._year!r}, doors={self._doors!r})"


class Truck(Vehicle):
    """ Класс грузового автомобиля, наследующий от Vehicle. """

    def __init__(self, make: str, model: str, year: int, capacity: float):
        """
        Конструктор для грузового автомобиля.

        :param make: Производитель грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность грузового автомобиля в тоннах.
        """
        super().__init__(make, model, year)
        self._capacity = capacity  # Непубличный атрибут

    def load_cargo(self, weight: float) -> str:
        """

        :param weight: Вес груза в тоннах.
        :return: Сообщение о загрузке.
        """
        if weight > self._capacity:
            return f"Cannot load {weight} tons, exceeding capacity of {self._capacity} tons."
        return f"Loaded {weight} tons of cargo."

    def __str__(self) -> str:
        return f"{super().__str__()} (Truck with {self._capacity} tons capacity)"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, year={self._year!r}, capacity={self._capacity!r})"
