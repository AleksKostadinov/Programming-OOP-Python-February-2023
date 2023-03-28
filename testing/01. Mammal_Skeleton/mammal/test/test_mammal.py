from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('Sasheto', 'monkey', 'hoot')

    def test_correct_init(self):
        self.assertEqual('Sasheto', self.mammal.name)
        self.assertEqual('monkey', self.mammal.type)
        self.assertEqual('hoot', self.mammal.sound)

    def test_if_makes_sound(self):
        self.assertEqual('Sasheto makes hoot', self.mammal.make_sound())

    def test_if_gets_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_if_returns_info(self):
        self.assertEqual('Sasheto is of type monkey', self.mammal.info())


if __name__ == "__main__":
    main()
