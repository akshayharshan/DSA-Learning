class BankAccount:
    def __init__(selef,balance):
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
    def get_balance(self):
        return self._balance

BankAccount()