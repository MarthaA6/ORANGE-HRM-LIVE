class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
        return self.balance


# Example usage
if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    account.check_balance()  # Output: Current balance is $100.

    account.deposit(50)  # Output: Deposited $50. New balance is $150.
    account.withdraw(30)  # Output: Withdrew $30. New balance is $120.
    account.withdraw(200)  # Output: Insufficient funds.
    account.check_balance()  # Output: Current balance is $120.
