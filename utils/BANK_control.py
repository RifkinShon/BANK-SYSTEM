import argparse
from argparse import Namespace

# Command system for editing JSON and CSV files
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
    "-c","--close ",
    help="Close an account based on its number"
)

parser.add_argument(
    "-v","--view ",
    help="Looking at the file contents",
    choices=["A", "B", "C", "T", "T_ID"]
)

args: Namespace = parser.parse_args()

if args.name:
    print(f"Hello {args.name}!")