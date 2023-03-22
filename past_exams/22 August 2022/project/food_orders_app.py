from project.client import Client
from project.meals.meal import Meal
from project.validation.validation import Validation


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 1

    def __get_or_create_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return new_client

    def __get_menu(self):
        return {meal.name: meal for meal in self.menu}

    @staticmethod
    def __reset_client_info(client):
        client.bill = 0
        client.shopping_cart = []
        client.ordered_meals = {}

    def register_client(self, client_phone_number: str):
        for c in self.clients_list:
            if c.phone_number == client_phone_number:
                raise Exception('The client has already been registered!')
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        Validation.menu_lt_5(self.menu)

        result = []
        for meal in self.menu:
            result.append(meal.details())

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        Validation.menu_lt_5(self.menu)

        find_client = self.__get_or_create_client(client_phone_number)
        menu_info = self.__get_menu()

        Validation.meal_in_menu(meal_names_and_quantities, menu_info)
        Validation.is_enough_quantity(meal_names_and_quantities, menu_info)

        for name, qty in meal_names_and_quantities.items():
            menu_info[name].quantity -= qty
            find_client.shopping_cart.append(menu_info[name])

        find_client.bill += sum(menu_info[name].price * qty for name, qty in meal_names_and_quantities.items())
        find_client.ordered_meals.update(meal_names_and_quantities)

        return f"Client {client_phone_number} successfully ordered {', '.join(find_client.ordered_meals)} for {find_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__get_or_create_client(client_phone_number)
        Validation.empty_shopping_cart(client.shopping_cart)

        menu_info = self.__get_menu()
        for name, qty in client.ordered_meals.items():
            menu_info[name].quantity += qty

        self.__reset_client_info(client)

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__get_or_create_client(client_phone_number)
        Validation.empty_shopping_cart(client.shopping_cart)
        current_receipt = self.receipt_id
        self.receipt_id += 1
        total_paid_money = client.bill
        self.__reset_client_info(client)

        return f"Receipt #{current_receipt} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
