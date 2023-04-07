from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    # LIVE_IN = 'FreshwaterAquarium'

    def __init__(self, name: str, species: str, price: float, size=3):
        super().__init__(name, species, size, price)

    def eat(self):
        self.size += 3
