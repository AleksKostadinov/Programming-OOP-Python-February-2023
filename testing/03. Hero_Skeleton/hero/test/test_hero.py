from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Sashe', 1, 99, 50)
        self.heroine = Hero('Tsvety', 2, 100, 69)

    def test_correct_init(self):
        self.assertEqual('Sashe', self.hero.username)
        self.assertEqual('Tsvety', self.heroine.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(99, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_cannot_fight_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_cannot_health_be_0_or_less(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.heroine)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest',
                         str(ve.exception))

    def test_battle_cannot_enemys_health_be_0_or_less(self):
        self.heroine.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.heroine)

        self.assertEqual('You cannot fight Tsvety. He needs to rest',
                         str(ve.exception))

    def test_battle_equals_health_should_get_draw(self):
        self.hero.health = 100
        self.heroine.health = 50
        self.heroine.damage = 50

        result = self.hero.battle(self.heroine)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.heroine.health)
        self.assertEqual('Draw', result)


    def test_battle_hero_won(self):
        self.hero.damage = 100
        self.heroine.damage = 45
        result = self.hero.battle(self.heroine)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(14, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual('You win', result)


    def test_battle_hero_lost(self):
        result = self.hero.battle(self.heroine)
        self.assertEqual(3, self.heroine.level)
        self.assertEqual(55, self.heroine.health)
        self.assertEqual(74, self.heroine.damage)
        self.assertEqual('You lose', result)

    def test_str_(self):
        self.assertEqual(
            "Hero Sashe: 1 lvl\n" +
            f"Health: 99\n" +
            f"Damage: 50\n",
            str(self.hero)
        )


if __name__ == "__main__":
    main()
