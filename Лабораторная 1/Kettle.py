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
