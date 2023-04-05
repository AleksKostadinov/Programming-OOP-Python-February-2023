from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_car_by_model(self, model):
        for car in self.cars:
            if car.model == model:
                return car

    def __find_car_by_type(self, car_type):
        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        return None

    def __find_driver_by_name(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def __find_driver_by_car(self, car):
        for driver in self.drivers:
            if driver.car == car:
                return driver

    def __find_race_by_name(self, name):
        for race in self.races:
            if race.name == name:
                return race

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.__find_car_by_model(model)
        if car:
            raise Exception(f'Car {model} is already created!')
        if car_type == 'MuscleCar':
            new_car = MuscleCar(model, speed_limit)
        elif car_type == 'SportsCar':
            new_car = SportsCar(model, speed_limit)
        else:
            return

        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if race:
            raise Exception(f'Race {race_name} is already created!')

        new_race = Race(race_name)
        self.races.append(new_race)
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type in ('MuscleCar', 'SportsCar'):
            car = self.__find_car_by_type(car_type)
            if not car:
                raise Exception(f"Car {car_type} could not be found!")

            if driver.car:
                old_car = driver.car
                old_car.is_taken = False
                driver.car = car
                car.is_taken = True
                return f"Driver {driver.name} changed his car from {old_car.model} to {driver.car.model}."
            else:
                driver.car = car
                car.is_taken = True
                return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = self.__find_driver_by_name(driver_name)
        race = self.__find_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f'Driver {driver_name} could not participate in the race!')

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_cars = sorted(self.cars, key=lambda x: -x.speed_limit)[:3]

        result = []

        for fast_car in fastest_cars:
            driver = self.__find_driver_by_car(fast_car)
            driver.number_of_wins += 1
            result.append(f'Driver {driver.name} wins the {race_name} race with a speed of {fast_car.speed_limit}.')

        return '\n'.join(result)
