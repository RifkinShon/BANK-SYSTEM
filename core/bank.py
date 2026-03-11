"""import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="שמך")
args: Namespace = parser.parse_args()
if args.name:
    print(f"שלום {args.name}!")
#מערכת פקודודות שיכולה לערוך את קבצי הjson ויכולת להפיל גם את הcvs"""
class BANK:


    @staticmethod
    def BANK_MONEY(fee,transactionType):
        import os
        import sys
        import json
        import os

        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


        if transactionType =="DEPOSIT":
            return
        file_path = "files/BANK_MONEY.json"
        
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump({"BANK_MONEY": [{"total": 0}]}, file, indent=2)
        
        with open(file_path, 'r') as file:
            existing = json.load(file)
        
        existing["BANK_MONEY"][0]["total"] += fee
        
        with open(file_path, 'w') as file:
            json.dump(existing, file, indent=2)
    @staticmethod
    def loan_money(amount):
        import os
        import sys
        import json
        import os

        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


    
        file_path = "files/BANK_MONEY.json"
        
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump({"BANK_MONEY": [{"total": 0}]}, file, indent=2)
        
        with open(file_path, 'r') as file:
            existing = json.load(file)
        
        existing["BANK_MONEY"][0]["total"] += amount
        
        with open(file_path, 'w') as file:
            json.dump(existing, file, indent=2)
        print(f"{amount} of loan money got added to the BANK")
        return


    @staticmethod
    def loan_interest():
        import os
        import sys
        import json
        from datetime import datetime
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from utils.file_manager import FileManager

        file = FileManager("files/accounts.json", {"accounts": []})
        data = file.load_data()

        now = datetime.now()

        for account in data["accounts"]:

            if account.get("account_type", "").upper() != "LOAN":
                continue

            if account.get("status", "").upper() == "CLOSED":
                print(f"Account {account['account_number']} is closed - skipping")
                continue

            update_time = account["updata_time"].strip()
            update_dt = datetime.strptime(update_time, "%Y-%m-%d")
            months_passed = (now.year - update_dt.year) * 12 + (now.month - update_dt.month)

            if months_passed <= 0:
                print(f"Account {account['account_number']} - less than a month since last update")
                continue

            credit_score = account["credit_score"]
            if credit_score >= 700:
                interest_rate = 0.03  
            elif credit_score >= 500:
                interest_rate = 0.05  
            else:
                interest_rate = 0.08  

            balance = account["balance"]
            new_balance = round(balance * ((1 + interest_rate) ** months_passed), 2)
            account["balance"] = new_balance

            account["updata_time"] = now.strftime("%Y-%m-%d")

            if new_balance >= 0:
                account["status"] = "CLOSED"
                print(f"Account {account['account_number']} closed - balance {new_balance} reached zero or above")
            else:
                print(f"Account {account['account_number']}: {balance} → {new_balance} ({months_passed} months, {interest_rate*100}% interest)")

        with open("files/accounts.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Interest rates updated successfully")

    @staticmethod
    def saving_interest():
            import os
            import sys
            import json
            from datetime import datetime
            sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            from utils.file_manager import FileManager

            file = FileManager("files/accounts.json", {"accounts": []})
            data = file.load_data()

            now = datetime.now()

            for account in data["accounts"]:

                if account.get("account_type", "").upper() != "SAVINGS":
                    continue

                if account.get("status", "").upper() == "CLOSED":
                    print(f"Account {account['account_number']} is closed - skipping  - balance {new_balance} ")

                    continue

                update_time = account["updata_time"].strip()
                update_dt = datetime.strptime(update_time, "%Y-%m-%d")
                months_passed = (now.year - update_dt.year) * 12 + (now.month - update_dt.month)

                if months_passed <= 0:
                    print(f"Account {account['account_number']} - less than a month since last update")
                    continue


                created_time = account["created_time"].strip()
                created_dt = datetime.strptime(created_time, "%Y-%m-%d")
                years_active = (now.year - created_dt.year)
                if years_active >= 10:
                    interest_rate = 0.08  
                elif years_active >= 5:
                    interest_rate = 0.05  
                elif years_active >= 2:
                    interest_rate = 0.03 
                else:
                    interest_rate = 0.02  

                balance = account["balance"]
                new_balance = round(balance * ((1 + interest_rate) ** months_passed), 2)
                account["balance"] = new_balance

                account["updata_time"] = now.strftime("%Y-%m-%d")

                print(f"Account {account['account_number']}: {balance} → {new_balance} ({months_passed} months, {interest_rate*100}% interest)")

            with open("files/accounts.json", "w") as f:
                json.dump(data, f, indent=2)
            print("Interest rates updated successfully")
if __name__ == "__main__":    
    BANK.loan_money(6900000)      
    BANK.loan_interest()
    BANK.saving_interest()