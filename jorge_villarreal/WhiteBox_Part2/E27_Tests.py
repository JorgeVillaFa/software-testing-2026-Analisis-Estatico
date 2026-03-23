"""
White-box unit testing examples.
"""

import unittest

from WhiteBox_P2 import (
    BankAccount,
    BankingSystem,
    DocumentEditingSystem,
    ElevatorSystem,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
)


class TestBankAccount(unittest.TestCase):
    """
    BankAccount unit tests.
    """

    def test_view_account_displays_info(self):
        """
        Checks that view_account runs without errors with valid data.
        """
        account = BankAccount("ACC001", 500)
        self.assertEqual(account.account_number, "ACC001")
        self.assertEqual(account.balance, 500)


class TestBankingSystem(unittest.TestCase):
    """
    BankingSystem unit tests.
    """

    def setUp(self):
        self.banking_system = BankingSystem()
        self.assertEqual(self.banking_system.users, {"user123": "pass123"})
        self.assertEqual(len(self.banking_system.logged_in_users), 0)

    # --- authenticate ---

    def test_authenticate_success(self):
        """
        Checks that a valid user with correct password authenticates successfully.
        """
        result = self.banking_system.authenticate("user123", "pass123")

        self.assertTrue(result)
        self.assertIn("user123", self.banking_system.logged_in_users)

    def test_authenticate_wrong_password(self):
        """
        Checks that authentication fails when the password is incorrect.
        """
        result = self.banking_system.authenticate("user123", "wrongpass")

        self.assertFalse(result)
        self.assertNotIn("user123", self.banking_system.logged_in_users)

    def test_authenticate_unknown_user(self):
        """
        Checks that authentication fails for a non-existent user.
        """
        result = self.banking_system.authenticate("unknown", "pass123")

        self.assertFalse(result)

    def test_authenticate_already_logged_in(self):
        """
        Checks that a user who is already logged in cannot authenticate again.
        """
        self.banking_system.authenticate("user123", "pass123")
        result = self.banking_system.authenticate("user123", "pass123")

        self.assertFalse(result)

    # --- transfer_money ---

    def test_transfer_money_sender_not_authenticated(self):
        """
        Checks that the transfer fails when the sender is not logged in.
        """
        result = self.banking_system.transfer_money(
            "user123", "receiver", 100, "regular"
        )

        self.assertFalse(result)

    def test_transfer_money_invalid_transaction_type(self):
        """
        Checks that the transfer fails when an unknown transaction type is provided.
        """
        self.banking_system.authenticate("user123", "pass123")
        result = self.banking_system.transfer_money(
            "user123", "receiver", 100, "crypto"
        )

        self.assertFalse(result)

    def test_transfer_money_regular_success(self):
        """
        Checks a successful regular transfer with sufficient funds.
        """
        self.banking_system.authenticate("user123", "pass123")
        result = self.banking_system.transfer_money(
            "user123", "receiver", 100, "regular"
        )

        self.assertTrue(result)

    def test_transfer_money_express_success(self):
        """
        Checks a successful express transfer with sufficient funds.
        """
        self.banking_system.authenticate("user123", "pass123")
        result = self.banking_system.transfer_money(
            "user123", "receiver", 100, "express"
        )

        self.assertTrue(result)

    def test_transfer_money_scheduled_success(self):
        """
        Checks a successful scheduled transfer with sufficient funds.
        """
        self.banking_system.authenticate("user123", "pass123")
        result = self.banking_system.transfer_money(
            "user123", "receiver", 100, "scheduled"
        )

        self.assertTrue(result)

    def test_transfer_money_insufficient_funds(self):
        """
        Checks that the transfer fails when the amount plus fee exceeds the balance.
        """
        self.banking_system.authenticate("user123", "pass123")
        result = self.banking_system.transfer_money(
            "user123", "receiver", 1000, "regular"
        )

        self.assertFalse(result)


class TestVendingMachine(unittest.TestCase):
    """
    VendingMachine unit tests.
    """

    def setUp(self):
        self.machine = VendingMachine()

    def test_initial_state_is_ready(self):
        """
        Checks that the vending machine starts in Ready state.
        """
        self.assertEqual(self.machine.state, "Ready")

    def test_insert_coin_from_ready(self):
        """
        Checks that inserting a coin from Ready moves to Dispensing.
        """
        result = self.machine.insert_coin()

        self.assertEqual(result, "Coin Inserted. Select your drink.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_insert_coin_from_dispensing(self):
        """
        Checks that inserting a coin while Dispensing returns invalid operation.
        """
        self.machine.insert_coin()
        result = self.machine.insert_coin()

        self.assertEqual(result, "Invalid operation in current state.")

    def test_select_drink_from_dispensing(self):
        """
        Checks that selecting a drink from Dispensing dispenses and returns to Ready.
        """
        self.machine.insert_coin()
        result = self.machine.select_drink()

        self.assertEqual(result, "Drink Dispensed. Thank you!")
        self.assertEqual(self.machine.state, "Ready")

    def test_select_drink_from_ready(self):
        """
        Checks that selecting a drink from Ready returns invalid operation.
        """
        result = self.machine.select_drink()

        self.assertEqual(result, "Invalid operation in current state.")


class TestTrafficLight(unittest.TestCase):
    """
    TrafficLight unit tests.
    """

    def setUp(self):
        self.light = TrafficLight()

    def test_initial_state_is_red(self):
        """
        Checks that the traffic light starts in Red state.
        """
        self.assertEqual(self.light.get_current_state(), "Red")

    def test_change_state_red_to_green(self):
        """
        Checks that changing from Red results in Green.
        """
        self.light.change_state()

        self.assertEqual(self.light.get_current_state(), "Green")

    def test_change_state_green_to_yellow(self):
        """
        Checks that changing from Green results in Yellow.
        """
        self.light.change_state()
        self.light.change_state()

        self.assertEqual(self.light.get_current_state(), "Yellow")

    def test_change_state_yellow_to_red(self):
        """
        Checks that changing from Yellow results in Red.
        """
        self.light.change_state()
        self.light.change_state()
        self.light.change_state()

        self.assertEqual(self.light.get_current_state(), "Red")


class TestUserAuthentication(unittest.TestCase):
    """
    UserAuthentication unit tests.
    """

    def setUp(self):
        self.auth = UserAuthentication()

    def test_initial_state_is_logged_out(self):
        """
        Checks that the user starts in Logged Out state.
        """
        self.assertEqual(self.auth.state, "Logged Out")

    def test_login_from_logged_out(self):
        """
        Checks that login succeeds when user is logged out.
        """
        result = self.auth.login()

        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

    def test_login_from_logged_in(self):
        """
        Checks that login returns invalid operation when already logged in.
        """
        self.auth.login()
        result = self.auth.login()

        self.assertEqual(result, "Invalid operation in current state")

    def test_logout_from_logged_in(self):
        """
        Checks that logout succeeds when user is logged in.
        """
        self.auth.login()
        result = self.auth.logout()

        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_logout_from_logged_out(self):
        """
        Checks that logout returns invalid operation when already logged out.
        """
        result = self.auth.logout()

        self.assertEqual(result, "Invalid operation in current state")


class TestDocumentEditingSystem(unittest.TestCase):
    """
    DocumentEditingSystem unit tests.
    """

    def setUp(self):
        self.doc = DocumentEditingSystem()

    def test_initial_state_is_editing(self):
        """
        Checks that the document starts in Editing state.
        """
        self.assertEqual(self.doc.state, "Editing")

    def test_save_document_from_editing(self):
        """
        Checks that saving from Editing moves to Saved.
        """
        result = self.doc.save_document()

        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(self.doc.state, "Saved")

    def test_save_document_from_saved(self):
        """
        Checks that saving from Saved returns invalid operation.
        """
        self.doc.save_document()
        result = self.doc.save_document()

        self.assertEqual(result, "Invalid operation in current state")

    def test_edit_document_from_saved(self):
        """
        Checks that editing from Saved moves back to Editing.
        """
        self.doc.save_document()
        result = self.doc.edit_document()

        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.doc.state, "Editing")

    def test_edit_document_from_editing(self):
        """
        Checks that editing from Editing returns invalid operation.
        """
        result = self.doc.edit_document()

        self.assertEqual(result, "Invalid operation in current state")


class TestElevatorSystem(unittest.TestCase):
    """
    ElevatorSystem unit tests.
    """

    def setUp(self):
        self.elevator = ElevatorSystem()

    def test_initial_state_is_idle(self):
        """
        Checks that the elevator starts in Idle state.
        """
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_from_idle(self):
        """
        Checks that moving up from Idle transitions to Moving Up.
        """
        result = self.elevator.move_up()

        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_up_from_moving_up(self):
        """
        Checks that moving up while already Moving Up returns invalid operation.
        """
        self.elevator.move_up()
        result = self.elevator.move_up()

        self.assertEqual(result, "Invalid operation in current state")

    def test_move_down_from_idle(self):
        """
        Checks that moving down from Idle transitions to Moving Down.
        """
        result = self.elevator.move_down()

        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_down_from_moving_down(self):
        """
        Checks that moving down while already Moving Down returns invalid operation.
        """
        self.elevator.move_down()
        result = self.elevator.move_down()

        self.assertEqual(result, "Invalid operation in current state")

    def test_stop_from_moving_up(self):
        """
        Checks that stopping while Moving Up returns to Idle.
        """
        self.elevator.move_up()
        result = self.elevator.stop()

        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_from_moving_down(self):
        """
        Checks that stopping while Moving Down returns to Idle.
        """
        self.elevator.move_down()
        result = self.elevator.stop()

        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_from_idle(self):
        """
        Checks that stopping while Idle returns invalid operation.
        """
        result = self.elevator.stop()

        self.assertEqual(result, "Invalid operation in current state")
