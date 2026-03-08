"""import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="שמך")
args: Namespace = parser.parse_args()
if args.name:
    print(f"שלום {args.name}!")
#מערכת פקודודות שיכולה לערוך את קבצי הjson ויכולת להפיל גם את הcvs"""

import time
import os
import sys

# מוסיף את תיקיית הבסיס של הפרויקט ל-PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.file_manager import FileManager

def search_account_info_To():
    account_number_To = "356270209"
    
    # נתיב מדויק לקובץ לפי מבנה הפרויקט
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "files", "accounts.json")
    
    data = FileManager(json_path, {"accounts": []}).load_data()
    
    for account in data["accounts"]:
        print(account)
        time.sleep(4)
        
        if account["account_number"] == account_number_To:
            return True, account
    
    print("account not found")
    return False, None

result = search_account_info_To()
print(result[0])
print(result[1])