# У нас есть какой-то unit, которому мы в параметры передаем
# - наше игровое поле
# - X координату
# - Y координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, x, y, field, state, speed):
        self.x = x
        self.y = y
        self.field = field
        self.state = state
        self.speed = speed

    def _get_speed(self):
        match self.state:
            case "fly":
                return self.speed * 1.2
            case "crawl":
                return self.speed * 0.5
            case _:
                raise ValueError
    def move(self, direction):
        """Функция реализует перемещение unit'а по полю. В качестве параметра принимает направление его движения.
        :param direction: Направление перемещения
        """
        speed = self._get_speed()
        match direction:
            case "UP":
                self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
            case "DOWN":
                self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
            case "LEFT":
                self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
            case "RIGHT":
                self.field.set_unit(y=self.y, x=self.x + speed, unit=self)
