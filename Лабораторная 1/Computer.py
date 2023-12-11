
import doctest


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
