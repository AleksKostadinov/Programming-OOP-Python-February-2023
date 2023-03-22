from project.band_members.musician import Musician


class Singer(Musician):
    # def __init__(self, name, age):
    #     super().__init__(name, age)
    #
    # @property
    # def available_skills(self):
    #     return "sing high pitch notes", "sing low pitch notes"

    AVAILABLE_SKILLS = (
        "sing high pitch notes",
        "sing low pitch notes",
    )

    def learn_new_skill(self, new_skill):
        if new_skill not in self.AVAILABLE_SKILLS:
            raise ValueError(f'{new_skill} is not a needed skill!')

        elif new_skill in self.skills:
            raise Exception(f'{new_skill} is already learned!')

        self.skills.append(new_skill)
        return f'{self.name} learned to {new_skill}.'
