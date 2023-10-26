import json
import config
import FileHandler
from random import randint

class Account:

    type = ''
    def __init__(self,user_id):
        self.user_id = user_id
        self.balance: int = 0
        self.account_id = self.account_id_generator()

    def get_balance(self):
        return self.balance
    def set_balance(self,amount):
        self.balance += amount

    def account_id_generator(self):
        return randint(0,9999999999)

    def view_accounts(self):
        data = FileHandler.read_file()
        return data

    def add_account(self):
        data = self.view_accounts()
        data.append(self.to_dict())
        FileHandler.write_file(data)
    def to_dict(self):
        return {'Account Id':self.account_id,'User Id':self.user_id,'Account_Type': self.type,'Balance':self.balance}



class FDRAccount(Account):
    type ='FDR Account'

    def __init__(self,user):
        super().__init__(user)


class CurrentAccount(Account):
    type = 'Current Account'

    def __init__(self,user):
        super().__init__(user)
        self.id = super().id

class SavingsAccount(Account):
    type = 'Savings Account'
    def __init__(self,user):
        super().__init__(user)


if __name__ == '__main__':
    user = {"fullname": "fahim","email": "mail4fahim@gmail.com"}
    ob = SavingsAccount(user)
    print(ob.to_dict())
    ob.add_account()
    temp = ob.view_accounts()
    print(temp)


def create_account(userid,account_type):

    if account_type == 1:
        ob = FDRAccount(userid)
        ob.add_account()
        print("Account is successfully created")
    elif account_type == 2:
        ob = CurrentAccount(userid)
        ob.add_account()
        print("Account is successfully created")
    elif account_type == 3:
        ob = SavingsAccount(userid)
        ob.add_account()
        print("Account is successfully created")
    else:
        print("pass a valid choice")


def get_account_balance(account_no):
    data = FileHandler.read_file()
    for temp in data:
        if temp['account_id'] == account_no
            return temp['balance']
