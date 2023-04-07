from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    # LIVE_IN = 'SaltwaterAquarium'

    def __init__(self, name: str, species: str, price: float, size=5):
        super().__init__(name, species, size, price)

    def eat(self):
        self.size += 2
