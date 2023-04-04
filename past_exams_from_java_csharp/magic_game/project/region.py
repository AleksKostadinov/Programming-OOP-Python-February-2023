from project.magician.black_widow import BlackWidow
from project.magician.magicians import Magician
from project.magician.wizard import Wizard


class Region:
    def __init__(self):
        self.wizards = []
        self.black_widows = []

    def start(self, magicians: Magician):
        self.wizards = [magician for magician in magicians if magician.magician_type == 'Wizard']
        self.black_widows = [magician for magician in magicians if magician.magician_type == 'BlackWidow']
        while self.wizards and self.black_widows:
            for wizard in self.wizards:
                if wizard.health > 0:
                    black_widow = self._select_target(self.black_widows)
                    if black_widow is not None:
                        damage = wizard.magic.bullets_count * wizard.magic.magic_type.damage_multiplier
                        self._inflict_damage(black_widow, damage)
            for black_widow in self.black_widows:
                if black_widow.health > 0:
                    wizard = self._select_target(self.wizards)
                    if wizard is not None:
                        damage = black_widow.magic.bullets_count * black_widow.magic.magic_type.damage_multiplier
                        self._inflict_damage(wizard, damage)
        if self.wizards:
            return "Wizards win!"
        else:
            return "Black widows win!"

    @staticmethod
    def _select_target(magicians: Magician):
        living_magicians = [magician for magician in magicians if magician.health > 0]
        if living_magicians:
            return min(living_magicians, key=lambda magician: magician.health)
        else:
            return None

    @staticmethod
    def _inflict_damage(magician: 'Magician', damage: int):
        actual_damage = max(damage - magician.protection, 0)
        magician.health = max(magician.health - actual_damage, 0)
