class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    # Intentionally Buggy (Task Requirement)
    def withdraw(self, amount):
        # BUG: Does not check for negative amounts!
        if amount > self.balance:
            raise ValueError("Insufficient funds!")

        self.balance -= amount

    def getBalance(self):
        return self.balance