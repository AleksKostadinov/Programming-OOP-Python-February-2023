from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    default_room_members = 2
    room_cost = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, self.default_room_members + len(children))

        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * (2 + len(children))
        self.calculate_expenses(self.appliances + self.children)
