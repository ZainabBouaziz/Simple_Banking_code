class BankAccount :
    
    all_accounts=[]
    def __init__(self,int_rate,balance=0):
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)

    def deposit(self,amount):
        self.balance+=amount
        return self
    
    def withdraw(self,amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance-=amount
        else:
            print("insufficient Funds")
        return self
    
    def display_account_info(self):
        print('Balance:$',self.balance)
        return self
    
    def yield_interest(self):
        if (self.balance>=0):
            self.balance+=self.balance*self.int_rate
        return self
    
    @classmethod
    def all_infos(cls):
        for account in cls.all_accounts :
            account.display_account_info()
    
    @staticmethod
    def can_withdraw(balance,amount):
        if balance<amount :
            return False
        else:
            return True
        
class Retirement_Account(BankAccount):
    def __init__(self, int_rate,is_roth,balance=0):
        super().__init__(int_rate, balance)
        self.is_roth=is_roth

    def withdraw(self, amount,is_early):
        if is_early:
            amount=amount*1.1
        super().withdraw(amount)    
        return self