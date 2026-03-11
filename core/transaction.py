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
    @staticmethod
    def account_number_To(account_number_To):
        star_account_number_To=str(account_number_To)
        if  len(star_account_number_To) <= 11 and star_account_number_To[0:3]=="356":
            return account_number_To
        raise ValueError("num have to follow standard.")
 




class Transaction:
    def __init__(self, transactionId, amount, transactionType, timestamp, account_info, fee, status, description):
        self.transactionId = transactionId
        self.amount = amount                    
        self.transactionType = transactionType
        self.timestamp = timestamp
        self.account_info = account_info
        self.fee = fee                          
        self.status = status               
        self.description = description
    
    def to_remove_transaction_from_info(self):
        if "transactions" in self.account_info:
         del self.account_info["transactions"]
        return self.account_info
    def to_dict_transaction(self):
        account_info = self.to_remove_transaction_from_info()
        return {
            "transactionId": self.transactionId,
            "amount": self.amount,
            "transactionType": self.transactionType,
            "timestamp": self.timestamp,
            "fee": self.fee,
            "status": self.status,
            "description": self.description,
            "account_info": account_info,
        }   
    def calculate_amount_in_account(self):
        if int(self.account_info["balance"]) >= self.amount+self.fee:
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
        if self.transactionType == "WITHDRAWAL" or  self.transactionType == "TRANSFER" :
            if self.account_info["daily_withdrawal_limit"] >= self.amount+self.fee:
                print("Daily withdrawal limit is sufficient.successful.")
                return True

        print("Daily withdrawal limit is insufficient.failed.")
        return False
    def acount_type(self):
        if self.account_info["account_type"] == "CHECKING":
            print("Account type is checking.successful.")
            return True
        elif self.account_info["account_type"] == "SAVINGS" and self.account_info["status"] == "CLOSED":
            print("Account type is saving and it is closed.successful.")
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



    def change_balance(self):
       print(f"{self.account_info["balance"]}balance before ") 
       if self.status == "COMPLETED":
        if self.transactionType == "DEPOSIT":
         self.account_info["balance"] += self.amount
        elif self.transactionType == "WITHDRAWAL":
         self.account_info["balance"] -= self.amount + self.fee
    
       balance = self.account_info["balance"]  
       print(balance)
       return balance,None
# להוסיף שזה יוריד מהחשבון את הכסף      
# צריך שזה שזה ימחוק מילון עם אותו נתונים עם קיים וירשום את המילון החדש  




print
class TransactionTo(Transaction):
    def __init__(self, transactionId, amount, transactionType, timestamp, account_info, fee, status, description, account_number_To):
        super().__init__(transactionId, amount, transactionType, timestamp, account_info, fee, status, description)
        self.account_number_To = account_number_To
    def to_dict_transaction(self):
        data = super().to_dict_transaction()
        new_data = {}
        
        for key, value in data.items():
            if key == "account_info":
                new_data["account_number_To"] =str( self.account_number_To)  # ← לפני description
            new_data[key] = value
        return new_data
    def to_dict_transaction_TO(self):
        data = super().to_dict_transaction()
        new_data = {}
        
        for key, value in data.items():
            if key == "account_info":
                new_data["account_number_To"] = str(self.account_info["account_number"])
                # ← מסיר transactions מתוך account_info
                new_data[key] = {k: v for k, v in self.account_info.items() if k != "transactions"}
            else:
                new_data[key] = value
        
        new_data["fee"] = 0
        dictTO_account = self.search_account_info_To()
        new_data["account_info"] = {k: v for k, v in dictTO_account[1].items() if k != "transactions"}
        return new_data

    def to_dict_account_transaction_TO(self):
        to_find_account_To=self.search_account_info_To()

        return to_find_account_To[1]


    def search_account_info_To(self):
        import os
        import sys
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from utils.file_manager import FileManager 
        data = FileManager("files/accounts.json", {"accounts": []}).load_data()
        for account in data["accounts"]:
            
            if account["account_number"] == str(self.account_number_To):
                return True, account
        
        raise ValueError("account not found")
    

    def not_same_account(self):
        if self.account_info["account_number"]==self.account_number_To:
            return False
        return True




    def change_balance(self):
        from core.BANK import BANK
        to_find_account_To=self.search_account_info_To()
        if self.transactionType == "TRANSFER":
            if self.status=="COMPLETED":
                self.account_info["balance"] -= self.amount+ self.fee
                to_find_account_To[1]["balance"] += self.amount
                account_info=self.account_info["balance"]
                if to_find_account_To[1]["account_type"]=="LOAN":#פונקציה שנותנת לבנק את הכסף מהלוואה
                    BANK.loan_money(self.amount)
                return  account_info,to_find_account_To[1]["balance"]
            else:
                return  self.account_info["balance"],to_find_account_To[1]["balance"]


# להוסיף שזה יוריד מהחשבון את הכסף        

    def cheack_status_transaction(self):
        super().cheack_status_transaction()
        search_account_info_To=self.search_account_info_To()
        not_same_account=self.not_same_account()
        if self.status=="COMPLETED":
         if search_account_info_To[0] and not_same_account:
            print("status is COMPLETED")
            return
        self.status = "FAILED"



