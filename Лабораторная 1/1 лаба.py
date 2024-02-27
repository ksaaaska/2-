# TODO Написать 3 класса с документацией и аннотацией типов
class Person:
    """
    Класс, представляющий человека.

    Атрибуты:
    - name (str): имя человека
    - age (int): возраст человека
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Car:
    """
    Класс, представляющий автомобиль.

    Атрибуты:
    - make (str): марка автомобиля
    - model (str): модель автомобиля
    - year (int): год выпуска автомобиля
    """

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year


class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
    - title (str): название книги
    - author (str): автор книги
    - pages (int): количество страниц в книге
    """

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

if __name__ == "__main__":
    import doctest
    doctest.testmod()
