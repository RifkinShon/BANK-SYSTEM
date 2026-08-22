from datetime import datetime
import json
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from file_manager import FileManager

class SortUtils:
    def sort_accounts() -> dict:

        ACCOUNT_TYPE_ORDER = {"CHECKING": 0, "SAVINGS": 1, "LOAN": 2}
        
        fm = FileManager("files/accounts.json", {"accounts": []})
        data = fm.load_data()

        data["accounts"].sort(
            key=lambda account: (
                ACCOUNT_TYPE_ORDER.get(account.get("account_type", "").upper(), 99),
                datetime.strptime(account.get("created_time", "").strip(), "%Y-%m-%d")
            )
        )

        with open("files/accounts.json", 'w') as file:
            json.dump(data, file, indent=2)
            print(f"JSON file 'files/accounts.json' has been saved successfully")




    def sort_customers() -> dict:
        fm = FileManager("files/customers.json", {"customers": []})
        data = fm.load_data()

        # הסרת כפיליות בסט
        seen = set()
        unique_customers = []
        
        for customer in data["customers"]:
            key = (customer.get("customer_id"), customer.get("account_number"))
            
            if key not in seen:
                seen.add(key)
                unique_customers.append(customer)
        
        data["customers"] = unique_customers

        # מיון לפי תאריך
        data["customers"].sort(
            key=lambda customer: datetime.strptime(customer.get("created_time", "").strip(), "%Y-%m-%d")
        )

        with open("files/customers.json", 'w') as file:
            json.dump(data, file, indent=2)
            print(f"JSON file 'files/customers.json' has been saved successfully")

    def sort_transactions() -> dict:

        fm = FileManager("files/transactions.json", {"transactions": []})
        data = fm.load_data()

        data["transactions"].sort(
            key=lambda transaction: transaction.get("transactionId", 0)
        )

        with open("files/transactions.json", 'w') as file:
            json.dump(data, file, indent=2)
            print(f"JSON file 'files/transactions.json' has been saved successfully")



if __name__ == "__main__":    
    SortUtils.sort_accounts()
    SortUtils.sort_customers()
    SortUtils.sort_transactions()