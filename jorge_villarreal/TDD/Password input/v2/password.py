"""
    TESTS
"""
import unittest

class TestValidatePassword(unittest.TestCase):

    def test_valid_password_exact_8_with_2_numbers(self):
        self.assertTrue(validate_password("abcd1234"))

    def test_valid_password_more_than_8_with_many_numbers(self):
        self.assertTrue(validate_password("secure12345"))

    def test_invalid_password_less_than_8_chars(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abc123")
        self.assertEqual(str(context.exception), "The password must be at least 8 characters")

    def test_invalid_empty_password(self):
        with self.assertRaises(ValueError) as context:
            validate_password("")
        self.assertEqual(str(context.exception), "The password must be at least 8 characters")

    def test_invalid_password_no_numbers(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefgh")
        self.assertEqual(str(context.exception), "The password must contain at least 2 numbers")

    def test_invalid_password_only_one_number(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefg1")
        self.assertEqual(str(context.exception), "The password must contain at least 2 numbers")

    def test_invalid_password_short_and_no_numbers(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abc")
        self.assertEqual(str(context.exception), "The password must be at least 8 characters")



"""
    METODO
"""
def validate_password(password: str) -> bool:
    """
    Validates that the password:
    - Has at least 8 characters
    - Contains at least 2 numbers

    """
    if len(password) < 8:
        raise ValueError("The password must be at least 8 characters")

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        raise ValueError("The password must contain at least 2 numbers")

    return True

if __name__ == '__main__':
    unittest.main()
