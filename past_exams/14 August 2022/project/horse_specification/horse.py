from abc import ABC, abstractmethod

from project.validation.validation import Validation


class Horse(ABC):
    MAX_HORSE_SPEED = None

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.horse_name_less_than_4(value)
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validation.max_speed(value, self.MAX_HORSE_SPEED)
        self.__speed = value

    @abstractmethod
    def train(self):
        pass
