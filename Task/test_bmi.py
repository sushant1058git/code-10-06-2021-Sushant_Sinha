import unittest
import bmi


class Test_Bmi(unittest.TestCase):

    def test_person_data(self):
        result = bmi.person_data(162, 67)
        self.assertEqual(result, 25.53)

    def test_person3_data(self):
        result = bmi.person_data(162, 67)
        self.assertNotEqual(result, 25.52)


class Test_Bmi2(unittest.TestCase):

    def test_person1_data(self):
        result = bmi.person_data(192, 67)
        self.assertEqual(result, 18.17)

    def test_person2_data(self):
        result = bmi.person_data(192, 67)
        self.assertEqual(result, 18.17000)


if __name__ == "__main__":
    unittest.main()
