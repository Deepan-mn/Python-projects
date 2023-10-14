class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,account_name, initial_amount):
        self.name = account_name
        self.balance = initial_amount
        print(f"Account '{self.name}' created. Balance = ₹{self.balance:.2f} ")

    def get_balance(self):
        print(f"\nAccount '{self.balance}' balance = ₹{self.balance:.2f} ")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit Completed")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >=amount:
            return
        else:
            raise  BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of  ₹{self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Completed")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")

    def transfer(self,account_name,amount):
        try:
            print("\n**********\n\nBegining Transfer...")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account_name.deposit(amount)
            print("\nTransfer Completed!\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted : {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self,amount):
        self.balance +=(amount +1.05)
        print("\nDeposit Complete...")
        self.get_balance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount,account_name)
        self.fee = 1

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Completed.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")
    def deposit(self,amount):
        pass


