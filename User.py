from Bank_Account import Checking_Account,Retirement_Account,BankAccount

class User:
    
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account={
            'checking':Checking_Account(int_rate=0.2,balance=0),
            'Retirement':Retirement_Account(int_rate=0.2,is_roth=False,balance=0),
        }

    def make_deposit(self,amount,account):
        self.account[account].deposit(amount)
        return self

    def make_withdrawal(self,amount,account):
        self.account[account].withdraw(amount)
        return self
    
    def display_user_balance(self,account):
        print('User:',self.name)
        print(account)
        self.account[account].display_account_info()
        return self

    def transfer_money(self, other_user, amount,account_1,account_2):
        self.account[account_1].withdraw(amount)
        other_user.account[account_2].deposit(amount)
        return self
    
""" 
zainab=User('zainab','zainab.bouaziz@gmail.com')
merya=User('merya','merya.bouaziz@gmail.com')

zainab.make_deposit(50,'checking').display_user_balance('checking').make_deposit(20,'Retirement').display_user_balance('Retirement').transfer_money(merya,50,'checking','Retirement').display_user_balance('checking')
merya.display_user_balance('Retirement')


"""