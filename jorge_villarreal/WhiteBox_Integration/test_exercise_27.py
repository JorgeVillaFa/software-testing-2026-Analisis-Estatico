# -*- coding: utf-8 -*-

"""
Pruebas unitarias de caja blanca para el ejercicio 27: BankAccount y BankingSystem.
"""
import unittest
from unittest.mock import patch

from white_box.class_exercises import BankAccount, BankingSystem


class TestBankAccount(unittest.TestCase):
    """
    Pruebas para la clase BankAccount.
    """

    def setUp(self):
        self.account = BankAccount(123, 1000)

    def test_inicializa_correctamente(self):
        """
        Verifica que la cuenta se cree con el número y saldo correctos.
        """
        self.assertEqual(self.account.account_number, 123)
        self.assertEqual(self.account.balance, 1000)

    @patch("builtins.print")
    def test_view_account_imprime_bien(self, mock_print):
        """
        Verifica que view_account imprima el número de cuenta y el saldo correctamente.
        """
        self.account.view_account()
        mock_print.assert_called_with(
            f"The account {self.account.account_number} has a balance of {self.account.balance}"
        )


class TestBankingSystem(unittest.TestCase):
    """
    Pruebas para la clase BankingSystem.
    """

    user = "user123"
    password = "pass123"

    def setUp(self):
        self.banking_system = BankingSystem()

    def test_inicializa_correctamente(self):
        """
        Verifica que el sistema bancario arranque con el usuario de prueba y sin sesiones activas.
        """
        self.assertEqual(self.banking_system.users, {self.user: self.password})
        self.assertEqual(self.banking_system.logged_in_users, set())

    @patch("builtins.print")
    def test_autenticar_usuario_exitoso(self, mock_print):
        """
        Verifica que un usuario con credenciales correctas inicie sesión sin problema.
        """
        result = self.banking_system.authenticate(self.user, self.password)
        self.assertTrue(result)
        self.assertIn(self.user, self.banking_system.logged_in_users)
        mock_print.assert_called_with(f"User {self.user} authenticated successfully.")

    @patch("builtins.print")
    def test_autenticar_usuario_ya_autenticado(self, mock_print):
        """
        Verifica que no se pueda autenticar de nuevo un usuario que ya tiene sesión activa.
        """
        self.banking_system.logged_in_users.add(self.user)
        result = self.banking_system.authenticate(self.user, self.password)
        self.assertFalse(result)
        mock_print.assert_called_with("User already logged in.")

    @patch("builtins.print")
    def test_autenticar_usuario_credenciales_incorrectas(self, mock_print):
        """
        Verifica que credenciales incorrectas no permitan iniciar sesión.
        """
        result = self.banking_system.authenticate(self.user, "wrongpass")
        self.assertFalse(result)
        self.assertNotIn(self.user, self.banking_system.logged_in_users)
        mock_print.assert_called_with("Authentication failed.")

    @patch("builtins.print")
    def test_transferencia_sin_sesion_activa(self, mock_print):
        """
        Verifica que no se pueda hacer una transferencia si el usuario no ha iniciado sesión.
        """
        result = self.banking_system.transfer_money(
            self.user, "user456", 200, "regular"
        )
        self.assertFalse(result)
        mock_print.assert_called_with("Sender not authenticated.")

    @patch("builtins.print")
    def test_transferencia_regular_exitosa(self, mock_print):
        """
        Verifica que una transferencia regular se procese bien cuando el usuario tiene sesión y fondos.
        """
        receiver = "user456"
        amount = 200
        transaction_type = "regular"
        self.banking_system.logged_in_users.add(self.user)
        result = self.banking_system.transfer_money(
            self.user, receiver, amount, transaction_type
        )
        self.assertTrue(result)
        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully."
        )

    @patch("builtins.print")
    def test_transferencia_express_exitosa(self, mock_print):
        """
        Verifica que una transferencia express se procese bien cuando el usuario tiene sesión y fondos.
        """
        receiver = "user456"
        amount = 200
        transaction_type = "express"
        self.banking_system.logged_in_users.add(self.user)
        result = self.banking_system.transfer_money(
            self.user, receiver, amount, transaction_type
        )
        self.assertTrue(result)
        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully."
        )

    @patch("builtins.print")
    def test_transferencia_programada_exitosa(self, mock_print):
        """
        Verifica que una transferencia programada se procese bien cuando el usuario tiene sesión y fondos.
        """
        receiver = "user456"
        amount = 200
        transaction_type = "scheduled"
        self.banking_system.logged_in_users.add(self.user)
        result = self.banking_system.transfer_money(
            self.user, receiver, amount, transaction_type
        )
        self.assertTrue(result)
        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully."
        )

    @patch("builtins.print")
    def test_transferencia_tipo_invalido(self, mock_print):
        """
        Verifica que un tipo de transferencia desconocido sea rechazado.
        """
        self.banking_system.logged_in_users.add(self.user)
        result = self.banking_system.transfer_money(self.user, "user456", 200, "crypto")
        self.assertFalse(result)
        mock_print.assert_called_with("Invalid transaction type.")

    @patch("builtins.print")
    def test_transferencia_fondos_insuficientes(self, mock_print):
        """
        Verifica que una transferencia mayor al saldo disponible sea rechazada.
        """
        self.banking_system.logged_in_users.add(self.user)
        result = self.banking_system.transfer_money(
            self.user, "user456", 1000, "regular"
        )
        self.assertFalse(result)
        mock_print.assert_called_with("Insufficient funds.")


if __name__ == "__main__":
    unittest.main()
