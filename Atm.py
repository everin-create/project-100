class Atm(object):
    def __init__(self,atmcard,pinumber,cash,balance):
        self.atmcard=atmcard,
        self.pinumber=pinumber,
        self.cash=cash,
        self.balance=balance
    def withdrawal(self,cash):
        print("cash taken",self.cash)
    def balance(self,cash,balance):
        return sum(self.balance-self.cash)
        
Bank=Atm(32452324,5432,300,3000)
print(Bank.withdrawal(300))
print("bank balance",Bank.balance(3000))
    
        
    


