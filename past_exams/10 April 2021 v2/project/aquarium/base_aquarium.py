from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish: object):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        fish_type = fish.__class__.__name__  # type(fish).__name__
        if fish_type in ("FreshwaterFish", "SaltwaterFish"):
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        result = [f'{self.name}:']
        if self.fish:
            result.append(f'Fish: {" ".join(fish.name for fish in self.fish)}')
        else:
            result.append('Fish: none')

        result.append(f'Decorations: {len(self.decorations)}')
        result.append(f'Comfort: {self.calculate_comfort()}')
        return '\n'.join(result)
