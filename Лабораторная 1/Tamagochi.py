

import doctest
class Tamagotchi:
    """
    Класс, описывающий поведение и характеристики Тамагочи.
    """

    def __init__(self, name: str, age: int, hunger: int, tiredness: int = 0):
        """
        Инициализация Тамагочи.

        :param name: Имя Тамагочи.
        :param age: Возраст Тамагочи.
        :param hunger: Уровень голода Тамагочи.
        :param tiredness: Уровень усталости Тамагочи.

        Примеры:
        >>> tamagotchi = Tamagotchi("Tama", 2, 50)
        """
        self.name = name
        self.age = age
        self.hunger = hunger
        self.tiredness = tiredness

    def feed(self, amount: int) -> None:
        """
        Кормление Тамагочи.

        :param amount: Количество еды.
        :raise ValueError: Если количество еды отрицательное.

        Примеры:
        >>> tamagotchi = Tamagotchi("Tama", 2, 50)
        >>> tamagotchi.feed(20)
        """
        if amount < 0:
            raise ValueError("Количество еды должно быть положительным числом")

        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0

    def play(self, time: int) -> None:
        """
        Игра с Тамагочи.

        :param time: Время, в течение которого играем.
        :raise ValueError: Если время игры отрицательное.

        Примеры:
        >>> tamagotchi = Tamagotchi("Tama", 2, 50)
        >>> tamagotchi.play(15)
        """
        if time < 0:
            raise ValueError("Время игры должно быть положительным числом")

        self.tiredness += time
        if self.tiredness > 100:
            self.tiredness = 100

    def sleep(self, duration: int) -> None:
        """
        Укладывание Тамагочи спать.

        :param duration: Длительность сна.
        :raise ValueError: Если длительность сна отрицательная.

        Примеры:
        >>> tamagotchi = Tamagotchi("Tama", 2, 50)
        >>> tamagotchi.sleep(8)
        """
        if duration < 0:
            raise ValueError("Длительность сна должна быть положительным числом")

        self.tiredness -= duration
        if self.tiredness < 0:
            self.tiredness = 0

    def get_status(self) -> str:
        """
        Получение статуса Тамагочи.

        :return: Строка с описанием статуса.

        Примеры:
        >>> tamagotchi = Tamagotchi("Tama", 2, 50)
        >>> tamagotchi.get_status()
        'Tama, 2 years old, Hunger: 50, Tiredness: 0'
        """
        return f"{self.name}, {self.age} years old, Hunger: {self.hunger}, Tiredness: {self.tiredness}"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
