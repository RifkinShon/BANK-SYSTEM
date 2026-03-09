from abc import abstractmethod


class AccountUtils:
       @staticmethod
       def balance(account_type):
        import random
        if account_type == "CHECKING":
            ranges = [
                (0, 500),
                (500, 3000),
                (3000, 10000),
                (10000, 30000),
                (30000, 100000),
                (100000, 1000000),
                (1000000, 50000000),
                (50000000, 1000000000)
            ]
            weights = [2000, 2800, 2300, 1300, 800, 500, 190, 10]

        elif account_type == "SAVINGS":
            ranges = [
                (0, 1000),
                (1000, 10000),
                (10000, 50000),
                (50000, 200000),
                (200000, 1000000),
                (1000000, 10000000),
                (10000000, 100000000),
                (100000000, 10000000000)
            ]
            weights = [2500, 2800, 2200, 1200, 700, 300, 190, 10]

        elif account_type == "LOAN":
            ranges = [
                (-5000, -1000),
                (-20000, -5000),
                (-100000, -20000),
                (-400000, -100000),
                (-1000000, -400000),
                (-5000000, -1000000),
                (-50000000, -5000000),
                (-1000000000, -50000000)
            ]
            weights = [1500, 2500, 2500, 1800, 1000, 400, 190, 10]
        selected_range = random.choices(ranges, weights=weights, k=1)[0]
        return random.randint(selected_range[0], selected_range[1])

           
@abstractmethod
class Account:
    def __init__(self, account_number,ownerId, account_holder, account_type, balance, status, daily_withdrawal_limit,transactions,credit_score,created_time):
        self.account_number = account_number
        self.ownerId=ownerId
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance
        self.status = status
        self.daily_withdrawal_limit = daily_withdrawal_limit
        self.transactions=transactions
        self.credit_score=credit_score
        self.created_time=created_time

    def to_dict_account(self):
        return {
            "account_number": self.account_number,
            "ownerId": self.ownerId,
            "account_holder": self.account_holder,
            "account_type": self.account_type,
            "balance": self.balance,
            "status": self.status,
            "daily_withdrawal_limit": self.daily_withdrawal_limit,
            "credit_score": self.credit_score,
            "created_time":self.created_time,
            "transactions": self.transactions,

        }      
    def freeze_account(self):
        self.status = "FROZEN"
    def unfreeze_account(self):
        self.status = "ACTIVE"
    def close_account(self):
        self.status = "CLOSED"


class CheckingAccount(Account):
    def __init__(self, account_number,ownerId, account_holder, balance, status, daily_withdrawal_limit,transactions,credit_score,created_time):
        super().__init__(account_number,ownerId, account_holder, "CHECKING", balance, status, daily_withdrawal_limit,transactions,credit_score,created_time)

class SavingsAccount(Account):
    def __init__(self, account_number,ownerId, account_holder, balance, status, daily_withdrawal_limit,transactions,credit_score,created_time):
        super().__init__(account_number,ownerId, account_holder, "SAVINGS", balance, status, daily_withdrawal_limit,transactions,credit_score,created_time)
    

    def to_dict_account(self):
        data = super().to_dict_account()
        data["account_type"] = "SAVINGS"
        if data["transactions"] in data:
         del data["transactions"]
        return data
     

    
    
    def cumulate_interest(self, interest_rate):
        monthly_interest = self.apply_monthly_intest_rate(self.created_time)
        self.balance += self.balance *((interest_rate+1)/12)
        if monthly_interest>12:
           self.status = "CLOSED"
    
        
    def apply_monthly_intest_rate(self,created_time):
        from datetime import datetime
        now = datetime.now()
        date=now.strftime("%Y-%m")
        start_date=created_time[5:7]
        monthly_interest=abs(int(date) - int(start_date))
        return monthly_interest
class LoanAccount(Account):
    def __init__(self, account_number,ownerId, account_holder, balance, status, daily_withdrawal_limit,transactions,credit_score,created_time):
        super().__init__(account_number,ownerId, account_holder, "LOAN", balance, status, daily_withdrawal_limit,transactions,credit_score,created_time)
    
    def to_dict_account(self):
        data = super().to_dict_account()
        data["account_type"] = "LOAN"
        if data["transactions"] in data:
         del data["transactions"]
        return data
     


    def cumulate_interest(self, credit_score):
        yearly_interest = self.apply_yearly_intest_rate(self.created_time)
        self.balance += self.balance *(1/(credit_score*100))*yearly_interest
        if self.balance<0:
           self.status = "CLOSED"

        
    def apply_yearly_intest_rate(self,created_time):
        from datetime import datetime
        now = datetime.now()
        date=now.strftime("%Y")
        start_date=created_time[1:4]
        yearly_interest=abs(int(date) - int(start_date))
        return yearly_interest
    def make_payment(self, payment_amount):
        if payment_amount > 0:
            self.balance -= payment_amount
            if self.balance < 0:
                self.status = "CLOSED"
        else:
            raise ValueError("Payment amount must be greater than zero.")
