from abc import ABC, abstractmethod

from project.magic.magic import Magic


class Magician(ABC):
    def __init__(self, username, health, protection, magic: Magic):
        self.username = username
        self.health = health
        self.protection = protection
        self.magic = magic
        self.is_alive = True

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == '':
            raise ValueError('Username cannot be null or empty.')
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError('Magician health cannot be below 0.')
        self.__health = value

    @property
    def protection(self):
        return self.__protection

    @protection.setter
    def protection(self, value):
        if value < 0:
            raise ValueError('Magician protection cannot be below 0.')
        self.__protection = value

    @property
    def magic(self):
        return self.__magic

    @magic.setter
    def magic(self, value):
        if value is None:
            raise ValueError('Magic cannot be null.')
        self.magic = value

    @abstractmethod
    def take_damage(self, points):
        ...

    def __str__(self):
        return f"{self.magician_type}: {self.username}\n" \
               f"  Health: {self.health}\n" \
               f"  Protection: {self.protection}\n" \
               f"  Magic: {self.magic.name}"

