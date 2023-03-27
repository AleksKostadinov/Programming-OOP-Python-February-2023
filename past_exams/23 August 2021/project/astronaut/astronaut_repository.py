from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        # a = next(filter(lambda x: x.name == name, self.astronauts), None)
        for a in self.astronauts:
            if a.name == name:
                return a