"""def exceptions():
  exceptions = [
    ValueError("ערך לא תקין"),         # ערך שגוי
    TypeError("סוג לא תקין"),           # סוג שגוי (int במקום str)
    KeyError("מפתח לא קיים"),           # מפתח לא קיים במילון
    IndexError("אינדקס לא קיים"),       # אינדקס לא קיים ברשימה
    AttributeError("תכונה לא קיימת"),  # תכונה לא קיימת באובייקט
    FileNotFoundError("קובץ לא נמצא"), # קובץ לא נמצא
    ZeroDivisionError("חלוקה באפס"),   # חלוקה באפס
    PermissionError("אין הרשאה"),       # אין הרשאה
    TimeoutError("פג תוקף"),            # פג תוקף
    NotImplementedError("לא ממומש"),    # פונקציה שעוד לא ממומשת
    RuntimeError("שגיאת ריצה"),
]"""


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