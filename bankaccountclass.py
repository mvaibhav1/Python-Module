class BankAcoount() :
    def __init__(self,name,balance=0):
        self.account_holder=name
        self.balance=balance

    def statement(self):
        print(f" Balance of {self.account_holder} is : {self.balance}")
    def deposit(self,amount_add=0):
        self.balance+=amount_add
        print(f"Credited {amount_add} \nNew balance of {self.account_holder} is : {self.balance}")
    
    def withdraw(self,amount_debit=0):
        if(self.balance>=amount_debit):
            self.balance-=amount_debit
            print(f''' Debited {amount_debit}
 New Balance :{self.balance}''')
        else:
            print("Insufficient Funds")

p1=BankAcoount("Sam")
p2=BankAcoount("Vaibhav",1000)
p1.statement()
p2.statement()
p1.deposit(500)
p1.withdraw(250)
p1.statement()
p2.deposit(4000)