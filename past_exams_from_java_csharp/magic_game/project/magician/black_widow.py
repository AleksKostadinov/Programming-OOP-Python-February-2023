from project.magic.magic import Magic
from project.magician.magicians import Magician


class BlackWidow(Magician):
    def __init__(self, username, health, protection, magic: Magic):
        super().__init__(username, health, protection, magic)

    def take_damage(self, points: int):
        self.protection -= points
        if self.protection < 0:
            self.health += self.protection  # -
        if self.health <= 0:
            self.is_alive = False

