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

    def test_returns_buzz_when_multiple_of_5(self):
        for number in [5, 10, 20, 25]:
            with self.subTest(number=number):
                self.assertEqual(FizzBuzz(number), 'Buzz')

    def test_does_not_return_buzz_when_not_multiple_of_5(self):
        for number in [1, 2, 3, 4]:
            with self.subTest(number=number):
                self.assertNotEqual(FizzBuzz(number), 'Buzz')

    def test_returns_fizzbuzz_when_multiple_of_3_and_5(self):
        for number in [15, 30, 45, 60]:
            with self.subTest(number=number):
                self.assertEqual(FizzBuzz(number), 'FizzBuzz')

    def test_does_not_return_fizzbuzz_when_not_multiple_of_both(self):
        for number in [3, 5, 6, 10]:
            with self.subTest(number=number):
                self.assertNotEqual(FizzBuzz(number), 'FizzBuzz')


""" 
    METODO v4
"""
def FizzBuzz(number):
    if(number % 3):
        if(number % 5):
            return 'FizzBuzz'
        return 'Fizz'
    elif(number % 5):
        if(number % 3):
            return 'FizzBuzz'
        return 'Buzz'
    return 'String'