import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.file_manager import task_id
from enum import Enum
from datetime import datetime   
class TransactionType(Enum):
    DEPOSIT = 1
    WITHDRAWAL = 2
    TRANSFER = 3

class TransactionStatus(Enum):
    COMPLETED = 1
    FAILED = 2
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
        if transaction_type in TransactionType:
            return transaction_type
        raise ValueError("Invalid transaction_type") 





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
    

    def to_dict(self):
        return {
            "transactionId": self.transactionId,
            "amount": self._amount,
            "transactionType": self.transactionType.name,
            "timestamp": self.timestamp,
            "account_info": self.account_info,
            "fee": self._fee,
            "status": self.status.name,
            "description": self.description
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
        if self.transactionType == self.transactionType.DEPOSIT:
            print("Daily withdrawal limit is not relevant for deposits.successful.")
            return True
        if self.transactionType == self.transactionType.WITHDRAWAL:
            if self.account_info["daily_withdrawal_limit"] >= self._amount:
                print("Daily withdrawal limit is sufficient.successful.")
                return True
        print("Daily withdrawal limit is insufficient.failed.")
        return False
    def acount_type(self):
        if self.account_info["account_type"] == "Checking":
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
            self.status = TransactionStatus.COMPLETED
        else:
            self.status = TransactionStatus.FAILED



    def change_balance(self, amount):
       cheack_status_transaction=self.cheack_status_transaction()
       if self.status == TransactionStatus.COMPLETED:
        if self.transactionType == TransactionType.DEPOSIT:
         self.account_info["balance"] += amount
        elif self.transactionType == TransactionType.WITHDRAWAL:
         self.account_info["balance"] -= amount + self._fee
    
       balance = self.account_info["balance"]  # ← בתוך ה-if!
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
        if self.transactionType == TransactionType.TRANSFER:
            self.account_info["balance"] -= amount- self._fee
            self.acount_info_To["balance"] += amount
            return self.acount_info_To["balance"]
# להוסיף שזה יוריד מהחשבון את הכסף        
    def search_account_info_To(self, account_number):
     pass    





T1=Transaction(transactionId=task_id("transactionId.txt"),
                amount=TransactionUtils.amount(100),
                transactionType=TransactionUtils.transactionType(TransactionType.DEPOSIT),
                timestamp=TransactionUtils.time_now_update(),
                account_info=account_info,
                fee=7.5,
                status=TransactionStatus.COMPLETED,
                description=TransactionUtils.description("Initial deposit"))

T1.cheack_status_transaction()
T1.change_balance(T1._amount)

for key, value in T1.to_dict().items():
    print(f"{key}: {value}")
print(T1.account_info["balance"])