from abc import ABC, abstractmethod

from project.validation.validation import Validation


class Delicacy(ABC):
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.empty_string_or_white_space(value, 'Name cannot be null or whitespace!')
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validation.price_less_or_equal_0(value, 'Price cannot be less or equal to zero!')
        self.__price = value

    @abstractmethod
    def details(self):
        pass
