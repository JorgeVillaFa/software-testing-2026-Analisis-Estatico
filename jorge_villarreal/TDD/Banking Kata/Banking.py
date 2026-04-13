"""
    TESTS
"""
import io
import unittest
import contextlib
import datetime
from unittest.mock import patch


class TestAccount(unittest.TestCase):
    """
    Kata - Banking

    Create a simple bank application with deposit, withdraw, and printStatement.

    Constraints:
    - Class Account with only 3 public methods: deposit, withdraw, printStatement
    - Use strings and integers for dates and amounts

    Requirements:
    1. Deposit into account
    2. Withdraw from account
    3. Print account statement to console: DATE | AMOUNT | BALANCE
    """

    FIXED_DATE = "13/04/2026"

    @classmethod
    def setUpClass(cls):
        cls.deposit_test_data = [
            # Single deposit
            {"input": [1000], "expected_balance": 1000},
            # Multiple deposits accumulate
            {"input": [1000, 2000], "expected_balance": 3000},
            {"input": [500, 500, 500], "expected_balance": 1500},
        ]

        cls.withdraw_test_data = [
            # Deposit first, then withdraw
            {"deposits": [1000], "input": [500], "expected_balance": 500},
            {"deposits": [2000], "input": [200, 300], "expected_balance": 1500},
        ]

        cls.statement_test_data = [
            # Single deposit
            {
                "operations": [("deposit", 1000)],
                "expected": (
                    "DATE | AMOUNT | BALANCE\n"
                    "13/04/2026 | 1000 | 1000"
                ),
            },
            # Deposit then withdraw
            {
                "operations": [("deposit", 1000), ("withdraw", 500)],
                "expected": (
                    "DATE | AMOUNT | BALANCE\n"
                    "13/04/2026 | -500 | 500\n"
                    "13/04/2026 | 1000 | 1000"
                ),
            },
            # Multiple deposits and withdrawals — statement in reverse order
            {
                "operations": [
                    ("deposit", 1000),
                    ("deposit", 2000),
                    ("withdraw", 500),
                ],
                "expected": (
                    "DATE | AMOUNT | BALANCE\n"
                    "13/04/2026 | -500 | 2500\n"
                    "13/04/2026 | 2000 | 3000\n"
                    "13/04/2026 | 1000 | 1000"
                ),
            },
        ]

    def _make_account_with_ops(self, operations):
        acc = Account()
        for op, amount in operations:
            if op == "deposit":
                acc.deposit(amount)
            elif op == "withdraw":
                acc.withdraw(amount)
        return acc

    def _capture_statement(self, acc):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            acc.printStatement()
        return buffer.getvalue().strip()

    @patch("Banking.datetime")
    def test_deposit(self, mock_dt):
        mock_dt.date.today.return_value.strftime.return_value = self.FIXED_DATE

        for x in self.deposit_test_data:
            with self.subTest(input=x["input"], expected_balance=x["expected_balance"]):
                acc = Account()
                for amount in x["input"]:
                    acc.deposit(amount)
                self.assertEqual(acc._balance, x["expected_balance"])

    @patch("Banking.datetime")
    def test_withdraw(self, mock_dt):
        mock_dt.date.today.return_value.strftime.return_value = self.FIXED_DATE

        for x in self.withdraw_test_data:
            with self.subTest(input=x["input"], expected_balance=x["expected_balance"]):
                acc = Account()
                for amount in x["deposits"]:
                    acc.deposit(amount)
                for amount in x["input"]:
                    acc.withdraw(amount)
                self.assertEqual(acc._balance, x["expected_balance"])

    @patch("Banking.datetime")
    def test_print_statement(self, mock_dt):
        mock_dt.date.today.return_value.strftime.return_value = self.FIXED_DATE

        for x in self.statement_test_data:
            with self.subTest(operations=x["operations"]):
                acc = self._make_account_with_ops(x["operations"])
                output = self._capture_statement(acc)
                self.assertEqual(output, x["expected"])


"""
    METODO
"""
import datetime


class Account:
    """
    Simple bank account supporting deposit, withdraw, and printStatement.
    Only public methods are deposit, withdraw, and printStatement.
    """

    def __init__(self):
        self._balance = 0
        self._transactions = []  # list of (date: str, amount: int, balance: int)

    def deposit(self, amount: int):
        self._balance += amount
        date = datetime.date.today().strftime("%d/%m/%Y")
        self._transactions.append((date, amount, self._balance))

    def withdraw(self, amount: int):
        self._balance -= amount
        date = datetime.date.today().strftime("%d/%m/%Y")
        self._transactions.append((date, -amount, self._balance))

    def printStatement(self):
        print("DATE | AMOUNT | BALANCE")
        for date, amount, balance in reversed(self._transactions):
            print(f"{date} | {amount} | {balance}")


if __name__ == "__main__":
    unittest.main()
