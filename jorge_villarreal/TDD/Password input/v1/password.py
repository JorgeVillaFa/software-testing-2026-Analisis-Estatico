"""
    TESTS
"""
import unittest

class TestValidatePassword(unittest.TestCase):

    def test_valid_password_exact_8_chars(self):
        self.assertTrue(validate_password("12345678"))

    def test_valid_password_more_than_8_chars(self):
        self.assertTrue(validate_password("securepassword"))

    def test_invalid_password_less_than_8_chars(self):
        with self.assertRaises(ValueError) as context:
            validate_password("1234567")
        self.assertEqual(str(context.exception), "The password must be at least 8 characters")

    def test_invalid_empty_password(self):
        with self.assertRaises(ValueError) as context:
            validate_password("")
        self.assertEqual(str(context.exception), "The password must be at least 8 characters")

    def test_invalid_password_7_chars(self):
        with self.assertRaises(ValueError):
            validate_password("abcdefg")


"""
    METODO
"""
def validate_password(password: str) -> bool:
    """
    Validates that the password has at least 8 characters.

    """
    if len(password) < 8:
        raise ValueError("The password must be at least 8 characters")
    return True

if __name__ == '__main__':
    unittest.main()
