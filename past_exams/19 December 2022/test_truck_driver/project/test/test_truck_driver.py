from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver('Alex', 3)

    def test_correct_init(self):
        self.assertEqual('Alex', self.driver.name)
        self.assertEqual(3, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual(f'{self.driver.name} went bankrupt.', str(ve.exception))

    # def test_bankrupt(self):
    #     self.driver.money_per_mile = 0.01
    #     self.driver.add_cargo_offer("California", 2000)
    #     with self.assertRaises(ValueError) as ve:
    #         self.driver.drive_best_cargo_offer()
    #     self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer_valid(self):
        result = self.driver.add_cargo_offer('Milano', 1000)
        self.assertEqual('Cargo for 1000 to Milano was added as an offer.', result)
        self.assertEqual({'Milano': 1000}, self.driver.available_cargos)

    def test_add_cargo_offer_already_added(self):
        self.driver.add_cargo_offer('Milano', 1000)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Milano', 1000)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer('Sofia', 100)
        self.driver.add_cargo_offer('Milano', 1000)

        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("Alex is driving 1000 to Milano.", result)
        self.assertEqual(2875, self.driver.earned_money)
        self.assertEqual(1000, self.driver.miles)

    def test_drive_best_cargo_offer_invalid(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_eat(self):
        self.driver.earned_money = 100
        self.driver.eat(1000)
        self.assertEqual(80, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 100
        self.driver.sleep(1000)
        self.assertEqual(55, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(3000)
        self.assertEqual(500, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(20000)
        self.assertEqual(2500, self.driver.earned_money)

    def test_repr(self):
        self.assertEqual("Alex has 0 miles behind his back.", self.driver.__repr__())


if __name__ == "__main__":
    main()
