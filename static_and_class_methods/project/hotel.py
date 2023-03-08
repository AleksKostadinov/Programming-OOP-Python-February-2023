from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    # @classmethod
    # def from_stars(cls, stars_count: int):
    #     return cls(f"{stars_count} stars Hotel")

    @staticmethod
    def from_stars(stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        # var.1 [room.take_room(people) for room in self.rooms if room.number == room_number]
        # var.2 room = next(filter(lambda r: r.number == room_number, self.rooms))
        # var.2     result = room.take_room(people)
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        free_rooms, taken_rooms = [], []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
                self.guests += room.guests
            else:
                free_rooms.append(room.number)

        result = [f'Hotel {self.name} has {self.guests} total guests',
                  f'Free rooms: {", ".join(map(str, free_rooms))}',
                  f'Taken rooms: {", ".join(map(str, taken_rooms))}']
        return '\n'.join(map(str, result))

        # return f"Hotel {self.name} has {self.guests} total guests\n" \
        #        f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n" \
        #        f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"