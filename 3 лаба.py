class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name} by {self.author}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Pages must be an integer.")
        if value <= 0:
            raise ValueError("Number of pages must be positive.")
        self._pages = value

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name} by {self.author}, {self.pages} pages'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Duration must be a number.")
        if value <= 0:
            raise ValueError("Duration must be positive.")
        self._duration = value

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name} by {self.author}, {self.duration} hours'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}', duration={self.duration})"

