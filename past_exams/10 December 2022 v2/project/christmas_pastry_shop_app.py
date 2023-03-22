from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.validation.validation import Validation


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    @property
    def __type_delicacy(self):
        return {"Gingerbread": Gingerbread,
                "Stolen": Stolen}

    @property
    def __type_booth(self):
        return {"Open Booth": OpenBooth,
                "Private Booth": PrivateBooth}

    def __find_booth(self, booth_number):
        for b in self.booths:
            if b.booth_number == booth_number:
                return b

    def __find_delicacy(self, delicacy_name):
        for d in self.delicacies:
            if d.name == delicacy_name:
                return d

    def __not_reserved(self, number_of_people,):
        for b in self.booths:
            if not b.is_reserved and b.capacity >= number_of_people:
                return b

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        Validation.duplicates_name(name, self.delicacies, f"{name} already exists!")
        Validation.not_valid_type(type_delicacy, self.__type_delicacy, f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.__type_delicacy[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        Validation.duplicates_num(booth_number, self.booths, f"Booth number {booth_number} already exists!")
        Validation.not_valid_type(type_booth, self.__type_booth, f"{type_booth} is not a valid booth!")

        booth = self.__type_booth[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        booth = self.__not_reserved(number_of_people)

        Validation.not_found(booth, f'No available booth for {number_of_people} people!')
        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth(booth_number)
        Validation.not_found(booth, f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy(delicacy_name)
        Validation.not_found(delicacy, f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth(booth_number)
        bill = booth.calculate_bill()
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        self.income += bill
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
