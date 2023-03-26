import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    def test_initialized(self):
        worker = Worker('John Doe', 1000, 100)
        self.assertEqual('John Doe', worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(100, worker.energy)

    def test_energy_is_incremented(self):
        worker = Worker('John Doe', 1000, 100)
        self.assertEqual(100, worker.energy)
        worker.rest()
        self.assertEqual(101, worker.energy)

    def test_if_can_work_with_negative_energy(self):
        worker = Worker('John Doe', 1000, -1)
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual('Not enough energy.', str(context.exception))

    def test_increased_salary(self):
        worker = Worker('John Doe', 1000, 100)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(1000, worker.money)

    def test_decreased_energy(self):
        worker = Worker('John Doe', 1000, 100)
        self.assertEqual(100, worker.energy)
        worker.work()
        self.assertEqual(99, worker.energy)

    def test_proper_string(self):
        worker = Worker('John Doe', 1000, 100)
        self.assertEqual('John Doe has saved 0 money.', worker.get_info())


if __name__ == '__main__':
    unittest.main()
