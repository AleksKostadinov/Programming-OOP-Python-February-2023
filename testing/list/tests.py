from unittest import TestCase, main
from testing.list.integer_list import IntegerList


class IntegerListTests(TestCase):
    def test_correct_init(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], int_list._IntegerList__data)

    def test_not_correct_init(self):
        int_list = IntegerList(1.5, 'foo', '3')
        self.assertEqual([], int_list._IntegerList__data)

    def test_add_ele(self):
        int_list = IntegerList(1, 2, 3)
        int_list.add(4)
        # self.assertEqual([1, 2, 3, 4], int_list._IntegerList__data)
        self.assertEqual([1, 2, 3, 4], int_list.get_data())

    def test_unsuccessful_add_ele(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ex:
            int_list.add('foo')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_ele(self):
        int_list = IntegerList(1, 2, 3)
        int_list.remove_index(2)
        self.assertEqual([1, 2], int_list.get_data())

    def test_unsuccessful_remove_ele(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            int_list.remove_index(3)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_ele(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual(3, int_list.get(2))

    def test_unsuccessful_get_ele(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            int_list.get(3)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_ele(self):
        int_list = IntegerList(1, 2, 3)
        int_list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3], int_list.get_data())

    def test_unsuccessful_insert_ele_not_valid_index(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            int_list.insert(10, 10)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_unsuccessful_insert_ele_not_int(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            int_list.insert(0, '0')
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_get_biggest(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual(3, int_list.get_biggest())

    def test_get_ele_index(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual(2, int_list.get_index(3))


if __name__ == "__main__":
    main()
