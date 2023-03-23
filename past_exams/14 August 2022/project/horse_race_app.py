from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.validation.validation import Validation


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __find_jockey(self, jockey_name):
        for j in self.jockeys:
            if j.name == jockey_name:
                return j

    def __find_horse(self, horse_type: str):
        return [h for h in self.horses if h.__class__.__name__ == horse_type][-1]

    def __find_race(self, race_type):
        for r in self.horse_races:
            if r.race_type == race_type:
                return r

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return
        Validation.duplicate_name(horse_name, self.horses, f'Horse {horse_name} has been already added!')

        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        Validation.duplicate_name(jockey_name, self.jockeys, f'Jockey {jockey_name} has been already added!')

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        Validation.duplicate_race(race_type, self.horse_races, f'Race {race_type} has been already created!')

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        Validation.jockey_exist(jockey_name, self.jockeys, f'Jockey {jockey_name} could not be found!')
        Validation.horse_available(horse_type, self.horses, f'Horse breed {horse_type} could not be found!')

        jockey = self.__find_jockey(jockey_name)
        horse = self.__find_horse(horse_type)

        if not horse.is_taken and jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.__find_jockey(jockey_name)
        race = self.__find_race(race_type)

        Validation.horse_race_exist(race_type, self.horse_races, f"Race {race_type} could not be found!")
        Validation.jockey_exist(jockey_name, self.jockeys, f"Jockey {jockey_name} could not be found!")
        Validation.jockey_have_horse(jockey, f"Jockey {jockey_name} cannot race without a horse!")

        if any(j.name == jockey_name for j in race.jockeys):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race(race_type)

        Validation.horse_race_exist(race_type, self.horse_races, f"Race {race_type} could not be found!")
        Validation.race_minimum_members(race.jockeys, f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda x: -x.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
