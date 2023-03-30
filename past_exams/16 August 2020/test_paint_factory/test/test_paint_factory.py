from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory('Factory', 100)

    def test_correct_init(self):
        self.assertEqual('Factory', self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual({}, self.factory.products)

    def test_add_ingredient_valid(self):
        self.factory.add_ingredient('white', 2)
        self.assertEqual({'white': 2}, self.factory.ingredients)

        self.factory.add_ingredient('green', 1)
        self.assertEqual({'white': 2, 'green': 1}, self.factory.ingredients)
        # self.assertEqual(100, self.factory.capacity)

    def test_add_ingredient_no_space(self):
        self.factory.capacity = 0
        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient('red', 1)
        self.assertEqual('Not enough space in factory', str(ve.exception))

    def test_add_ingredient_not_allowed_ingredient(self):
        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient('pink', 2)
        self.assertEqual('Ingredient of type pink not allowed in PaintFactory', str(te.exception))

    def test_remove_ingredient_valid(self):
        self.factory.add_ingredient('white', 2)
        self.factory.remove_ingredient('white', 1)
        self.assertEqual({'white': 1}, self.factory.ingredients)

    def test_remove_ingredient_cannot_be_less_than_zero(self):
        self.factory.add_ingredient('white', 0)
        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient('white', 1)
        self.assertEqual('Ingredients quantity cannot be less than zero', str(ve.exception))

    def test_remove_ingredient_no_such_ingredient(self):
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient('pink', 1)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))


if __name__ == "__main__":
    main()
