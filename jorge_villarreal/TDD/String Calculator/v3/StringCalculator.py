"""
    TESTS
"""
import unittest

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(stringCalculator(''), 0)

    def test_single_number(self):
        self.assertEqual(stringCalculator('5'), 5)

    def test_multiple_numbers_comma(self):
        self.assertEqual(stringCalculator('1,2,3'), 6)

    def test_multiple_numbers_newline(self):
        self.assertEqual(stringCalculator('1\n2\n3'), 6)

    def test_mixed_delimiters(self):
        self.assertEqual(stringCalculator('1\n2,3'), 6)

    def test_comma_newline_treated_as_zero(self):
        self.assertEqual(stringCalculator('1,\n2'), 3)

    def test_newline_comma_treated_as_zero(self):
        self.assertEqual(stringCalculator('1\n,2'), 3)

    def test_multiple_invalid_sequences(self):
        self.assertEqual(stringCalculator('1,\n,2\n,3'), 6)

    def test_empty_elements_ignored(self):
        self.assertEqual(stringCalculator('1,,2'), 3)



"""
    METODO
"""

def stringCalculator(numbers):
    if numbers == '':
        return 0
    numbers = numbers.replace(',\n', ',0,').replace('\n,', ',0,')
    total = 0
    for n in numbers.replace('\n', ',').split(','):
        if n.strip() == '':
            continue
        total += float(n)
    return total


if __name__ == '__main__':
    unittest.main()
