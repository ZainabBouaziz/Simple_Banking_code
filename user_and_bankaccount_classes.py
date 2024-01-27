
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

class User:
    
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate=0.2,balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print('User:',self.name)
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self


zainab=User('zainab','zainab.bouaziz@gmail.com')
merya=User('merya','merya.bouaziz@gmail.com')
zainab.make_deposit(50).display_user_balance().transfer_money(merya,20).display_user_balance()
merya.display_user_balance()





"""
BA_1=BankAccount(0.02)
BA_2=BankAccount(0.01,100)

BA_1.deposit(50).deposit(50).deposit(60).withdraw(10).withdraw(1000).yield_interest().display_account_info()

BA_2.deposit(70).deposit(70).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()

BA_3=BankAccount(0.01,20)

print(50*'*')

BankAccount.all_infos()
"""