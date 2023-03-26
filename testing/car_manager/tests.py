from unittest import TestCase, main
from testing.car_manager.car_manager import Car


class CarTests(TestCase):

    def setUp(self) -> None:
        self.car = Car("VW", "CC", 8, 70)

    def test_correct_init(self):
        self.assertEqual('VW', self.car.make)
        self.assertEqual('CC', self.car.model)
        self.assertEqual(8, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_valid_make_init(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_valid_model_init(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_no_valid_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_no_valid_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_no_valid_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_refuel(self):
        self.car.refuel(50)
        self.assertEqual(50, self.car.fuel_amount)

    def test_no_valid_refuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive(self):
        self.car.fuel_amount = 8
        self.car.drive(100)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_valid_drive(self):
        self.car.fuel_amount = 8
        with self.assertRaises(Exception) as ex:
            self.car.drive(200)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
