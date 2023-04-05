from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team('Alex')

    def test_correct_init(self):
        self.assertEqual('Alex', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_if_name_contains_not_only_letters_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team = Team('Cherry1')
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_valid(self):
        result = self.team.add_member(Tsvety=36)
        self.assertEqual('Successfully added: Tsvety', result)
        self.assertEqual({'Tsvety': 36}, self.team.members)
        self.assertEqual(36, self.team.members['Tsvety'])

    def test_remove_member_valid(self):
        self.team.add_member(Tsvety=36)
        result = self.team.remove_member('Tsvety')
        self.assertEqual("Member Tsvety removed", result)
        self.assertEqual({}, self.team.members)

    def test_remove_member_not_exist_raise_error(self):
        self.team.add_member(Alex=36)
        result = self.team.remove_member('Tsvety')
        self.assertEqual("Member with name Tsvety does not exist", result)
        self.assertEqual({'Alex': 36}, self.team.members)

    def test__gt__(self):
        self.team.add_member(Tsvety=36)
        self.team.add_member(Alex=36)
        other = Team('Philip')
        other.add_member(Ani=12)
        self.assertEqual(True, self.team.__gt__(other))
        self.assertEqual(False, other.__gt__(self.team))

    def test__len__(self):
        self.team.add_member(Tsvety=36)
        self.team.add_member(Alex=36)
        self.assertEqual(2, self.team.__len__())

    def test__add__(self):
        self.team.add_member(Tsvety=36)
        other = Team('Philip')
        other.add_member(Ani=12)
        self.team.__add__(other)
        self.assertEqual('AlexPhilip', self.team.__add__(other).name)
        self.assertEqual({'Ani': 12, 'Tsvety': 36}, self.team.__add__(other).members)

    def test__str__(self):
        self.team.add_member(Tsvety=36)
        self.team.add_member(Philip=8)

        self.assertEqual(
            'Team name: Alex\n'
            'Member: Tsvety - 36-years old\n'
            'Member: Philip - 8-years old',
            self.team.__str__())


if __name__ == '__main__':
    main()
