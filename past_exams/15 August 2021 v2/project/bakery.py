from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def __find_food_by_name(self, name):
        for f in self.food_menu:
            if f.name == name:
                return f

    def __find_drink_by_name(self, name):
        for d in self.drinks_menu:
            if d.name == name:
                return d

    def __find_table_by_number(self, number):
        for t in self.tables_repository:
            if t.table_number == number:
                return t

    def add_food(self, food_type: str, name: str, price: float):
        food = self.__find_food_by_name(name)

        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type == 'Bread':
            new_food = Bread(name, price)
        elif food_type == 'Cake':
            new_food = Cake(name, price)
        else:
            return

        self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        drink = self.__find_drink_by_name(name)

        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == 'Tea':
            new_drink = Tea(name, portion, brand)
        elif drink_type == 'Water':
            new_drink = Water(name, portion, brand)
        else:
            return

        self.drinks_menu.append(new_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self.__find_table_by_number(table_number)

        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == 'InsideTable':
            new_table = InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            new_table = OutsideTable(table_number, capacity)
        else:
            return

        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for t in self.tables_repository:
            if not t.is_reserved and t.capacity >= number_of_people:
                t.reserve(number_of_people)
                return f"Table {t.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table = self.__find_table_by_number(table_number)
        food_in_menu, food_not_in_menu = [], []

        if not table:
            return f"Could not find table {table_number}"

        for food_name in food_names:
            food = self.__find_food_by_name(food_name)
            if food:
                food_in_menu.append(food.__repr__())
                table.order_food(food)
            else:
                food_not_in_menu.append(food_name)

        result = [f'Table {table_number} ordered:']

        for item in food_in_menu:
            result.append(item)

        result.append(f'{self.name} does not have in the menu:')

        for item in food_not_in_menu:
            result.append(item)

        return '\n'.join(result)

    def order_drink(self, table_number: int, *drinks_names: str):
        table = self.__find_table_by_number(table_number)
        drink_in_menu, drink_not_in_menu = [], []

        if not table:
            return f"Could not find table {table_number}"

        for drink_name in drinks_names:
            drink = self.__find_drink_by_name(drink_name)
            if drink:
                drink_in_menu.append(drink.__repr__())
                table.order_drink(drink)
            else:
                drink_not_in_menu.append(drink_name)

        result = [f'Table {table_number} ordered:']

        for item in drink_in_menu:
            result.append(item)

        result.append(f'{self.name} does not have in the menu:')

        for item in drink_not_in_menu:
            result.append(item)

        return '\n'.join(result)

    def leave_table(self, table_number: int):
        table = self.__find_table_by_number(table_number)

        if table:
            bill = table.get_bill()
            result = [f"Table: {table_number}", f"Bill: {bill:.2f}"]
            self.total_income += bill
            table.clear()

            return '\n'.join(result)

    def get_free_tables_info(self):
        return '\n'.join(t.free_table_info() for t in self.tables_repository)
        # vacant_tables = []
        # for table in self.tables_repository:
        #     vacant_tables.append(table.free_table_info())
        # return '\n'.join(vacant_tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
