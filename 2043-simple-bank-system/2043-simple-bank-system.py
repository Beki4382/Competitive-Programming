class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.balance_len = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        
        if account1 <= self.balance_len and account2 <= self.balance_len:
            
            if self.withdraw(account1, money):
                self.deposit(account2, money)
                return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if account > self.balance_len:
            return False
        self.balance[account-1] += money
        return True
        
    def withdraw(self, account: int, money: int) -> bool:
        if account > self.balance_len or money > self.balance[account-1] :
            return False
        
        self.balance[account-1] -= money
        return True
        
