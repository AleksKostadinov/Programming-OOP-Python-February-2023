from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.report = StudentReportCard('Phillip', 2)

    def test_correct_init(self):
        self.assertEqual('Phillip', self.report.student_name)
        self.assertEqual(2, self.report.school_year)
        self.assertEqual({}, self.report.grades_by_subject)

    def test_student_name_raise_if_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.report.student_name = ''
        self.assertEqual('Student Name cannot be an empty string!', str(ve.exception))

    def test_successful_year(self):
        self.report.school_year = 1
        self.assertEqual(1, self.report.school_year)

    def test_student_school_year_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.report.school_year = 13
        self.assertEqual('School Year must be between 1 and 12!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.report.school_year = 0
        self.assertEqual('School Year must be between 1 and 12!', str(ve.exception))

    def test_add_grade_valid(self):
        self.report.add_grade('Math', 5.00)
        self.assertEqual({'Math': [5.00]}, self.report.grades_by_subject)
        self.assertEqual([5.00], self.report.grades_by_subject['Math'])
        self.report.add_grade('German', 6.00)
        self.report.add_grade('Math', 6.00)
        self.assertEqual({'Math': [5.00, 6.00], 'German': [6.00]}, self.report.grades_by_subject)

    def test_average_grade_by_subject_valid(self):
        self.report.add_grade('Math', 5.00)
        self.report.add_grade('Math', 6.00)
        result = self.report.average_grade_by_subject()

        self.assertEqual('Math: 5.50', result)
        self.assertEqual({'Math': [5.0, 6.0]}, self.report.grades_by_subject)
        self.assertEqual([5.0, 6.0], self.report.grades_by_subject['Math'])
        self.report.add_grade('German', 6.00)
        self.assertEqual({'Math': [5.0, 6.0], 'German': [6.00]}, self.report.grades_by_subject)
        self.assertEqual('Math: 5.50\nGerman: 6.00', self.report.average_grade_by_subject())

    def test_average_grade_for_all_subjects_valid(self):
        self.report.add_grade('Math', 5.00)
        self.report.add_grade('German', 5.00)
        self.report.add_grade('Math', 6.00)
        self.report.add_grade('German', 6.00)
        result = self.report.average_grade_for_all_subjects()

        self.assertEqual('Average Grade: 5.50', result)
        self.assertEqual([5.0, 6.0], self.report.grades_by_subject['German'])
        self.assertEqual({'Math': [5.0, 6.0], 'German': [5.0, 6.0]}, self.report.grades_by_subject)

    def test__repr__(self):
        self.report = StudentReportCard('Alex', 12)
        self.report.add_grade("Math", 6.00)
        self.report.add_grade("Math", 6.00)
        self.report.add_grade("German", 6.00)

        result = self.report.__repr__()

        self.assertEqual("Name: Alex\n"
                         "Year: 12\n"
                         "----------\n"
                         "Math: 6.00\n"
                         "German: 6.00\n"
                         "----------\n"
                         "Average Grade: 6.00", result)


if __name__ == "__main__":
    main()
