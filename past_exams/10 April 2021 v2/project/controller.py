from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def __find_aquarium(self, name):
        for a in self.aquariums:
            if a.name == name:
                return a

    @property
    def __get_type_aquariums(self):
        return {"FreshwaterAquarium": FreshwaterAquarium,
                "SaltwaterAquarium": SaltwaterAquarium}

    @property
    def __get_decorations(self):
        return {"Ornament": Ornament,
                "Plant": Plant}

    @property
    def __get_type_fish(self):
        return {"FreshwaterFish": FreshwaterFish,
                "SaltwaterFish": SaltwaterFish}

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.__get_type_aquariums:
            return "Invalid aquarium type."

        new_aquarium = self.__get_type_aquariums[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.__get_decorations:
            return "Invalid decoration type."

        new_decorations = self.__get_decorations[decoration_type]()
        self.decorations_repository.add(new_decorations)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__find_aquarium(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.__get_type_fish:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium(aquarium_name)

        if not aquarium:
            return

        if aquarium.capacity == len(aquarium.fish):
            return "Not enough capacity."

        if fish_type != aquarium.suitable_for:
            return "Water not suitable."

        new_fish = self.__get_type_fish[fish_type](fish_name, fish_species, price)
        aquarium.add_fish(new_fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)

        if aquarium:
            aquarium.feed()

            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        fish_sum, decoration_sum = 0, 0

        if aquarium:
            if aquarium.fish:
                fish_sum = sum(f.price for f in aquarium.fish)
            if aquarium.decorations:
                decoration_sum = sum(d.price for d in aquarium.decorations)

            value = fish_sum + decoration_sum

            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return '\n'.join(a.__str__() for a in self.aquariums)
