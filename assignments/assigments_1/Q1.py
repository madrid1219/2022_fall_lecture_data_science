# Q1
# DO NOT CHANGE CLASS NAME!! #

class Bank():
    def __init__(self) -> None:
        # the information about account types
        # [key]: type of account -> [value]: the number of accounts opened
        self.total_accounts = {'checking': 0, 'saving': 0}
        # total balance of bank
        self.total_balance = 0
        # deposit per customer
        # [key]: name of customer -> [value]: total balance of the customer
        self.customers = dict() 
    
    def openAccount(self, accountType: str) -> None:
        self.total_accounts[accountType] += 1
    
    def changeDeposit(self, amount: int) -> None:
        self.total_balance += amount

    def updateBalancePerCustomer(self, customerName: str, amount: int) -> None:
        if not self.customers.get(customerName, False):
            self.customers[customerName] = amount
        else:
            self.customers[customerName] += amount


class Account():
    def __init__(self, owner: str, bank: Bank, accountType: str, initBalance: int):
        self.bank = bank
        self.owner = owner
        self.accountType = accountType
        self.balance = initBalance
        # Q1-1. Write your code below 
        # 3 more status should be updated with __init__
        # - When an account is opened, bank's account type info is updated
        # - total balance of the bank that issued this account increases as the "initBalance"
        # - the balance of the owner of this account is updated 
    
    def deposit(self, amount: int) -> None:
        # Q1-2. Write your code below
        # - when the input amount is 0 or less, print warning
        # - when the input amount is valid, 
        #   1) update the account's balance (+)
        #   2) update bank's customer dict
        #   3) update bank's total balance (+)
        #   4) print success message and current balance of the account 
        pass    

    def withdraw(self, amount: int) -> None:
        # Q1-3. Write your code below
        # - when the input amount is 0 or less, print warning
        # - When your input amount exceeds balance, print warning
        # - when the input amount is valid, 
        #   1) update the account's balance (-)
        #   2) update bank's customer dict
        #   3) update bank's total balance (-)
        #   4) print success message and current balance of the account
        pass