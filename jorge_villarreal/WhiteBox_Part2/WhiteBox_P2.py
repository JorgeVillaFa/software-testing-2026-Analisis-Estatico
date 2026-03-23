

# 22
class VendingMachine:
    """
    A simple vending machine that dispenses drinks.
    It has two states: "Ready" and "Dispensing."
    """

    def __init__(self):
        """
        Defines the vending machine initial state.
        """
        self.state = "Ready"

    def insert_coin(self):
        """
        Function called when a coin is inserted.
        """
        if self.state == "Ready":
            self.state = "Dispensing"
            return "Coin Inserted. Select your drink."

        return "Invalid operation in current state."

    def select_drink(self):
        """
        Function called after selecting a drink.
        """
        if self.state == "Dispensing":
            self.state = "Ready"
            return "Drink Dispensed. Thank you!"

        return "Invalid operation in current state."


# 23
class TrafficLight:
    """
    A traffic light system with three states: "Green," "Yellow," and "Red."
    """

    def __init__(self):
        """
        Defines the traffic light initial state.
        """
        self.state = "Red"

    def change_state(self):
        """
        Function that changes the traffic light state.
        """
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

    def get_current_state(self):
        """
        Provides the current traffic light state.
        """
        return self.state


# 24
class UserAuthentication:
    """
    A user authentication system with states "Logged Out" and "Logged In."
    """

    def __init__(self):
        """
        Defines the user initial state.
        """
        self.state = "Logged Out"

    def login(self):
        """
        Function to login a user.
        """
        if self.state == "Logged Out":
            self.state = "Logged In"
            return "Login successful"

        return "Invalid operation in current state"

    def logout(self):
        """
        Function to logout a user.
        """
        if self.state == "Logged In":
            self.state = "Logged Out"
            return "Logout successful"

        return "Invalid operation in current state"


# 25
class DocumentEditingSystem:
    """
    A document editing system with states "Editing" and "Saved."
    """

    def __init__(self):
        """
        Defines the initial state.
        """
        self.state = "Editing"

    def save_document(self):
        """
        Function to save a document.
        """
        if self.state == "Editing":
            self.state = "Saved"
            return "Document saved successfully"

        return "Invalid operation in current state"

    def edit_document(self):
        """
        Function to edit a document.
        """
        if self.state == "Saved":
            self.state = "Editing"
            return "Editing resumed"

        return "Invalid operation in current state"


# 26
class ElevatorSystem:
    """
    An elevator system with states "Idle," "Moving Up," and "Moving Down."
    """

    def __init__(self):
        """
        Defines the elevator initial state.
        """
        self.state = "Idle"

    def move_up(self):
        """
        Function to move up the elevator.
        """
        if self.state == "Idle":
            self.state = "Moving Up"
            return "Elevator moving up"

        return "Invalid operation in current state"

    def move_down(self):
        """
        Function to move down the elevator.
        """
        if self.state == "Idle":
            self.state = "Moving Down"
            return "Elevator moving down"

        return "Invalid operation in current state"

    def stop(self):
        """
        Function to stop the elevator.
        """
        if self.state in ["Moving Up", "Moving Down"]:
            self.state = "Idle"
            return "Elevator stopped"

        return "Invalid operation in current state"


# 27
class BankAccount:  # pylint: disable=too-few-public-methods
    """
    Bank account class.
    """

    def __init__(self, account_number, balance):
        """
        Set the bank account details.
        """
        self.account_number = account_number
        self.balance = balance

    def view_account(self):
        """
        Function to display the account details.
        """
        print(f"The account {self.account_number} has a balance of {self.balance}")


class BankingSystem:
    """
    Banking system class.
    """

    def __init__(self):
        """
        Mock users.
        """
        self.users = {"user123": "pass123"}  # Simplified user database
        self.logged_in_users = set()

    def authenticate(self, username, password):
        """
        User authentication function.
        """
        if username in self.users and self.users[username] == password:
            if username not in self.logged_in_users:
                self.logged_in_users.add(username)
                print(f"User {username} authenticated successfully.")
                return True

            print("User already logged in.")
        else:
            print("Authentication failed.")

        return False

    def transfer_money(self, sender, receiver, amount, transaction_type):
        """
        Function to perform a money transfer.
        """
        if sender not in self.logged_in_users:
            print("Sender not authenticated.")
            return False

        # Simulate transaction processing logic
        if transaction_type == "regular":
            fee = 0.02 * amount
        elif transaction_type == "express":
            fee = 0.05 * amount
        elif transaction_type == "scheduled":
            fee = 0.01 * amount
        else:
            print("Invalid transaction type.")
            return False

        # Simulate checking for sufficient funds
        if BankAccount(sender, 1000).balance < (amount + fee):
            print("Insufficient funds.")
            return False

        print(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )
        return True
