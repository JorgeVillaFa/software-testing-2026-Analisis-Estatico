"""
    TESTS
"""
import unittest

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_0(self):
        self.assertEqual(stringCalculator(''), 0)

    def test_single_integer(self):
        self.assertEqual(stringCalculator('1'), 1)

    def test_two_integers_comma(self):
        self.assertEqual(stringCalculator('1,2'), 3)

    def test_two_integers_newline(self):
        self.assertEqual(stringCalculator('1\n2'), 3)

    def test_mixed_separators_valid(self):
        self.assertEqual(stringCalculator('1,2\n3'), 6)

    def test_many_numbers_newline(self):
        self.assertEqual(stringCalculator('1\n2\n3\n4'), 10)

    def test_comma_then_newline_treated_as_zero(self):
        self.assertEqual(stringCalculator('1,\n3'), 4)

    def test_newline_then_comma_treated_as_zero(self):
        self.assertEqual(stringCalculator('1\n,3'), 4)

    def test_trailing_comma_raises(self):
        with self.assertRaises(ValueError):
            stringCalculator('1,2,3,')

    def test_trailing_newline_raises(self):
        with self.assertRaises(ValueError):
            stringCalculator('1,2\n')


"""
    METODO
"""

def stringCalculator(numbers):
    if numbers == '':
        return 0

    if numbers.endswith(',') or numbers.endswith('\n'):
        raise ValueError('Invalid input: string cannot end with a separator')

    numbers = numbers.replace(',\n', ',0,').replace('\n,', ',0,')

    total = 0
    for n in numbers.replace('\n', ',').split(','):
        if n.strip() == '':
            continue
        total += float(n)

    return total

if __name__ == '__main__':
    unittest.main()
