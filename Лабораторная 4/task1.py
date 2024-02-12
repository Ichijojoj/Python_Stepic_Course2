from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Базовый класс Транспортное средство.
    """
    def __init__(self, brand: str, model: str, year: int):
        """
        Конструктор класса Транспортное средство.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def move(self) -> str:
        """
        Абстрактный метод движения транспортного средства.
        """
        pass

    def __str__(self) -> str:
        """
        Магический метод преобразования объекта в строку.
        """
        return f"{self.brand} {self.model} {self.year}"

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки.
        """
        return f"Vehicle(brand={self.brand}, model={self.model}, year={self.year})"


class Car(Vehicle):
    """
    Дочерний класс Легковой автомобиль.
    """
    def __init__(self, brand: str, model: str, year: int, color: str):
        """
        Конструктор класса Легковой автомобиль.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param color: Цвет автомобиля.
        """
        super().__init__(brand, model, year)
        self.color = color

    def move(self) -> str:
        """
        Метод движения легкового автомобиля.

        :return: Описание движения легкового автомобиля.
        """
        return f"{self.brand} {self.model} едет по дороге."

    def __str__(self) -> str:
        """
        Магический метод преобразования объекта в строку.
        """
        return f"{super().__str__()}, цвет: {self.color}"

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки.
        """
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, color={self.color})"


class Truck(Vehicle):
    """
    Дочерний класс Грузовой автомобиль.
    """
    def __init__(self, brand: str, model: str, year: int, capacity: float):
        """
        Конструктор класса Грузовой автомобиль.

        :param brand: Марка грузовика.
        :param model: Модель грузовика.
        :param year: Год выпуска грузовика.
        :param capacity: Грузоподъемность грузовика в тоннах.
        """
        super().__init__(brand, model, year)
        self.capacity = capacity

    def move(self) -> str:
        """
        Метод движения грузового автомобиля.

        :return: Описание движения грузового автомобиля.
        """
        return f"{self.brand} {self.model} перевозит груз."

    def __str__(self) -> str:
        """
        Магический метод преобразования объекта в строку.
        """
        return f"{super().__str__()}, грузоподъемность: {self.capacity} т"

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки.
        """
        return f"Truck(brand={self.brand}, model={self.model}, year={self.year}, capacity={self.capacity})"


""" Пример работы кода """

car = Car("Toyota", "Supra", "1997", "White")
truck = Truck("Cybertruck", "3000", "2023", "10")

print(car)
print(truck)