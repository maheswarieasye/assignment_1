


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def deposit(self,deposit):

        deposit=1000
        self.deposit=self.balance+deposit

    def withdrawal(self, withdrawal):
        withdrawal=500
        self.withdrawal=self.amount1-withdrawal

    def getBalance(self):
        print("getbalance=",self.amount+self.balance)

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestrate=0):
            super().__init__(title, balance)
            self.interestrate = interestrate
    
    def interestamount(self):
        self.interestamount=(self.interestrate*self.balance)/100
    
    def display1(self):
        print("Title:",self.title)
        print("Balance:",self.balance)
        print("Interestrate:",self.interestrate)
        print("Interestamount:",self.interestamount)

obj= SavingsAccount("Ashish", 2000, 5) 
obj.deposit()
obj.withdrawal()
obj.interestamount()
obj.display1()

