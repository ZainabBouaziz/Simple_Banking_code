from Bank_Account import BankAccount

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