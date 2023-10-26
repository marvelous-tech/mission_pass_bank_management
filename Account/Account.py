import json
import config
import FileHandler

class Account:

    type = ''
    id:int
    def __init__(self,user):
        self.user = user
        self.balance: int = 0
        self.id += 1

    def get_balance(self):
        return self.balance
    def set_balance(self,amount):
        self.balance += amount

    def add_account(self):
        pass

    def to_dict(self):
        return {'AccountId':self.id,'Fullname':self.user['fullname'],'email':self.user['email'],'Account_Type': self.type,'Balance':self.balance}



class FDRAccount(Account):
    type ='FDR Account'
    id:int

    def __init__(self,user):
        super().__init__(user)
        self.id = super().id


class CurrentAccount(Account):
    type = 'Current Account'

    def __init__(self,user):
        super().__init__(user)
        self.id = super().id

class SavingsAccount(Account):
    type = 'Savings Account'
    def __init__(self,user):
        super().__init__(user)
        self.id = super().id


if __name__ == '__main__':
    user = {'fullname': 'shrif', 'email': 'mail4newaj@gmail.com'}
    ob = CurrentAccount(user)
    #ob.add_account()
    print(ob.id)
    print(ob.type)