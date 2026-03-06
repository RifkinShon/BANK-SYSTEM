
from datetime import datetime

class TransactionUtils:
    @staticmethod
    def time_now_update():
        from datetime import datetime
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def amount(amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount < 0 :
            raise ValueError("Amount must be greater than zero.")
        return amount
        
    @staticmethod
    def description(description):

        if description:
            return description
        else:
            raise ValueError("Description cannot be empty.")
    @staticmethod
    def transactionType(transaction_type):
        if transaction_type in ["DEPOSIT", "WITHDRAWAL", "TRANSFER"]:
            return transaction_type
        raise ValueError("Invalid Transaction Type")
    @staticmethod
    def transactionStatus(transaction_status):
        if transaction_status in ["COMPLETED", "FAILED"]:
            return transaction_status
        raise ValueError("Invalid Transaction Status")




class Transaction:
    def __init__(self, transactionId, amount, transactionType, timestamp, account_info, fee, status, description):
        self.transactionId = transactionId
        self._amount = amount                    
        self.transactionType = transactionType
        self.timestamp = timestamp
        self.account_info = account_info
        self._fee = fee                          
        self.status = status               
        self.description = description
    
    def to_remove_transaction_from_info(self):
        del self.account_info["transactions"]
        return self.account_info
    def to_dict_transaction(self):
        account_info = self.to_remove_transaction_from_info()
        return {
            "transactionId": self.transactionId,
            "amount": self._amount,
            "transactionType": self.transactionType,
            "timestamp": self.timestamp,
            "fee": self._fee,
            "status": self.status,
            "description": self.description,
            "account_info": account_info,
        }   
    def calculate_amount_in_account(self):
        if int(self.account_info["balance"]) >= self._amount+self._fee:
            print("Sufficient balance in the account.successful.")
            return True
        else:
            print("Insufficient balance in the account.failed.")
            return False
    def cheack_status_account(self):
        if self.account_info["status"] == "ACTIVE" or self.account_info["status"] == "CLOSED":
            print("Account status is active.successful.")
            return True
        else:
            print("Account status is not active.failed.")
            return False
    def cheack_daily_withdrawal_limit(self):
        if self.transactionType == "DEPOSIT":
            print("Daily withdrawal limit is not relevant for deposits.successful.")
            return True
        if self.transactionType == "WITHDRAWAL":
            if self.account_info["daily_withdrawal_limit"] >= self._amount:
                print("Daily withdrawal limit is sufficient.successful.")
                return True
        print("Daily withdrawal limit is insufficient.failed.")
        return False
    def acount_type(self):
        if self.account_info["account_type"] == "CHECKING":
            print("Account type is checking.successful.")
            return True
        else:
            print("Account type is not checking.failed.")
            return False
    
    def cheack_status_transaction(self):
        calculate_amount_in_account=self.calculate_amount_in_account()
        cheack_status_account=self.cheack_status_account()
        cheack_daily_withdrawal_limit=self.cheack_daily_withdrawal_limit()
        acount_type=self.acount_type()
        if acount_type and calculate_amount_in_account and cheack_status_account and cheack_daily_withdrawal_limit:
            self.status = "COMPLETED"
        else:
            self.status = "FAILED"



    def change_balance(self, amount):
       cheack_status_transaction=self.cheack_status_transaction()
       if self.status == "COMPLETED":
        if self.transactionType == "DEPOSIT":
         self.account_info["balance"] += amount
        elif self.transactionType == "WITHDRAWAL":
         self.account_info["balance"] -= amount + self._fee
    
       balance = self.account_info["balance"]  
       print(balance)
       return balance
# להוסיף שזה יוריד מהחשבון את הכסף        


class TransactionTo(Transaction):
    def __init__(self, transactionId, amount, transactionType, timestamp, account_info, fee, status, description, acount_info_To):
        super().__init__(transactionId, amount, transactionType, timestamp, account_info, fee, status, description)
        self.acount_info_To = acount_info_To

    def to_dict(self):
        data = super().to_dict()
        data["acount_info_To"] = self.acount_info_To
        return data
    
    def change_balance(self, amount):
        if self.transactionType == "TRANSFER":
            self.account_info["balance"] -= amount- self._fee
            self.acount_info_To["balance"] += amount
            return self.acount_info_To["balance"]
# להוסיף שזה יוריד מהחשבון את הכסף        
    def search_account_info_To(self, account_number):
     pass    





