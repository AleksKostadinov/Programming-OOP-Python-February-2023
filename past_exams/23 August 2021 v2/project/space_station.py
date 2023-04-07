from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.mission_report = {" successful missions!": 0, " missions were not completed!": 0}

    # def __find_astronaut(self, name):
    #     for a in self.astronaut_repository.astronauts:
    #         if a.name == name:
    #             return a

    # def __find_planet(self, name):
    #     for p in self.planet_repository.planets:
    #         if p.name == name:
    #             return p

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut:
            return f"{name} is already added."

        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            new_astronaut = Meteorologist(name)
        else:
            raise Exception("Astronaut type is not valid!")

        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)

        if planet:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items += items.split(', ')
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        sorted_astronauts = [a for a in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)]

        if all(a.oxygen <= 30 for a in sorted_astronauts):
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_top5 = sorted_astronauts[:5]

        for a in astronauts_top5:
            while planet.items and a.oxygen > 0:
                a.backpack.append(planet.items.pop())
                a.breathe()

        if planet.items:
            self.mission_report[' missions were not completed!'] += 1
            return "Mission is not completed."

        self.mission_report[' successful missions!'] += 1
        return f"Planet: {planet_name} was explored. " \
               f"{len([a for a in astronauts_top5 if a.backpack])} astronauts participated in collecting items."

    def report(self):
        result = []

        for key, value in self.mission_report.items():
            result.append(f'{value}{key}')

        result.append("Astronauts' info:")
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f'Name: {astronaut.name}')
            result.append(f'Oxygen: {astronaut.oxygen}')
            if astronaut.backpack:
                result.append(f"Backpack items: {', '.join(astronaut.backpack)}")
            else:
                result.append(f"Backpack items: none")
        return '\n'.join(result)
