from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []  # An empty list that will contain all the players (objects)
        self.supplies = []  # An empty list that will contain all the supplies (objects)

    def __last_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)

    def __find_player(self, name):
        for p in self.players:
            if p.name == name:
                return p

    def add_player(self, *players: Player):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)
        # if added_players:
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies: Supply):
        self.supplies.extend(supplies)
        # self.supplies += list(supplies)
        # [self.supplies.append(s) for s in supplies]

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)

        if player.stamina == 100:
            return f"{player.name} have enough stamina."

        supply = self.__last_supply(sustenance_type)

        if not player:
            return

        if sustenance_type not in ("Food", "Drink"):
            return

        if supply:
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy

            return f'{player.name} sustained successfully with {supply.name}.'

        raise Exception(f'There are no {sustenance_type.lower()} supplies left!')

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)

        result = []

        for p in [first_player, second_player]:
            if p.stamina == 0:
                result.append(f"Player {p.name} does not have enough stamina.")

        if result:
            return '\n'.join(result)

        # player with lower stamina attacks first
        if first_player.stamina > second_player.stamina:
            first_player, second_player = second_player, first_player

        # attacks / if stamina is 0 finish battle else continue
        if second_player.stamina - (first_player.stamina / 2) <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"
        else:
            second_player.stamina -= first_player.stamina / 2

        if first_player.stamina - (second_player.stamina / 2) <= 0:
            first_player.stamina = 0
            return f"Winner: {second_player.name}"
        else:
            first_player.stamina -= second_player.stamina / 2

        # finish battle
        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        else:
            return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = []
        for p in self.players:
            result.append(p.__str__())

        for s in self.supplies:
            result.append(s.details())

        return '\n'.join(result)
