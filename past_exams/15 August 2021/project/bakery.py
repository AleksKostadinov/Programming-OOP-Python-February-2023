from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Name cannot be empty string or white space!')
        self.__name = value

    def __find_food(self, name):
        food = next(filter(lambda x: x.name == name, self.food_menu), None)
        return food

    def __find_drink(self, name):
        drink = next(filter(lambda x: x.name == name, self.drinks_menu), None)
        return drink

    def __find_table(self, table_number):
        table = next(filter(lambda x: x.table_number == table_number, self.tables_repository), None)
        return table

    def add_food(self, food_type: str, name: str, price: float):
        food = self.__find_food(name)
        if food_type in ('Bread', 'Cake'):
            if food:
                raise Exception(f'{food_type} {name} is already in the menu!')

            if food_type == 'Bread':
                food = Bread(name, price)
            elif food_type == 'Cake':
                food = Cake(name, price)

            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        drink = self.__find_drink(name)
        if drink_type in ('Tea', 'Water'):
            if drink:
                raise Exception(f"{drink_type} {name} is already in the menu!")

            if drink_type == 'Tea':
                drink = Tea(name, portion, brand)
            elif drink_type == 'Water':
                drink = Water(name, portion, brand)

            self.drinks_menu.append(drink)
            return f'Added {name} ({brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self.__find_table(table_number)
        if table_type in ('InsideTable', 'OutsideTable'):
            if table:
                raise Exception(f"Table {table_number} is already in the bakery!")

            if table_type == 'InsideTable':
                table = InsideTable(table_number, capacity)
            elif table_type == 'OutsideTable':
                table = OutsideTable(table_number, capacity)

            self.tables_repository.append(table)
            return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        vacant_table = next(filter(lambda x: x.is_reserved is False and x.capacity >= number_of_people,
                                   self.tables_repository), None)
        if vacant_table:
            vacant_table.reserve(number_of_people)
            return f'Table {vacant_table.table_number} has been reserved for {number_of_people} people'

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table = self.__find_table(table_number)
        foods_in_menu, foods_not_in_menu = [], []

        if not table:
            return f"Could not find table {table_number}"

        for food_name in food_names:
            food = self.__find_food(food_name)
            if food:
                foods_in_menu.append(food.__repr__())
                table.order_food(food)
            else:
                foods_not_in_menu.append(food_name)

        result = [f'Table {table.table_number} ordered:']

        for item in foods_in_menu:
            result.append(item)

        result.append(f'{self.name} does not have in the menu:')

        for item in foods_not_in_menu:
            result.append(item)

        return '\n'.join(result)

    def order_drink(self, table_number: int, *drinks_names: str):
        table = self.__find_table(table_number)
        drinks_in_menu, drinks_not_in_menu = [], []

        if not table:
            return f"Could not find table {table_number}"

        for drink_name in drinks_names:
            drink = self.__find_drink(drink_name)
            if drink:
                drinks_in_menu.append(str(drink))
                table.order_drink(drink)
            else:
                drinks_not_in_menu.append(drink_name)

        result = [f'Table {table.table_number} ordered:']

        for item in drinks_in_menu:
            result.append(item)

        result.append(f'{self.name} does not have in the menu:')

        for item in drinks_not_in_menu:
            result.append(item)

        return '\n'.join(result)

    def leave_table(self, table_number: int):
        table = self.__find_table(table_number)
        bill = table.get_bill()
        result = [f'Table: {table_number}\nBill: {bill:.2f}']
        self.total_income += bill
        table.clear()

        return '\n'.join(result)

    def get_free_tables_info(self):
        vacant_tables = []

        for table in self.tables_repository:
            if table.is_reserved is False:
                vacant_tables.append(table.free_table_info())

        return '\n'.join(vacant_tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
