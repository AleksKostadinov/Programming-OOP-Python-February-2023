from math import log2

from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    POSSIBLE_RAM = [2, 4, 8, 16, 32, 64, 128]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f'{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!')
        elif ram not in self.POSSIBLE_RAM:
            raise ValueError(f'{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!')
        else:
            self.processor = processor
            self.ram = ram
            self.price += self.AVAILABLE_PROCESSORS[processor] + int(log2(ram)) * 100
            return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
