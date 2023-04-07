from unittest import TestCase, main

from project.library import Library


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library('Library1')

    def test_correct_init(self):
        self.assertEqual('Library1', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.library = Library('')
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_valid(self):
        self.library.add_book('Author1', 'Book1')
        self.assertEqual({'Author1': ['Book1']}, self.library.books_by_authors)

    def test_add_reader_valid(self):
        self.library.add_reader('Reader1')
        self.assertEqual({'Reader1': []}, self.library.readers)

    def test_add_reader_invalid_already_registered(self):
        self.library.readers = {'Reader1': []}
        result = self.library.add_reader('Reader1')
        self.assertEqual("Reader1 is already registered in the Library1 library.", result)

    def test_rent_book_valid(self):
        self.library.add_book('Author1', 'Book1')
        self.library.add_reader('Reader1')
        self.library.rent_book('Reader1', 'Author1', 'Book1')
        self.assertEqual({'Reader1': [{'Author1': 'Book1'}]}, self.library.readers)
        self.assertEqual({'Author1': []}, self.library.books_by_authors)

    def test_rent_book_invalid_user_is_not_registered(self):
        self.library.add_book('Author1', 'Book1')
        self.library.add_reader('Reader1')
        result = self.library.rent_book('Reader2', 'Author1', 'Book1')
        self.assertEqual("Reader2 is not registered in the Library1 Library.", result)

    def test_rent_book_invalid_library_does_not_have_any_author_book(self):
        self.library.add_book('Author1', 'Book1')
        self.library.add_reader('Reader1')
        result = self.library.rent_book('Reader1', 'Author2', 'Book1')
        self.assertEqual("Library1 Library does not have any Author2's books.", result)

    def test_rent_book_invalid_library_does_not_have_this_book(self):
        self.library.add_book('Author1', 'Book1')
        self.library.add_reader('Reader1')
        result = self.library.rent_book('Reader1', 'Author1', 'Book2')
        self.assertEqual("""Library1 Library does not have Author1's "Book2".""", result)


if __name__ == '__main__':
    main()
