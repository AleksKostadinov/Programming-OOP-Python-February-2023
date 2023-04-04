from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Movie', 1999, 6.0)

    def test_correct_init(self):
        self.assertEqual('Movie', self.movie.name)
        self.assertEqual(1999, self.movie.year)
        self.assertEqual(6.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_valid(self):
        pass

    def test_name_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual('Name cannot be an empty string!', str(ve.exception))

    def test_year_valid(self):
        pass

    def test_year_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 666
        self.assertEqual('Year is not valid!', str(ve.exception))

    def test_add_valid(self):
        self.movie.actors = []
        self.movie.add_actor('Alex')
        self.assertEqual(['Alex'], self.movie.actors)

    def test_add_invalid(self):
        self.movie.actors = ['Alex']
        result = self.movie.add_actor('Alex')
        self.assertEqual('Alex is already added in the list of actors!', result)
        self.assertEqual(['Alex'], self.movie.actors)

    def test__gt__o(self):
        other = Movie('Other', 1995, 5.00)
        self.assertEqual('"Movie" is better than "Other"', self.movie.__gt__(other))

    def test__gt__s(self):
        other = Movie('Other', 1995, 7.00)
        self.assertEqual('"Other" is better than "Movie"', self.movie.__gt__(other))

    def test__repr__(self):
        self.movie.add_actor('Alex')
        self.assertEqual(
            "Name: Movie\n"
            "Year of Release: 1999\n"
            "Rating: 6.00\n"
            "Cast: Alex",
            self.movie.__repr__()
        )


if __name__ == '__main__':
    main()
