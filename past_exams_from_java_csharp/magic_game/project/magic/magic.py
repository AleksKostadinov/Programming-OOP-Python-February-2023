from abc import ABC, abstractmethod


class Magic(ABC):
    def __init__(self, name, bullets_count):
        self.name = name
        self.bullets_count = bullets_count

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Magic cannot be null or empty.')
        self.__name = value

    @property
    def bullets_count(self):
        return self.__bullets_count

    @bullets_count.setter
    def bullets_count(self, value):
        if value < 0:
            raise ValueError('Bullets cannot be below 0.')
        self.__bullets_count = value

    @abstractmethod
    def fire(self):
        ...

    def __str__(self):
        return f"{self.magic_type} Magic: {self.name} ({self.bullets_count} bullets)"
