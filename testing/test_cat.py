from unittest import main, TestCase


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat('Kitty')

    def test_size_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_if_cat_fed_cannot_eat_raise_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual('Already fed.', str(context.exception))

    def test_if_not_fed_cannot_asleep_raise_error(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_cat_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
