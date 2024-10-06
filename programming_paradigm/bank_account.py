class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient balance is available."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
