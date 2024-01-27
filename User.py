from Bank_Account import Checking_Account,Retirement_Account,BankAccount

class User:
    
    def __init__(self,name,email,account):
        self.name=name
        self.email=email
        self.account=account

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
        self.account.balance-=amount
        other_user.account.deposit(amount)
        return self
    
RBA_1=Retirement_Account(0.1,0)
CBA_1=Checking_Account(0.2,0)
zainab=User('zainab','zainab.bouaziz@gmail.com',RBA_1)
merya=User('merya','merya.bouaziz@gmail.com',CBA_1)
zainab.make_deposit(50).display_user_balance().make_deposit(20).display_user_balance().transfer_money(merya,50).display_user_balance()
merya.display_user_balance()



