#5. Bank account
# Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Added ${amount}. Balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance -= amount
            print(f"Withdraw ${amount}. Balance: ${self.balance}")
        
acc = account("John", 100)
acc.deposit(1000)
acc.withdraw(30)
acc.withdraw(200)