# 1. Создать класс TrafficLight...

from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 1))

    def running(self):
        for color, sec in cycle(self.__color):
            print(f'Цвет светофора: {color}, ожидание {sec} секунд(ы)')
            sleep(sec)


traffic_light = TrafficLight()
traffic_light.running()
