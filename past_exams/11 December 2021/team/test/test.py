from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team('Cherry')

    def test_correct_init(self):
        self.assertEqual('Cherry', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_if_name_contains_not_only_letters_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team = Team('Cherry1')
        self.assertEqual('Team Name can contain only letters!', str(ve.exception))

    def test_add_member_valid(self):
        self.team.add_member(Alex=36)
        result = self.team.add_member(Phillip=8)
        self.assertEqual('Successfully added: Phillip', result)
        self.assertEqual({'Alex': 36, 'Phillip': 8}, self.team.members)

    def test_remove_member_valid(self):
        self.team.add_member(Alex=36)
        result = self.team.remove_member('Alex')
        self.assertEqual('Member Alex removed', result)
        self.assertEqual({}, self.team.members)

    def test_remove_member_not_exist_raise_error(self):
        self.team.add_member(Alex=36)
        result = self.team.remove_member('Phillip')
        self.assertEqual('Member with name Phillip does not exist', result)
        self.assertEqual({'Alex': 36}, self.team.members)

    def test__gt__(self):
        self.team.add_member(Alex=36)
        self.team.add_member(Phillip=8)

        other = Team('Strawberry')
        other.add_member(Tsvety=36)
        result = self.team > other
        self.assertEqual(True, self.team.__gt__(other))
        self.assertEqual(False, other.__gt__(self.team))

    def test__len__(self):
        self.team.add_member(Alex=36, Phillip=8)
        self.assertEqual(2, self.team.__len__())

    def test__add__(self):
        self.team.add_member(Alex=36, Phillip=8)
        other = Team('Strawberry')
        other.add_member(Tsvety=36)
        added_team = self.team.__add__(other)
        self.assertEqual('CherryStrawberry', added_team.name)
        self.assertEqual({'Alex': 36, 'Phillip': 8, 'Tsvety': 36}, added_team.members)

    def test__str__(self):
        self.team.add_member(Alex=36, Phillip=8)
        self.assertEqual(
            "Team name: Cherry\n"
            'Member: Alex - 36-years old\n'
            'Member: Phillip - 8-years old',
            self.team.__str__()
        )


if __name__ == "__main__":
    main()
