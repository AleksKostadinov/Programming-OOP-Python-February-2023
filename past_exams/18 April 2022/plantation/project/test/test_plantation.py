from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_correct_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_negative(self):
        with self.assertRaises(ValueError) as ve:
            result = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_valid(self):
        result = self.plantation.hire_worker('Worker1')
        self.assertEqual('Worker1 successfully hired.', result)
        # self.assertTrue("Joro" in self.plantation.workers)
        #
        # result = self.plantation.hire_worker("Not Joro")
        #
        # self.assertEqual("Not Joro successfully hired.", result)
        # self.assertTrue("Not Joro" in self.plantation.workers)

    def test_hire_worker_already_hired(self):
        self.plantation.hire_worker('Worker1')
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Worker1')
        self.assertEqual('Worker already hired!', str(ve.exception))

    def test_len(self):
        self.assertEqual(0, self.plantation.__len__())
        self.plantation.plants = {'Sashe': ['roses'], 'Tsvety': ['camomiles']}
        self.assertEqual(2, self.plantation.__len__())

    def test_planting_valid_first_time(self):
        self.plantation.hire_worker('Sashe')
        result = self.plantation.planting('Sashe', 'roses')
        self.assertEqual('Sashe planted it\'s first roses.', result)
        self.assertEqual({'Sashe': ['roses']}, self.plantation.plants)

    def test_planting_valid_not_first_time(self):
        self.plantation.hire_worker('Sashe')
        self.plantation.plants = {'Sashe': ['roses']}
        result = self.plantation.planting('Sashe', 'roses')
        self.assertEqual('Sashe planted roses.', result)
        self.assertEqual({'Sashe': ['roses', 'roses']}, self.plantation.plants)

    def test_planting_raise_plantation_is_full(self):
        self.plantation.size = 2
        self.plantation.hire_worker('Tsvety')
        self.plantation.planting('Tsvety', 'camomiles')
        self.plantation.planting('Tsvety', 'hyacinth')
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Tsvety', 'snowdrop')
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_worker_is_not_hired(self):
        self.plantation.hire_worker('Sashe')
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Tsvety', 'snowdrop')
        self.assertEqual("Worker with name Tsvety is not hired!", str(ve.exception))

    def test_str(self):
        self.plantation.size = 5
        self.plantation.hire_worker('Sashe')
        self.plantation.hire_worker('Tsvety')
        self.plantation.planting('Sashe', 'roses')
        self.plantation.planting('Tsvety', 'hyacinth')
        self.plantation.planting('Tsvety', 'snowdrop')
        self.assertEqual('Plantation size: 5\n'
                         'Sashe, Tsvety\n'
                         'Sashe planted: roses\n'
                         'Tsvety planted: hyacinth, snowdrop',
                         str(self.plantation.__str__())
                         )

    def test_repr(self):
        self.plantation.size = 5
        self.plantation.hire_worker('Sashe')
        self.plantation.hire_worker('Tsvety')
        self.assertEqual('Size: 5\n'
                         'Workers: Sashe, Tsvety',
                         str(self.plantation.__repr__())
                         )


if __name__ == "__main__":
    main()
