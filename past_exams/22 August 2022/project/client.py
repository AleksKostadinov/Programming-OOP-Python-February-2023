from project.validation.validation import Validation


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        Validation.validate_phone_number(value, f"Invalid phone number!")
        self.__phone_number = value
