from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        for c in self.clients_list:
            if c.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f'Client {client.phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ("Starter", "MainDish", "Dessert"):
                self.menu.append(meal)

    def show_menu(self):
        result = []
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        for meal in self.menu:
            result.append(meal.details())

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        meals, price = [], 0

        for meal_name, quantity in meal_names_and_quantities.items():
            meal_found = False
            for meal in self.menu:
                if meal.name == meal_name:
                    meal_found = True
                    meals.append([meal, quantity])
                    price += meal.price * quantity
            if not meal_found:
                raise Exception(f'{meal_name} is not on the menu!')

            for current_meal in meals:
                if current_meal[0].quantity < quantity:
                    raise Exception(
                        f"Not enough quantity of {current_meal[0].__class__.__name__}: {current_meal[0].name}!")

        for ordered_meal, quantity in meals:
            ordered_meal.quantity -= quantity
            client.shopping_cart.append(ordered_meal)
        client.bill += price
        client.ordered_meals += meals
        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for ordered_meal, quantity in client.ordered_meals:
            ordered_meal.quantity += quantity

        client.bill = 0
        client.shopping_cart = []
        client.ordered_meals = []
        return f'Client {client_phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception(f"There are no ordered meals!")

        total_paid_money = client.bill
        client.bill = 0
        client.ordered_meals = []
        client.shopping_cart = []
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
