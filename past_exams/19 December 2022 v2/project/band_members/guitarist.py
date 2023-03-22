from project.band_members.musician import Musician
from project.validation.validation import Validation


class Guitarist(Musician):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def available_skills(self):
        return "play metal", "play rock", "play jazz"

    def learn_new_skill(self, new_skill):
        Validation.check_not_in(new_skill, self.available_skills, f"{new_skill} is not a needed skill!")
        Validation.check_in(new_skill, self.skills, f"{new_skill} is already learned!")

        self.skills.append(new_skill)
        return f'{self.name} learned to {new_skill}.'
