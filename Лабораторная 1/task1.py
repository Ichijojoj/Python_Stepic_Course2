import doctest


class Kettle:
    """
    Класс, описывающий поведение и характеристики чайника.
    """

    def __init__(self, capacity_volume: float, current_volume: float, is_heated: bool = False):
        """
        Инициализация чайника.

        :param capacity_volume: Максимальный объем чайника.
        :param current_volume: Текущий объем воды в чайнике.
        :param is_heated: Нагрета ли вода в чайнике.

        Примеры:
        >>> kettle = Kettle(1.5, 0)
        """
        if not isinstance(capacity_volume, (int, float)) or capacity_volume <= 0:
            raise ValueError("Максимальный объем чайника должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(current_volume, (int, float)) or current_volume < 0:
            raise ValueError("Текущий объем воды должен быть неотрицательным числом")
        if current_volume > capacity_volume:
            raise ValueError("Текущий объем воды не может превышать максимальный объем чайника")
        self.current_volume = current_volume

        self.is_heated = is_heated

    def fill(self, volume: float) -> None:
        """
        Наполнение чайника водой.

        :param volume: Объем добавляемой воды.
        :raise ValueError: Если объем добавляемой воды отрицательный или превышает свободное место в чайнике.

        Примеры:
        >>> kettle = Kettle(1.5, 0)
        >>> kettle.fill(1.0)
        """
        if not isinstance(volume, (int, float)) or volume < 0:
            raise ValueError("Объем добавляемой воды должен быть положительным числом")

        if self.current_volume + volume > self.capacity_volume:
            raise ValueError("Добавляемый объем воды превышает свободное место в чайнике")

        self.current_volume += volume

    def heat(self) -> None:
        """
        Нагревание воды в чайнике.

        Примеры:
        >>> kettle = Kettle(1.5, 1.0)
        >>> kettle.heat()
        """
        if self.current_volume == 0:
            raise ValueError("Нельзя нагреть чайник без воды")

        self.is_heated = True

    def pour_out(self, volume: float) -> None:
        """
        Выливание воды из чайника.

        :param volume: Объем выливаемой воды.
        :raise ValueError: Если объем выливаемой воды отрицательный или превышает текущий объем воды в чайнике.

        Примеры:
        >>> kettle = Kettle(1.5, 1.0)
        >>> kettle.pour_out(0.5)
        """
        if not isinstance(volume, (int, float)) or volume < 0:
            raise ValueError("Объем выливаемой воды должен быть положительным числом")

        if volume > self.current_volume:
            raise ValueError("Объем выливаемой воды превышает текущий объем воды в чайнике")

        self.current_volume -= volume

    def get_status(self) -> str:
        """
        Получение информации о состоянии чайника.

        :return: Строка с информацией о текущем объеме воды и ее температуре.

        Примеры:
        >>> kettle = Kettle(1.5, 1.0, True)
        >>> kettle.get_status()
        'Current volume: 1.0 liters, Water is heated'
        """
        heated_status = "heated" if self.is_heated else "not heated"
        return f"Current volume: {self.current_volume} liters, Water is {heated_status}"




class Computer:
    """
    Класс, описывающий поведение и характеристики компьютера.
    """

    def __init__(self, processor: str, ram: int, storage: int):
        """
        Инициализация компьютера.

        :param processor: Название процессора.
        :param ram: Объем оперативной памяти в ГБ.
        :param storage: Объем внутреннего хранилища в ГБ.

        Примеры:
        >>> computer = Computer("Intel i7", 16, 512)
        """
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.is_on = False
        self.is_in_game_mode = False

    def turn_on(self) -> None:
        """
        Включение компьютера.

        Примеры:
        >>> computer = Computer("Intel i7", 16, 512)
        >>> computer.turn_on()
        >>> computer.is_on
        True
        """
        self.is_on = True

    def work(self) -> None:
        """
        Режим работы на компьютере.

        Примеры:
        >>> computer = Computer("Intel i7", 16, 512)
        >>> computer.turn_on()
        >>> computer.work()
        """
        if not self.is_on:
            raise RuntimeError("Компьютер выключен")
        self.is_in_game_mode = False

    def play_game(self) -> None:
        """
        Игровой режим на компьютере.

        Примеры:
        >>> computer = Computer("Intel i7", 16, 512)
        >>> computer.turn_on()
        >>> computer.play_game()
        >>> computer.is_in_game_mode
        True
        """
        if not self.is_on:
            raise RuntimeError("Компьютер выключен")
        self.is_in_game_mode = True

    def turn_off(self) -> None:
        """
        Выключение компьютера.

        Примеры:
        >>> computer = Computer("Intel i7", 16, 512)
        >>> computer.turn_on()
        >>> computer.turn_off()
        >>> computer.is_on
        False
        """
        self.is_on = False
        self.is_in_game_mode = False

    def get_status(self) -> str:
        """
        Получение статуса компьютера.

        :return: Статус компьютера.

        Примеры:
        >>> computer = Computer("Intel i7", 16, 512)
        >>> computer.turn_on()
        >>> computer.get_status()
        'Включен, Режим работы: Обычный'
        >>> computer.play_game()
        >>> computer.get_status()
        'Включен, Режим работы: Игровой'
        """
        on_status = "Включен" if self.is_on else "Выключен"
        mode_status = "Игровой" if self.is_in_game_mode else "Обычный"
        return f"{on_status}, Режим работы: {mode_status}"

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
