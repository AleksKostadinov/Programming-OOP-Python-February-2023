from unittest import TestCase, main
from project.library import Library


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library('Public')

    def test_correct_init(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.library = Library('')
        self.assertEqual('Name cannot be empty string!', str(ve.exception))

    def test_add_book_valid(self):
        self.library.add_book('Philip K. Dick', 'Do Androids Dream of Electric Sheep?')
        self.assertEqual({'Philip K. Dick': ['Do Androids Dream of Electric Sheep?']}, self.library.books_by_authors)

        self.library.add_book('Douglas Adams', 'The Hitchhiker\'s Guide to the Galaxy')
        self.assertEqual({'Philip K. Dick': ['Do Androids Dream of Electric Sheep?'],
                          'Douglas Adams': ['The Hitchhiker\'s Guide to the Galaxy']}, self.library.books_by_authors)

        self.library.add_book('Philip K. Dick', 'The Man in the High Castle')
        self.assertEqual({'Philip K. Dick': ['Do Androids Dream of Electric Sheep?', 'The Man in the High Castle'],
                          'Douglas Adams': ['The Hitchhiker\'s Guide to the Galaxy']}, self.library.books_by_authors)

    def test_add_reader_valid(self):
        self.library.add_reader('Alex')
        self.assertEqual({'Alex': []}, self.library.readers)

        self.library.add_reader('Tsvety')
        self.assertEqual({'Alex': [], 'Tsvety': []}, self.library.readers)

    def test_add_reader_already_registered_raise_error(self):
        self.library.add_reader('Alex')
        result = self.library.add_reader('Alex')
        self.assertEqual("Alex is already registered in the Public library.", result)

    def test_rent_book_reader_not_registered(self):
        self.library.add_book('Philip K. Dick', 'The Man in the High Castle')
        result = self.library.rent_book('Alex', 'Philip K. Dick', 'The Man in the High Castle')
        self.assertEqual("Alex is not registered in the Public Library.", result)

    def test_rent_book_doesnt_have_by_this_author(self):
        self.library.add_reader('Alex')
        self.library.add_book('Philip K. Dick', 'The Man in the High Castle')
        result = self.library.rent_book('Alex', 'Ray Bradbury', 'Something Wicked This Way Comes')
        self.assertEqual("Public Library does not have any Ray Bradbury's books.",
                         result)

    def test_rent_book_doesnt_have_this_book(self):
        self.library.add_reader('Alex')
        self.library.add_book('Philip K. Dick', 'The Man in the High Castle')
        result = self.library.rent_book('Alex', 'Philip K. Dick', 'Do Androids Dream of Electric Sheep?')
        self.assertEqual("""Public Library does not have Philip K. Dick's "Do Androids Dream of Electric Sheep?".""",
                         result)

    def test_rent_book_valid(self):
        self.library.add_reader('Alex')
        self.library.add_book('Philip K. Dick', 'The Man in the High Castle')
        self.library.add_book('Philip K. Dick', 'Do Androids Dream of Electric Sheep?')
        self.library.rent_book('Alex', 'Philip K. Dick', 'The Man in the High Castle')

        self.assertEqual([{'Philip K. Dick': 'The Man in the High Castle'}], self.library.readers['Alex'])
        self.assertEqual({'Philip K. Dick': ['Do Androids Dream of Electric Sheep?']}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
