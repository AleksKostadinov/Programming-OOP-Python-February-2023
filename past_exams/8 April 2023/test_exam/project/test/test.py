from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Alex', 36, 100.00)
        # self.player2 = TennisPlayer('Ani', 16, 50.00)

    def test_correct_init(self):
        self.assertEqual('Alex', self.player.name)
        self.assertEqual(36, self.player.age)
        self.assertEqual(100.00, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_valid(self):
        self.player = TennisPlayer('Phi', 36, 100.00)
        self.assertEqual('Phi', self.player.name)
        self.player.name = 'Phi'

    def test_name_invalid_raise_error_if_name_is_less_than_3_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer('A', 36, 100.00)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer('Al', 36, 100.00)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_valid(self):
        self.player = TennisPlayer('Phi', 22, 100.00)
        self.assertEqual(22, self.player.age)
        self.player.age = 22

    def test_age_invalid_raise_error_if_age_is_less_than_18(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer('Alex', 16, 100.00)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_valid(self):
        self.assertEqual([], self.player.wins)
        self.player.add_new_win('Tournament')
        self.assertEqual(['Tournament'], self.player.wins)

    def test_add_new_win_invalid_already_added(self):
        self.player.add_new_win('Tournament')
        result = self.player.add_new_win('Tournament')
        self.assertEqual("Tournament has been already added to the list of wins!", result)

    def test__lt__(self):
        other = TennisPlayer('Tsv', 36, 101.00)
        self.assertEqual('Tsv is a top seeded player and he/she is better than Alex', self.player.__lt__(other))

        other = TennisPlayer('Phi', 36, 10.00)
        self.assertEqual('Alex is a better player than Phi', self.player.__lt__(other))

    def test__str__(self):
        self.player = TennisPlayer('Oleg', 56, 60.00)
        self.player.wins = ['OOP', 'Adv']

        self.assertEqual(
            'Tennis Player: Oleg\n'
            'Age: 56\n'
            'Points: 60.0\n'
            'Tournaments won: OOP, Adv',
            self.player.__str__()
        )


if __name__ == '__main__':
    main()
