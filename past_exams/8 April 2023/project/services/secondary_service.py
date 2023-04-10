from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str, capacity=15):
        super().__init__(name, capacity)

    def details(self):
        result = [f'{self.name} Secondary Service:']
        if self.robots:
            result.append(f"Robots: {' '.join(robot.name for robot in self.robots)}")
        else:
            result.append(f'Robots: none')

        return '\n'.join(result)
