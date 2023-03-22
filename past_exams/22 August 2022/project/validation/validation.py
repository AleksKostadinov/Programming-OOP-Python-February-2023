class Validation:
    @staticmethod
    def validate_phone_number(text, message):
        if not text.startswith('0') or len(text) != 10 or not text.isdigit():
            raise ValueError(message)

    @staticmethod
    def empty_str(text, message):
        if text.strip() == '':
            raise ValueError(message)

    @staticmethod
    def le_0(number, message):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def meal_in_menu(meal_names_and_quantities, menu_info):
        for meal in meal_names_and_quantities.keys():
            if meal not in menu_info:
                raise Exception(f'{meal} is not on the menu!')

    @staticmethod
    def is_enough_quantity(meal_names_and_quantities, menu_info):
        for meal, quantity in meal_names_and_quantities.items():
            if quantity > menu_info[meal].quantity:
                raise Exception(f"Not enough quantity of {menu_info[meal].__class__.__name__}: {meal}!")

    @staticmethod
    def empty_shopping_cart(data):
        if not data:
            raise Exception("There are no ordered meals!")

    @staticmethod
    def menu_lt_5(text):
        if len(text) < 5:
            raise ValueError('The menu is not ready!')
