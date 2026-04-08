"""
    PRUEBAS
"""
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_returns_string(self):
        result = FizzBuzz(1)
        self.assertIsInstance(result, str)

    def test_returns_string_with_multiple_inputs(self):
        for number in [1, 3, 5, 15, 100]:
            with self.subTest(number=number):
                result = FizzBuzz(number)
                self.assertIsInstance(result, str)

    def test_raises_error_when_input_is_not_a_number(self):
        for invalid in ["hello", None, [1], {"a": 1}]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    FizzBuzz(invalid)

    def test_returns_fizz_when_multiple_of_3(self):
        for number in [3, 6, 9, 12]:
            with self.subTest(number=number):
                self.assertEqual(FizzBuzz(number), 'Fizz')

    def test_does_not_return_fizz_when_not_multiple_of_3(self):
        for number in [1, 2, 4, 5]:
            with self.subTest(number=number):
                self.assertNotEqual(FizzBuzz(number), 'Fizz')


""" 
    METODO v2
"""
def FizzBuzz(number):
    if(number % 3):
        return 'Fizz'
    return 'String'