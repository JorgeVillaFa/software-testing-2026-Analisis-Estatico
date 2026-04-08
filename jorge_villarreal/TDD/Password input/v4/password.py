"""
    TESTS
"""
import unittest

class TestValidatePassword(unittest.TestCase):

    def test_valid_password_all_conditions(self):
        self.assertTrue(validate_password("Abcd1234"))

    def test_valid_password_multiple_uppercase_and_numbers(self):
        self.assertTrue(validate_password("SECURE1234"))

    def test_invalid_password_short(self):
        with self.assertRaises(ValueError) as context:
            validate_password("Abc12")
        self.assertIn("The password must be at least 8 characters", str(context.exception))

    def test_invalid_password_not_enough_numbers(self):
        with self.assertRaises(ValueError) as context:
            validate_password("Abcdefgh")
        self.assertIn("The password must contain at least 2 numbers", str(context.exception))

    def test_invalid_password_no_uppercase(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abcd1234")
        self.assertIn("The password must contain at least one capital letter", str(context.exception))

    def test_invalid_password_no_uppercase_and_numbers(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefgh")
        message = str(context.exception)
        self.assertIn("The password must contain at least 2 numbers", message)
        self.assertIn("The password must contain at least one capital letter", message)

    def test_invalid_password_all_conditions_fail(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abc")
        message = str(context.exception)
        self.assertIn("The password must be at least 8 characters", message)
        self.assertIn("The password must contain at least 2 numbers", message)
        self.assertIn("The password must contain at least one capital letter", message)

    def test_invalid_password_one_number(self):
        with self.assertRaises(ValueError) as context:
            validate_password("Abcdefg1")
        self.assertIn("The password must contain at least 2 numbers", str(context.exception))




"""
    METODO
"""

def validate_password(password: str) -> bool:
    """
    Validates that the password:
    - Has at least 8 characters
    - Contains at least 2 numbers
    - Contains at least 1 uppercase letter

    Raises ValueError with all corresponding error messages.
    """
    errors = []

    if len(password) < 8:
        errors.append("The password must be at least 8 characters")

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        errors.append("The password must contain at least 2 numbers")

    has_uppercase = any(char.isupper() for char in password)
    if not has_uppercase:
        errors.append("The password must contain at least one capital letter")

    if errors:
        raise ValueError(" | ".join(errors))

    return True

if __name__ == '__main__':
    unittest.main()