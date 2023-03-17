from abc import ABC


class FormulaTeam(ABC):

    def __init__(self, budget):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError('F1 is an expensive sport, find more sponsors!')
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = self.sponsors.get(race_pos, 0) - self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
