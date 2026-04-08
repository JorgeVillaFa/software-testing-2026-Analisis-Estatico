"""
    TESTS
"""
import unittest

class TestValidatePassword(unittest.TestCase):

    def test_valid_password_all_conditions(self):
        self.assertTrue(validate_password("Abcd12!@"))

    def test_valid_password_multiple_specials(self):
        self.assertTrue(validate_password("Secure123!#"))

    def test_invalid_password_no_special_char(self):
        with self.assertRaises(ValueError) as context:
            validate_password("Abcd1234")
        self.assertIn("The password must contain at least one special character", str(context.exception))

    def test_invalid_password_no_uppercase(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abcd12!@")
   
    def test_invalid_password_not_enough_numbers(self):
        with self.assertRaises(ValueError) as context:
            validate_password("Abcdef!@")
        self.assertIn("The password must contain at least 2 numbers", str(context.exception))

    def test_invalid_password_short(self):
        with self.assertRaises(ValueError) as context:
            validate_password("Ab1!")
        self.assertIn("The password must be at least 8 characters", str(context.exception))

    def test_invalid_password_multiple_failures(self):
        with self.assertRaises(ValueError) as context:
            validate_password("abc")
        message = str(context.exception)
        self.assertIn("The password must be at least 8 characters", message)
        self.assertIn("The password must contain at least 2 numbers", message)
        self.assertIn("The password must contain at least one capital letter", message)
        self.assertIn("The password must contain at least one special character", message)

    def test_invalid_password_no_special_and_numbers(self):
        with self.assertRaises(ValueError) as context:
            validate_password("Abcdefgh")
        message = str(context.exception)
        self.assertIn("The password must contain at least 2 numbers", message)
        self.assertIn("The password must contain at least one special character", message)



"""
    METODO
"""
import string

def validate_password(password: str) -> bool:
    """
    Validates that the password:
    - Has at least 8 characters
    - Contains at least 2 numbers
    - Contains at least 1 uppercase letter
    - Contains at least 1 special character

    Raises ValueError with all corresponding error messages.
    """
    errors = []

    if len(password) < 8:
        errors.append("The password must be at least 8 characters")

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        errors.append("The password must contain at least 2 numbers")

    if not any(char.isupper() for char in password):
        errors.append("The password must contain at least one capital letter")

    special_characters = string.punctuation
    if not any(char in special_characters for char in password):
        errors.append("The password must contain at least one special character")

    if errors:
        raise ValueError(" | ".join(errors))

    return True

if __name__ == '__main__':
    unittest.main()