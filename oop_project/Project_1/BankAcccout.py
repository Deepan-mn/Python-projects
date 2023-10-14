class BankAccount:
    def __init__(self,account_name, initial_amount):
        self.name = account_name
        self.balance = initial_amount
        print(f"Account '{self.name}' created. Balance = ₹{self.balance:.2f} ")

    def get_balance(self):
        print(f"\nAccount '{self.balance}' balance = ${self.balance:.2f} ")

    def deposit(self, amount):
        self.balance += amount
        print("\n Deposit Completed")
        self.get_balance()

