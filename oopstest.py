class account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f" Account onwer: {self.owner} \n Account balance is: {self.balance}"

    def deposit(self,amount):
        print("deposit accepted")
        self.balance = self.balance + amount


    def withdraw(self,amount):
        if amount> self.balance:
            print("Funds unavailable")
        else:
            print("Withdrawal accepted")
            self.balance = self.balance - amount

acc1 = account("Joe", 100)
print(acc1)

print(acc1.owner)
print(acc1.balance)

acc1.deposit(90)
print(acc1.balance)

acc1.withdraw(100)
print(acc1.balance)

acc1.withdraw(100)

acc1.deposit(400)
print(acc1.balance)

acc1.withdraw(490)
print(acc1.balance)