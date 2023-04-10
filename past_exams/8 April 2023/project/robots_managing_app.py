from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def __find_robot_by_name(self, name):
        for r in self.robots:
            if r.name == name:
                return r

    def __find_service_by_name(self, name):
        for s in self.services:
            if s.name == name:
                return s

    def add_service(self, service_type: str, name: str):
        if service_type == 'MainService':
            new_service = MainService(name)
        elif service_type == 'SecondaryService':
            new_service = SecondaryService(name)
        else:
            raise Exception("Invalid service type!")

        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type == 'MaleRobot':
            new_robot = MaleRobot(name, kind, price)
        elif robot_type == 'FemaleRobot':
            new_robot = FemaleRobot(name, kind, price)
        else:
            raise Exception("Invalid robot type!")

        self.robots.append(new_robot)
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_robot_by_name(robot_name)
        service = self.__find_service_by_name(service_name)

        if type(robot).__name__ == 'FemaleRobot' and type(service).__name__ == 'MainService':
            return "Unsuitable service."
        elif type(robot).__name__ == 'MaleRobot' and type(service).__name__ == 'SecondaryService':
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service_by_name(service_name)
        robot = next(filter(lambda r: r.name == robot_name, service.robots), None)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service_by_name(service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service_by_name(service_name)
        total_price = 0
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for s in self.services:
            result.append(s.details())

        return '\n'.join(result)
