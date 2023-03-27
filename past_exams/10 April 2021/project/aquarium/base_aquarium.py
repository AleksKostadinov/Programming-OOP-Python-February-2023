from abc import ABC


class BaseAquarium(ABC):
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
        if len(value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'
        fish_types = fish.__class__.__name__
        if fish_types in ("FreshwaterFish", "SaltwaterFish"):
            self.fish.append(fish)
            return f'Successfully added {fish_types} to {self.name}.'

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]
        # for f in self.fish:
        #     f.eat()

    def __str__(self):
        result = [
            f"{self.name}:",
            f"Fish: {' '.join(x.name for x in self.fish) if self.fish else 'none'}",
            f"Decorations: {len(self.decorations)}",
            f"Comfort: {self.calculate_comfort()}"
        ]
        return '\n'.join(result)
