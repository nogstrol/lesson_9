from time import sleep


class TrafficLight:

    def __init__(self, color):
        self._color = color

    def ruuning(self):
        for key, value in self._color.items():
            sleep(value)
            print(key)


traf = TrafficLight(color={
    'Красный': 1,
    'Желтый': 7,
    'Зеленый': 2})
traf.ruuning()
