import argparse
from argparse import Namespace
# Command system for editing JSON and CSV files
print("# Command system for BANK system")
"""python utils/BANK_control.py """
""" השורה למעלה חייבת לכלול כדי שהקוד יתפקד כראוי, אחרת הוא לא יזהה את הפרמטרים שנשלחים מהטרמינל."""
parser = argparse.ArgumentParser(
    description="Command system for editing JSON and CSV files"
)

parser.add_argument(
    "-d", "--deletion",
    help="Deletes a dictionary by file path and account number — Enter: file_path account_number",
    nargs=2,
    metavar=("FILE_PATH", "ACCOUNT_NUMBER")
)

parser.add_argument(
    "-df", "--deletion_file",
    help="Deletes a file — Choose: A, B, C, T, T_ID",
    choices=["A", "B", "C", "T", "T_ID"]
)

parser.add_argument(
    "-e", "--edit",
    help="Edits a dictionary by file path and account number — Enter: file_path account_number attribute value",
    nargs=4,
    metavar=("FILE_PATH", "ACCOUNT_NUMBER", "ATTRIBUTE", "VALUE")
)

parser.add_argument(
    "-f","--freeze",
    help="Freezes an account based on its number"
)

parser.add_argument(
    "-uf","--un_freeze",
    help="Unfreezes an account based on its account number"
)
parser.add_argument(
    "-c","--close",
    help="Close an account based on its number"
)

parser.add_argument(
    "-a","--activate",
    help="Activate an account based on its number"  # תוקן: היה "Close" (העתק-הדבק שגוי)
)
parser.add_argument(
    "-v","--view",
    help="Looking at the file contents",
    choices=["A", "B", "C", "T", "T_ID"]
)

parser.add_argument(
    "-vw","--view_web",
    help="Looking at the file contents in html",
    choices=["A", "B", "C", "T", "T_ID"]
)

args: Namespace = parser.parse_args()


if args.deletion:
    from file_manager import FileManager

    FILE_PATHS = {
        "A": "files/accounts.json",
        "C": "files/customers.json",
        "T": "files/transactions.json"
    }

    file_key, account_number = args.deletion

    if file_key not in FILE_PATHS:
        print("Error: Invalid file key. Choose A (accounts), C (customers), or T (transactions).")
    else:
        file_path = FILE_PATHS[file_key]
        deletion_dict = FileManager(file_path, {"deletion": [{"account_number": account_number}]})
        deletion_dict.delete_data()

if args.deletion_file:
    from file_manager import FileManager

    FILE_PATHS = {
        "A": "files/accounts.json",
        "C": "files/customers.json",
        "T": "files/transactions.json",
        "B": "files/BANK_MONEY.json",
        "T_ID": "files/transactionId.txt"
    }

    file_key = args.deletion_file

    if file_key not in FILE_PATHS:
        print("Error: Invalid file key. Choose A, C, T, B, or T_ID.")
    else:
        file_path = FILE_PATHS[file_key]
        deletion_dict = FileManager(file_path, {})
        deletion_dict.delete_file()


if args.edit:
    from file_manager import FileManager

    FILE_PATHS = {
        "A": "files/accounts.json",
        "C": "files/customers.json",
        "T": "files/transactions.json",
    }

    file_key = args.edit[0]
    account_number = args.edit[1]
    attribute = args.edit[2]
    value = args.edit[3]

    if file_key not in FILE_PATHS:
        print("Error: Invalid file key. Choose A, C, T")
    else:
        file_path = FILE_PATHS[file_key]
        edit_dict = FileManager(file_path, {"edit": [{"account_number": account_number, "attribute": attribute, "value": value}]})
        edit_dict.edit_data()


if args.freeze:
    from file_manager import FileManager
    account_number = args.freeze
    edit_dict = FileManager("files/accounts.json", {"edit": [{"account_number": account_number, "attribute": "status", "value": "FROZEN"}]})
    edit_dict.edit_data()

if args.un_freeze:
    from file_manager import FileManager
    account_number = args.un_freeze
    edit_dict = FileManager("files/accounts.json", {"edit": [{"account_number": account_number, "attribute": "status", "value": "ACTIVE"}]})
    edit_dict.edit_data()

if args.close:
    from file_manager import FileManager
    account_number = args.close
    edit_dict = FileManager("files/accounts.json", {"edit": [{"account_number": account_number, "attribute": "status", "value": "CLOSED"}]})
    edit_dict.edit_data()

if args.activate:
    from file_manager import FileManager
    account_number = args.activate
    edit_dict = FileManager("files/accounts.json", {"edit": [{"account_number": account_number, "attribute": "status", "value": "ACTIVE"}]})
    edit_dict.edit_data()


if args.view:
    from pprint import pprint
    import json

    # תוקן: נוסף T_ID כדי להתאים ל-choices של הפרסר
    FILE_PATHS = {
        "A": "files/accounts.json",
        "C": "files/customers.json",
        "T": "files/transactions.json",
        "B": "files/BANK_MONEY.json",
        "T_ID": "files/transactionId.txt",
    }

    file_key = args.view

    if file_key not in FILE_PATHS:
        print("Error: Invalid file key. Choose A, C, T, B, or T_ID.")
    else:
        file_path = FILE_PATHS[file_key]
        # תוקן: הוספת טיפול בשגיאות (קובץ לא קיים / לא JSON תקין / ריק)
        try:
            if file_key == "T_ID":
                # transactionId.txt הוא קובץ טקסט רגיל, לא JSON
                with open(file_path, 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if not content.strip():
                    print(f"File '{file_path}' is empty.")
                else:
                    data = json.loads(content)
                    pprint(data, indent=2)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{file_path}' is not a valid JSON file.")


if args.view_web:
    from file_manager import FileManager
    import webbrowser
    import html as html_lib
    import os

    FILE_PATHS = {
        "A": "files/accounts.json",
        "C": "files/customers.json",
        "T": "files/transactions.json",
        "B": "files/BANK_MONEY.json",
        "T_ID": "files/transactionId.txt",
    }

    file_key = args.view_web

    if file_key not in FILE_PATHS:
        print("Error: Invalid file key. Choose A, C, T, B, or T_ID.")
    elif file_key == "T_ID":
        print("Error: T_ID is a plain text file and cannot be viewed as HTML table. Use -v T_ID instead.")
    else:
        file_path = FILE_PATHS[file_key]
        file = FileManager(file_path, {})

        try:
            data = file.load_data()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            data = None
        except ValueError:
            print(f"Error: File '{file_path}' is not a valid JSON file.")
            data = None

        if data:
            values = list(data.values())
            records = values[0] if values and isinstance(values[0], list) else []

            if not records:
                print(f"No records found in '{file_path}'.")
            else:
                rows = ""
                for item in records:
                    rows += "<tr>" + "".join(f"<td>{html_lib.escape(str(v))}</td>" for v in item.values()) + "</tr>"

                headers = "".join(f"<th>{html_lib.escape(str(k))}</th>" for k in records[0].keys())

                html_content = f"""
                <html>
                <body>
                <table border="1">
                <tr>{headers}</tr>
                {rows}
                </table>
                </body>
                </html>
                """

                # וודאות שתיקיית files קיימת
                os.makedirs("files", exist_ok=True)
                output_file = os.path.join("files", "view.html")

                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(html_content)

                webbrowser.open(output_file)
        elif data is not None:
            print(f"No data found in '{file_path}'.")