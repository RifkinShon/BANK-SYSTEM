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

def BANK_MONEY(fee,transactionType):
    import json
    import os
    if transactionType =="DEPOSIT":
        return
    file_path = "files/BANK_MONEY.json"
    
    # יוצר קובץ אם לא קיים
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({"BANK_MONEY": [{"total": 0}]}, file, indent=2)
    
    # טוען
    with open(file_path, 'r') as file:
        existing = json.load(file)
    
    # מוסיף את העמלה
    existing["BANK_MONEY"][0]["total"] += fee
    
    # שומר
    with open(file_path, 'w') as file:
        json.dump(existing, file, indent=2)