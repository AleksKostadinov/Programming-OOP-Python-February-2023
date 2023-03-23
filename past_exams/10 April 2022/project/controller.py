class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for p in players:
            if p not in self.players:
                added_players.append(p.name)
                self.players.append(p)
        return f"Successfully added: {', '.join(added_players)}"

    def __find_player(self, name):
        for p in self.players:
            if p.name == name:
                return p

    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    @staticmethod
    def __check_if_players_can_duel(*players):
        result = []
        for p in players:
            if p.stamina == 0:
                result.append(f"Player {p.name} does not have enough stamina.")
        # if result:
        return '\n'.join(result)

    @staticmethod
    def __attack(attacker, defender):
        defender.stamina -= attacker.stamina / 2

        if attacker.stamina - defender.stamina / 2 <= 0:
            attacker.stamina = 0
        else:
            attacker.stamina -= defender.stamina / 2

        if attacker.stamina < defender.stamina:
            return f'Winner: {defender.name}'
        else:
            return f'Winner: {attacker.name}'

    def add_supply(self, *supplies):
        for s in supplies:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."
        supply = self.__take_last_supply(sustenance_type)
        if supply:
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy

            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)
        not_ready_for_duel = self.__check_if_players_can_duel(first_player, second_player)

        if not_ready_for_duel:
            return not_ready_for_duel

        if first_player.stamina < second_player.stamina:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= p.age * 2
            self.sustain(p.name, 'Food')
            self.sustain(p.name, 'Drink')

    def __str__(self):
        result = []
        for p in self.players:
            result.append(f'{p}')

        for s in self.supplies:
            result.append(f'{s.details()}')

        return '\n'.join(result)
