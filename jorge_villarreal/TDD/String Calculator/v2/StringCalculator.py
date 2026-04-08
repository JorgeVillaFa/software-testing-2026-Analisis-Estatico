"""
    TESTS
"""
import unittest

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_0(self):
        self.assertEqual(stringCalculator(''), 0)

    def test_single_integer(self):
        self.assertEqual(stringCalculator('1'), 1)

    def test_two_integers(self):
        self.assertEqual(stringCalculator('1,2'), 3)

    def test_single_float(self):
        self.assertAlmostEqual(stringCalculator('1.2'), 1.2)

    def test_integer_and_float(self):
        self.assertAlmostEqual(stringCalculator('1,1.2'), 2.2)

    def test_two_floats(self):
        self.assertAlmostEqual(stringCalculator('1.2,2.3'), 3.5)

    def test_many_numbers(self):
        self.assertEqual(stringCalculator('1,2,3,4,5'), 15)

    def test_three_numbers_with_float(self):
        self.assertAlmostEqual(stringCalculator('1,2,1.2'), 4.2)


"""
    METODO
"""

def stringCalculator(numbers):
    if numbers == '':
        return 0
    total = 0
    for n in numbers.split(','):
        total += float(n)
    return total


if __name__ == '__main__':
    unittest.main()
