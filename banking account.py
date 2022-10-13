class account:
    def __init__(self,name=None,balance=0):
        self.name=name
        self.balance=balance


        

class savingaccount(account):
    def __init__(self,name=None,balance=0,interestrate=0):
        super().__init__(name,balance)
        self.interestrate=interestrate 

    def display1(self):
        print("Title:",self.name)
        print("Balance:",self.balance)
        print("Interestrate:",self.interestrate)

obj=savingaccount("mahesh",5000,5)
obj.display1()

