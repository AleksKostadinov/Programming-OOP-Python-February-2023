from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __find_horse_by_name(self, name):
        for horse in self.horses:
            if horse.name == name:
                return horse

    def __find_horse_by_type(self, horse_type):
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        return None

    def __find_jockeys_by_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self.__find_horse_by_name(horse_name)

        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type == 'Appaloosa':
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == 'Thoroughbred':
            new_horse = Thoroughbred(horse_name, horse_speed)
        else:
            return

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self.__find_jockeys_by_name(jockey_name)

        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)

        if race:
            raise Exception(f"Race {race_type} has been already created!")

        if race_type in ("Winter", "Spring", "Autumn", "Summer"):
            new_race = HorseRace(race_type)
            self.horse_races.append(new_race)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockeys_by_name(jockey_name)
        horse = self.__find_horse_by_type(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        else:
            if jockey.horse:
                return f"Jockey {jockey_name} already has a horse."

            jockey.horse = horse
            jockey.horse.is_taken = True
            return f"Jockey {jockey_name} will ride the horse {jockey.horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.__find_jockeys_by_name(jockey_name)
        race = self.__find_race_by_type(race_type)

        if not race or race_type not in ("Winter", "Spring", "Autumn", "Summer"):
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        else:
            if jockey.horse is None:
                raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

            if jockey in race.jockeys:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        fastest_jockey = sorted(race.jockeys, key=lambda x: -x.horse.speed)[:1]

        return f"The winner of the {race_type} race, " \
               f"with a speed of {fastest_jockey[0].horse.speed}km/h is {fastest_jockey[0].name}! " \
               f"Winner's horse: {fastest_jockey[0].horse.name}."
