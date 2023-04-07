from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop('Shoppy')

    def test_correct_init(self):
        self.assertEqual('Shoppy', self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_v(self):
        result = self.shop.add_food('Food1', 200.00)
        self.assertEqual("Successfully added 200.00 grams of Food1.", result)
        self.assertEqual(200.00, self.shop.food['Food1'])
        self.assertEqual({'Food1': 200.00}, self.shop.food)

    def test_add_food_le0(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food('Food1', 0.00)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_pet_v(self):
        result = self.shop.add_pet('Philip')
        self.assertEqual('Successfully added Philip.', result)
        self.assertEqual(['Philip'], self.shop.pets)

    def test_add_pet_same_name(self):
        self.shop.pets = ['Philip']
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet('Philip')
        self.assertEqual('Cannot add a pet with the same name', str(ex.exception))

    def test_feed_pet_v(self):
        self.shop.pets = ['Alex']
        self.shop.food = {'Food1': 200.00}
        result = self.shop.feed_pet('Food1', 'Alex')
        self.assertEqual("Alex was successfully fed", result)
        self.assertEqual({'Food1': 100.00}, self.shop.food)
        self.assertEqual(100.00, self.shop.food['Food1'])

    def test_feed_pet_not_v_name(self):
        self.shop.pets = ['Alex']
        self.shop.food = {'Food1': 200.00}
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('Food1', 'Tsvety')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_not_food(self):
        self.shop.pets = ['Tsvety']
        self.shop.food = {'Food1': 200.00}
        result = self.shop.feed_pet('Food2', 'Tsvety')
        self.assertEqual("You do not have Food2", result)

    def test_feed_pet_add_food(self):
        self.shop.pets = ['Tsvety']
        self.shop.food = {'Food1': 50.00}
        result = self.shop.feed_pet('Food1', 'Tsvety')
        self.assertEqual("Adding food...", result)
        self.assertEqual({'Food1': 1050.00}, self.shop.food)
        self.assertEqual(1050, self.shop.food['Food1'])

    def test_repr(self):
        self.shop.pets = ['Tsvety', 'Alex']
        self.assertEqual(
            'Shop Shoppy:\n'
            'Pets: Tsvety, Alex',
            self.shop.__repr__()
        )


if __name__ == '__main__':
    main()
