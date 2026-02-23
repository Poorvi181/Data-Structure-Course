class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder= account_holder
        self.balance= balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited £{amount}. New balance: £{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew £{amount}. New balance: £{self.balance}")
        else:
            print("Insuffient funds!")

    def check_balance(self):
        print(f"Current balance: £{self.balance}")

account = BankAccount("Ava", 100)

account.deposit(50)
account.withdraw(30)
account.withdraw(200)   
account.check_balance()