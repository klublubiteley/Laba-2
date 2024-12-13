from task_1 import Student, Product, Book

if __name__ == "__main__":
    student = Student("Иван", 20, [5, 4, 3, 4, 5])
    product = Product("Ноутбук", 50000, 10)
    book = Book("Война и мир", "Лев Толстой", 1869)

    try:
        student.add_grade(0)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        product.update_price(-670000)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        book.is_old(-2077)
    except ValueError:
        print('Ошибка: неправильные данные')
