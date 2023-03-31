from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if sum(s.capacity_consumption for s in self.software_components) + software.capacity_consumption > \
                self.capacity or sum(s.memory_consumption for s in self.software_components)\
                + software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def __str__(self):
        result = [f"Hardware Component - {self.name}",
                  f"Express Software Components: {sum(1 for s in self.software_components if s.software_type == 'Express')}",
                  f"Light Software Components: {sum(1 for s in self.software_components if s.software_type == 'Light')}",
                  f"Memory Usage: {sum(s.memory_consumption for s in self.software_components)} / {self.memory}",
                  f"Capacity Usage: {sum(s.capacity_consumption for s in self.software_components)} / {self.capacity}",
                  f"Type: {self.hardware_type}",
                  f"Software Components: "]

        if self.software_components:
            result[-1] += ", ".join(s.name for s in self.software_components)
        else:
            result[-1] += "None"

        return "\n".join(result)
