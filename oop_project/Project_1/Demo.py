from oop_project.Project_1.BankAcccout import *

Deeps = BankAccount("Deeps", 100)
Siva = BankAccount("Siva", 500)

Deeps.get_balance()

Deeps.deposit(150)
Deeps.withdraw(3000000000)
Deeps.withdraw(150)
Deeps.transfer(Siva,50)

Siva.get_balance()

pavai = InterestRewardsAccount("Pavai",1000)
pavai.deposit(1000)

DSC = SavingsAccount("DSC",1000)
DSC.deposit(2000)
DSC.withdraw(1)