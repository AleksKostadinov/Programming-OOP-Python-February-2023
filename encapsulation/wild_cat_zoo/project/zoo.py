from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_cost = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_care_cost:
            self.__budget -= total_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda a: a.__class__.__name__ == 'Lion', self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == 'Tiger', self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == 'Cheetah', self.animals))

        result = [f'You have {len(self.animals)} animals']

        result.append(f'----- {len(lions)} Lions:')
        result.extend(lions)

        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(tigers)

        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(cheetahs)

        return '\n'.join(list(map(str, result)))

    def workers_status(self):
        keepers = list(filter(lambda a: a.__class__.__name__ == 'Keeper', self.workers))
        caretakers = list(filter(lambda a: a.__class__.__name__ == 'Caretaker', self.workers))
        vets = list(filter(lambda a: a.__class__.__name__ == 'Vet', self.workers))

        result = [f'You have {len(self.workers)} workers']

        result.append(f'----- {len(keepers)} Keepers:')
        result.extend(keepers)

        result.append(f'----- {len(caretakers)} Caretakers:')
        result.extend(caretakers)

        result.append(f'----- {len(vets)} Vets:')
        result.extend(vets)

        return '\n'.join(list(map(str, result)))
