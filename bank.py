class Account:

    def __init__(self,Account_number,Account_holder_name,balance,interest_rate):
        self.Account_number=Account_number
        self.Account_holder_name=Account_holder_name
        self.balance=balance
        self.interest_rate=interest_rate


    def account_details(self):
        return(f"{self.Account_holder_name} whose account is{self.Account_number} has {self.balance} at interest of{self.interest_rate}") 

    def deposite(self,amount):
        self.balance+=amount
        return(f"{self.Account_holder_name}'s new balance is {self.balance}")    
    
    def withdraw(self,amount):
        self.balance-=amount
        return(f"{self.Account_holder_name}'s new balance is{self.balance}")

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest  
        return (f"your interest has been add to your balance your new balance is {self.balance} ")

