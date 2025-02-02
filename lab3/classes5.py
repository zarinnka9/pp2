class Account:
    def __init__(self, owner, balance=0): 
        self.owner = owner
        self.balance = balance
    def deposit(self, amount): 
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. Updated Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds , withdrawal denied.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. New Balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive.")
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
acc = Account("Zarina", 1555)
print(acc)  

acc.deposit(75)
acc.withdraw(40)  
acc.withdraw(190)  
print(acc)  