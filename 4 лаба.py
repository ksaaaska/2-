if __name__ == "__main__":
    # Write your solution here
    pass
# Базовый класс: "транспортное средство"

class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.

    Атрибуты:
    - brand (str): марка транспортного средства
    - color (str): цвет транспортного средства
    """

    def __init__(self, brand: str, color: str):
        self._brand = brand  # Марка транспортного средства (приватный атрибут)
        self.color = color

    def __str__(self) -> str:
        return f'{self._brand}'

    def __repr__(self) -> str:
        return f"Vehicle(brand='{self._brand}', color='{self.color}')"

# Дочерний класс: "автомобиль"

class Car(Vehicle):
    """
    Дочерний класс, представляющий автомобиль.

    Дополнительные атрибуты:
    - model (str): модель автомобиля
    - year (int): год выпуска автомобиля
    """

    def __init__(self, brand: str, color: str, model: str, year: int):
        super().__init__(brand, color)
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f'{self._brand} {self.model}'

    def __repr__(self) -> str:
        return f"Car(brand='{self._brand}', color='{self.color}', model='{self.model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Метод для запуска двигателя автомобиля.

        Возвращает строку о том, что двигатель автомобиля был успешно запущен.
        """
        return 'Двигатель запущен.'

    def drive(self, distance: float) -> str:
        """
        Метод для езды на автомобиле.

        Аргументы:
        - distance (float): расстояние, которое нужно проехать

        Возвращает строку о пройденном расстоянии.
        """
        return f'Проехали {distance} км.'
