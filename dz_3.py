from decimal import Decimal


class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def __str__(self):
        return f'{self.name} {self.surname} {self.position} {self._income["wage"]} {self._income["bonus"]}'


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        result = Decimal(self._income['wage']) + Decimal(self._income['bonus'])
        return f'{result} Премия'


if __name__ == '__main__':
    toney = Worker('Соколов', 'Тони', 'установщик', 1000, 1500)
    print(toney)
    sergey = Position('Тихонов', 'Сергей', 'уборщик', 300, 500)
    print(sergey)
    print(sergey.get_full_name())
    print(sergey.get_total_income())

