from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_correct_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_add_toy_valid(self):
        result = self.toy_store.add_toy('A', 'Pateto Coco')
        self.assertEqual('Toy:Pateto Coco placed successfully!', result)
        self.assertEqual({
            "A": 'Pateto Coco',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_add_toy_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('Z', 'Pateto Coco')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_taken(self):
        self.toy_store.add_toy('A', 'Pateto Coco')
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Pateto Coco')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_shelf_taken(self):
        self.toy_store.add_toy('A', 'Pateto Coco')
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Snake')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_remove_toy_valid(self):
        self.toy_store.add_toy('A', 'Pateto Coco')
        result = self.toy_store.remove_toy('A', 'Pateto Coco')
        self.assertEqual('Remove toy:Pateto Coco successfully!', result)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_remove_toy_shelf_doesnt_exist(self):
        self.toy_store.add_toy('A', 'Pateto Coco')
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('Z', 'Pateto Coco')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_doesnt_exist(self):
        self.toy_store.add_toy('A', 'Pateto Coco')
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'Snake')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))


if __name__ == "__main__":
    main()
