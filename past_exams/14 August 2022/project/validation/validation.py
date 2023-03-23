class Validation:
    @staticmethod
    def empty_string_or_whitespace(text):
        if text.strip() == '':
            raise ValueError("Name should contain at least one character!")

    @staticmethod
    def age_18(number):
        if number < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")

    @staticmethod
    def horse_name_less_than_4(text):
        if len(text) < 4:
            raise ValueError(f"Horse name {text} is less than 4 symbols!")

    @staticmethod
    def max_speed(number, max_speed):
        if number > max_speed:
            raise ValueError("Horse speed is too high!")

    @staticmethod
    def valid_seasons(text):
        if text not in ["Winter", "Spring", "Autumn", "Summer"]:
            raise ValueError("Race type does not exist!")

    @staticmethod
    def duplicate_name(name, collection, message):
        for c in collection:
            if c.name == name:
                raise Exception(message)

    @staticmethod
    def duplicate_race(race_types, horse_races, message):
        for t in horse_races:
            if t.race_type == race_types:
                raise Exception(message)

    @staticmethod
    def jockey_exist(jockey_name, jockeys, message):
        if all(j.name != jockey_name for j in jockeys):
            raise Exception(message)

    @staticmethod
    def horse_available(horse_type, horses, message):
        if all(h.is_taken for h in horses) or all(h.__class__.__name__ != horse_type for h in horses):
            raise Exception(message)

    @staticmethod
    def horse_race_exist(race_type, horse_races, message):
        if all(r.race_type != race_type for r in horse_races):
            raise Exception(message)

    @staticmethod
    def jockey_have_horse(jockey, message):
        if jockey.horse is None:
            raise Exception(message)

    @staticmethod
    def race_minimum_members(jockeys, message):
        if len(jockeys) < 2:
            raise Exception(message)




