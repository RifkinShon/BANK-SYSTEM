from datetime import datetime
from file_manager import FileManager
import json



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
    sort_accounts()
    sort_customers()
    sort_transactions()