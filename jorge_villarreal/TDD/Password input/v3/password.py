"""
    TESTS
"""
import unittest

class TestValidatePassword(unittest.TestCase):

    def test_valid_password_exact_conditions(self):
        self.assertTrue(validate_password("abcd1234"))

    def test_valid_password_more_numbers(self):
        self.assertTrue(validate_password("secure12345"))

    def test_invalid_password_short(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abc123")
        self.assertIn("The password must be at least 8 characters", str(context.exception))

    def test_invalid_password_not_enough_numbers(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefgh")
        self.assertIn("The password must contain at least 2 numbers", str(context.exception))

    def test_invalid_password_both_conditions(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abc")
        message = str(context.exception)
        self.assertIn("The password must be at least 8 characters", message)
        self.assertIn("The password must contain at least 2 numbers", message)

    def test_invalid_password_one_number(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abcdefg1")
        self.assertIn("The password must contain at least 2 numbers", str(context.exception))



"""
    METODO
"""
def validate_password(password: str) -> bool:
    """
    Validates that the password:
    - Has at least 8 characters
    - Contains at least 2 numbers

    If one or both conditions fail, raises a ValueError
    with the corresponding message(s).
    """
    errors = []

    if len(password) < 8:
        errors.append("The password must be at least 8 characters")

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        errors.append("The password must contain at least 2 numbers")

    if errors:
        raise ValueError(" | ".join(errors))

    return True

if __name__ == '__main__':
    unittest.main()