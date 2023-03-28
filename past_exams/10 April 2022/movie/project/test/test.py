from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('The Shawshank Redemption', 1994, 9.2)

    def test_correct_init(self):
        self.assertEqual('The Shawshank Redemption', self.movie.name)
        self.assertEqual(1994, self.movie.year)
        self.assertEqual(9.2, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_cannot_be_empty(self):
        with self.assertRaises(ValueError) as ve:
            result = Movie('', 1994, 9.2)
        self.assertEqual('Name cannot be an empty string!', str(ve.exception))

    def test_year_if_before_1887(self):
        with self.assertRaises(ValueError) as ve:
            self.movie = Movie('The Shawshank Redemption', 1886, 9.2)
        self.assertEqual('Year is not valid!', str(ve.exception))
        # self.assertEqual(['Charlize Theron'], self.movie.actors)

    def test_added_actor_valid(self):
        self.movie.add_actor('Charlize Theron')
        self.assertEqual(['Charlize Theron'], self.movie.actors)

    def test_if_actor_is_already_added(self):
        self.movie.add_actor('Charlize Theron')
        result = self.movie.add_actor('Charlize Theron')
        self.assertEqual('Charlize Theron is already added in the list of actors!', result)
        self.assertEqual(['Charlize Theron'], self.movie.actors)

    def test__gt__the_rating_is_bigger(self):
        other_movie = Movie('The Godfather', 1972, 9.1)
        self.assertEqual('"The Shawshank Redemption" is better than "The Godfather"', self.movie.__gt__(other_movie))

    def test__gt__the_rating_is_lower(self):
        other_movie = Movie('Stranger Things', 2016, 9.3)
        self.assertEqual('"Stranger Things" is better than "The Shawshank Redemption"', self.movie.__gt__(other_movie))

    def test__repr__(self):
        self.movie.add_actor('Tim Robbins')
        self.movie.add_actor('Morgan Freeman')
        self.assertEqual(
            "Name: The Shawshank Redemption\n"
            "Year of Release: 1994\n"
            "Rating: 9.20\n"
            "Cast: Tim Robbins, Morgan Freeman",
            self.movie.__repr__()
        )


if __name__ == "__main__":
    main()
