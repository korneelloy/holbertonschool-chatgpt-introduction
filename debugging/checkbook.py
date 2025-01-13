#!/usr/bin/env python3

class Checkbook:
    """
    A simple checkbook class to manage a balance, allowing deposits, withdrawals, 
    and checking the current balance.
    """

    def __init__(self):
        """
        Initialize a Checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Args:
            amount (float): The amount to deposit. Must be non-negative.

        Returns:
            None
        """
        if amount < 0:
            print("Cannot deposit a negative amount.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Args:
            amount (float): The amount to withdraw. Must be non-negative.

        Returns:
            None
        """
        if amount < 0:
            print("Cannot withdraw a negative amount.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook class via a command-line interface.

    Users can deposit money, withdraw money, check the balance, or exit the program.

    Returns:
        None
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Thank you for using the checkbook. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $").strip())
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $").strip())
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
