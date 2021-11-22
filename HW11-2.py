from typing import get_type_hints


class Car():
    def __init__(self, type, model, year, speed=0):
        self.__type = type
        self.__model = model
        self.__year = year
        self.__speed = speed

    def getType(self):
        return self.__type

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year

    def getSpeed(self):
        return self.__speed

    def upSpeed(self):
        self.__speed += 5
        print(self.__speed)

    def downSpeed(self):
        self.__speed = self.__speed - 5

    def breake(self):
        self.__speed = 0

    def ShowSpeed(self):
        print(f'{self.__speed} km/h')

    def changeWay(self):
        self.__speed = - self.__speed


mitshubishi = Car('Sedan', 'x335', 2002, 90)
