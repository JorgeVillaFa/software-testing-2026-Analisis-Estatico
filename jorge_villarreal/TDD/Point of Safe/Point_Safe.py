"""
    TESTS
"""
import unittest


class TestPointOfSale(unittest.TestCase):
    """
    Kata - Point of Sale

    Create a simple app for scanning bar codes to sell products.

    Requirements:
    1. Barcode '12345' should display '$7.25'
    2. Barcode '23456' should display '$12.50'
    3. Barcode '99999' should display 'Error: barcode not found'
    4. Empty barcode should display 'Error: empty barcode'
    5. Total command: scanning multiple items displays the sum of scanned product prices
    """

    @classmethod
    def setUpClass(cls):
        cls.scan_test_data = [
            # Requirement 1
            {"input": "12345", "output": "$7.25"},
            # Requirement 2
            {"input": "23456", "output": "$12.50"},
            # Requirement 3
            {"input": "99999", "output": "Error: barcode not found"},
            # Requirement 4
            {"input": "", "output": "Error: empty barcode"},
        ]

        cls.total_test_data = [
            # Single item
            {"input": ["12345"], "output": "$7.25"},
            # Multiple items
            {"input": ["12345", "23456"], "output": "$19.75"},
            # Errors are not added to total
            {"input": ["12345", "99999", ""], "output": "$7.25"},
            # No items scanned
            {"input": [], "output": "$0.00"},
        ]

    def test_scan(self):
        for x in self.scan_test_data:
            with self.subTest(input=x["input"], output=x["output"]):
                pos = PointOfSale()
                self.assertEqual(pos.scan(x["input"]), x["output"])

    def test_total(self):
        for x in self.total_test_data:
            with self.subTest(input=x["input"], output=x["output"]):
                pos = PointOfSale()
                for barcode in x["input"]:
                    pos.scan(barcode)
                self.assertEqual(pos.total(), x["output"])


"""
    METODO
"""


class PointOfSale:
    """
    Point of Sale system that scans barcodes and tracks a running total.
    """

    PRODUCTS = {
        "12345": 7.25,
        "23456": 12.50,
    }

    def __init__(self):
        self._total = 0.0

    def scan(self, barcode: str) -> str:
        """
        Scans a barcode and returns its price or an error message.
        Valid prices are also accumulated in the running total.
        """
        if barcode == "":
            return "Error: empty barcode"

        if barcode not in self.PRODUCTS:
            return "Error: barcode not found"

        price = self.PRODUCTS[barcode]
        self._total += price
        return f"${price:.2f}"

    def total(self) -> str:
        """
        Returns the sum of all successfully scanned product prices.
        """
        return f"${self._total:.2f}"


if __name__ == "__main__":
    unittest.main()
