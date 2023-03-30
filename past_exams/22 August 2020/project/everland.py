from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumptions = 0
        for room in self.rooms:
            total_consumptions += room.expenses
            total_consumptions += room.room_cost
        return f'Monthly consumption: {total_consumptions:.2f}$.'

    def pay(self):
        result = []
        for room in self.rooms:
            consumption = room.expenses + room.room_cost
            if consumption <= room.budget:
                room.budget -= consumption
                result.append(f'{room.family_name} paid {consumption:.2f}$ and have {room.budget:.2f}$ left.')
            else:
                result.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
                self.rooms.remove(room)
        return '\n'.join(result)

    def status(self):
        result = []
        total_members = sum([room.members_count for room in self.rooms])
        result.append(f'Total population: {total_members}')
        for room in self.rooms:
            result.append(f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, '
                          f'Expenses: {room.expenses:.2f}$')
            for child in room.children:
                result.append(f"--- Child {room.children.index(child) + 1} monthly cost: {child.cost * 30:.2f}$")
            if hasattr(room, 'appliances'):
                result.append(
                    f"--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances]):.2f}$")
        return '\n'.join(result)



