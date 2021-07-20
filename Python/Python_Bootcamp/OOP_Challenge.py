class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print('Deposit Accepted')

    def withdraw(self, money):
        if(self.balance - money >= 0):
            self.balance -= money
            print('Withdrawl Accepted')
        else:
            print('Funds Unavailable!')

    def __str__(self) -> str:
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"


# kb_ted = Account('Ted', 5000)
# print(kb_ted.balance)

# kb_ted.deposit(500)
# print(kb_ted.balance)

# kb_ted.withdraw(500)
# print(kb_ted.balance)

# kb_ted.withdraw(5500)
