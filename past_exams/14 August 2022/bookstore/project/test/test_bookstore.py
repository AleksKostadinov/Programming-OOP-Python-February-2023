from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_correct_init(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)
        # self.assertEqual(self.bookstore.total_sold_books, self.bookstore._Bookstore__total_sold_books)
        # self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_books_limit_valid(self):
        self.bookstore.books_limit = 5
        self.assertEqual(5, self.bookstore.books_limit)

    def test_books_limit_le_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
            # store = Bookstore(0)
        self.assertEqual('Books limit of 0 is not valid', str(ve.exception))

    def test_count_books(self):
        self.bookstore.availability_in_store_by_book_titles = {'Title': 1, 'Title2': 2}
        self.assertEqual(3, len(self.bookstore))

    def test_receive_book_if_there_is_enough_bookstore(self):
        self.bookstore.availability_in_store_by_book_titles = {'Available Title': 2}
        result = self.bookstore.receive_book('Title', 3)
        self.assertEqual('3 copies of Title are available in the bookstore.', result)
        self.assertEqual(2, len(self.bookstore.availability_in_store_by_book_titles))

        result = self.bookstore.receive_book('Title', 2)
        self.assertEqual('5 copies of Title are available in the bookstore.', result)
        self.assertEqual(2, len(self.bookstore.availability_in_store_by_book_titles))

    def test_receive_book_if_there_is_not_enough_bookstore(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Title', 11)
        self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

    def test_sell_book_valid(self):
        self.bookstore.receive_book('Title', 1)
        result = self.bookstore.sell_book('Title', 1)
        self.assertEqual("Sold 1 copies of Title", result)
        self.assertEqual(1, self.bookstore.total_sold_books)
        self.assertEqual(0, len(self.bookstore))

    def test_sell_book_doesnt_exist(self):
        self.bookstore.receive_book('Title1', 1)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Title2', 1)
        self.assertEqual("Book Title2 doesn't exist!", str(ex.exception))

    def test_sell_book_not_enough_copies(self):
        self.bookstore.receive_book('Title', 1)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Title', 3)
        self.assertEqual("Title has not enough copies to sell. Left: 1", str(ex.exception))

    def test_str(self):
        self.bookstore.receive_book('Title', 2)
        self.bookstore.receive_book('OtherTitle', 4)
        self.bookstore.sell_book('Title', 1)
        self.bookstore.sell_book('OtherTitle', 2)
        self.assertEqual('Total sold books: 3\n'
                         'Current availability: 3\n'
                         ' - Title: 1 copies\n'
                         ' - OtherTitle: 2 copies',
                         str(self.bookstore)
                         )


if __name__ == "__main__":
    main()
