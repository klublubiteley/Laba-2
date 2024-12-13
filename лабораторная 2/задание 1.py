import doctest


class Student:
    def __init__(self, name: str, age: int, grades: list[int]) -> None:
        """
        Инициализация объекта Студент.

        :param name: Имя студента.
        :param age: Возраст студента (от 18 до 100 лет).
        :param grades: Список оценок студента.

        :raises ValueError: Если возраст меньше 18 или больше 100.
        """
        if not (18 <= age <= 100):
            raise ValueError("Возраст должен быть от 18 до 100 лет.")
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self) -> float:
        """
        Возвращает средний балл студента.

        :return: Средний балл.

        :doctest:
        >>> student = Student('Иван', 20, [5, 4, 3, 4, 5])
        >>> student.average_grade()
        4.2
        """
        return sum(self.grades) / len(self.grades)

    def add_grade(self, grade: int) -> None:
        """
        Добавляет новую оценку студенту.

        :param grade: Оценка студента.

        :raises ValueError: Если оценка не в диапазоне от 1 до 5.
        """
        if not (1 <= grade <= 5):
            raise ValueError("Оценка должна быть в диапазоне от 1 до 5.")
        self.grades.append(grade)


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Инициализация объекта Товар.

        :param name: Название товара.
        :param price: Цена товара (должна быть положительной).
        :param quantity: Количество товара на складе (должно быть не отрицательным).

        :raises ValueError: Если цена или количество товара отрицательны.
        """
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price: float) -> None:
        """
        Обновляет цену товара.

        :param new_price: Новая цена товара.

        :raises ValueError: Если новая цена отрицательная.
        """
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.price = new_price

    def update_quantity(self, new_quantity: int) -> None:
        """
        Обновляет количество товара.

        :param new_quantity: Новое количество товара.

        :raises ValueError: Если новое количество отрицательное.
        """
        if new_quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным.")
        self.quantity = new_quantity

    def total_value(self) -> float:
        """
        Рассчитывает общую стоимость товара на складе (цена * количество).

        :return: Общая стоимость товара.

        :doctest:
        >>> product = Product("Ноутбук", 50000, 10)
        >>> product.total_value()
        500000
        """
        return self.price * self.quantity


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Инициализация объекта Книга.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год выпуска книги.

        :raises ValueError: Если год выпуска книги больше текущего.
        """
        if year > 2024:
            raise ValueError("Год выпуска книги не может быть больше текущего.")
        self.title = title
        self.author = author
        self.year = year

    def is_old(self, year: int) -> bool:
        """
        Проверяет, является ли книга старой (более 50 лет).

        :return: True, если книга старая (более 50 лет), иначе False.

        :doctest:
        >>> book = Book("1984", "Джордж Оруэлл", 1949)
        >>> book.is_old(2077)
        True
        """
        if year < 0:
            raise ValueError("Где-то косяк")
        else:
            return 2024 - self.year > 50

    def brief_info(self) -> str:
        """
        Возвращает краткую информацию о книге.

        :return: Краткая информация о книге.

        :doctest:
        >>> book = Book("Война и мир", "Лев Толстой", 1869)
        >>> book.brief_info()
        'Книга "Война и мир" написана Лев Толстой и издана в 1869 году.'
        """
        return f'Книга "{self.title}" написана {self.author} и издана в {self.year} году.'


if __name__ == "__main__":
    doctest.testmod()
