from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10, 170)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(170, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_enough_fuel(self):
        self.vehicle.drive(1)
        self.assertEqual(8.75, self.vehicle.fuel)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_correct(self):
        self.vehicle.refuel(0)
        self.assertEqual(10, self.vehicle.fuel)

    def test_refuel_too_much_incorrect(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correct_str(self):
        self.assertEqual('The vehicle has 170 horse power with 10 '
                         'fuel left and 1.25 fuel consumption', self.vehicle.__str__())


if __name__ == "__main__":
    main()
