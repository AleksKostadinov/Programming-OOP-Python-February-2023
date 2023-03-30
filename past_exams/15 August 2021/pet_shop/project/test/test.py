from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('Pet')

    def test_correct_init(self):
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_valid(self):
        result = self.pet_shop.add_food('Food1', 50)
        self.assertEqual("Successfully added 50.00 grams of Food1.", result)
        self.assertEqual({'Food1': 50}, self.pet_shop.food)

    def test_add_food_food_le_zero(self):
        with self.assertRaises(ValueError) as ve:
            result = self.pet_shop.add_food('Food1', 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_pet_valid(self):
        result = self.pet_shop.add_pet('Pet1')
        self.assertEqual("Successfully added Pet1.", result)
        self.assertEqual(['Pet1'], self.pet_shop.pets)

    def test_add_pet_same_name(self):
        self.pet_shop.add_pet('Pet1')
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('Pet1')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(['Pet1'], self.pet_shop.pets)

    def test_add_feed_pet_valid(self):
        self.pet_shop.add_food('Food1', 500)
        self.pet_shop.add_pet('Pet1')
        result = self.pet_shop.feed_pet('Food1', 'Pet1')
        self.assertEqual('Pet1 was successfully fed', result)
        self.assertEqual(400, self.pet_shop.food['Food1'])

    def test_add_feed_pet_insert_valid_name(self):
        self.pet_shop.add_food('Food1', 500)
        self.pet_shop.add_pet('Pet1')

        with self.assertRaises(Exception) as ex:
            result = self.pet_shop.feed_pet('Food1', 'Pet2')
        self.assertEqual('Please insert a valid pet name', str(ex.exception))

    def test_add_feed_pet_dont_have_this_food(self):
        self.pet_shop.add_food('Food1', 500)
        self.pet_shop.add_pet('Pet1')
        result = self.pet_shop.feed_pet('Food2', 'Pet1')
        self.assertEqual('You do not have Food2', result)

    def test_add_feed_pet_add_more_food(self):
        self.pet_shop.add_food('Food1', 50)
        self.pet_shop.add_pet('Pet1')
        result = self.pet_shop.feed_pet('Food1', 'Pet1')
        self.assertEqual('Adding food...', result)
        self.assertEqual(1050, self.pet_shop.food['Food1'])

    def test__repr__(self):
        self.pet_shop = PetShop('PetShop')
        self.pet_shop.add_pet('Alex')
        self.pet_shop.add_pet('Tsvety')
        self.pet_shop.add_food('Meat', 100)
        self.assertEqual(
            'Shop PetShop:\n'
            'Pets: Alex, Tsvety',
            self.pet_shop.__repr__()
        )



