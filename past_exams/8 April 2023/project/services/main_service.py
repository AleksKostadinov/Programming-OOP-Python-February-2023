from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str, capacity=30):
        super().__init__(name, capacity)

    def details(self):
        result = [f'{self.name} Main Service:']
        if self.robots:
            result.append(f"Robots: {' '.join(robot.name for robot in self.robots)}")
        else:
            result.append(f'Robots: none')

        return '\n'.join(result)

