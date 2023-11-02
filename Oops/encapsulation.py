# Encapsulation restricts access to certain parts of an object, hiding the internal details and exposing a controlled interface.

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient funds"

account = BankAccount()
account.deposit(1000)
account.withdraw(500)
