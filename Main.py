from enum import Enum

from core.transaction import Transaction,TransactionUtils
from core.customer import Customer,CustomerUtils
from core.account import AccountUtils, CheckingAccount, LoanAccount, SavingsAccount
from utils.file_manager import FileManager 


Customer1 = Customer(
    customer_id=CustomerUtils.id_number("123456789"),
    name=CustomerUtils.name("John Doe"),
    age=CustomerUtils.age(30),
    email=CustomerUtils.email("johndoe@gmail.com"),
    phone=CustomerUtils.phone("0501234567"),
    account_number=CustomerUtils.account_number(),
    address=CustomerUtils.address("123 Main St, City, Country"),
    password=CustomerUtils.password(1235643223),
    role=CustomerUtils.customerRole("CLIENT"),
    credit_score=CustomerUtils.credit_score(),
    created_time=CustomerUtils.created_time(),
    account_type=CustomerUtils.account_type("CHECKING")
)
dict_customer=Customer1.to_dict_customer()

    
    # הנתונים המשותפים לכולם
common = {
        "account_number": dict_customer["account_number"],
        "ownerId": dict_customer["customer_id"],
        "account_holder": dict_customer["name"],
        "balance": AccountUtils.balance(dict_customer["account_type"]),
        "status": "ACTIVE",
        "daily_withdrawal_limit": dict_customer["credit_score"] * 12.57,
        "transactions": [],
        "credit_score": dict_customer["credit_score"],
        "created_time": dict_customer["created_time"]
    }
    
 

account_type = dict_customer["account_type"]
if account_type == "CHECKING":
    checkingAccount = CheckingAccount(**common)
elif account_type == "SAVINGS":
    savingsAccount = SavingsAccount(**common)
elif account_type == "LOAN":
    loanAccount = LoanAccount(**common)





















print(common)
T1=Transaction(transactionId=FileManager.task_id("files/transactionId.txt"),
                amount=TransactionUtils.amount(100),
                transactionType=TransactionUtils.transactionType("DEPOSIT"),
                timestamp=TransactionUtils.time_now_update(),
                account_info=CheckingAccount.to_dict_account(CheckingAccount(**common)),
                fee=7.5,
                status=TransactionUtils.transactionStatus("COMPLETED"),
                description=TransactionUtils.description("Initial deposit"))

T1.cheack_status_transaction()
T1.change_balance(T1._amount)




checking_dict = CheckingAccount.to_dict_account(CheckingAccount(**common))
transaction_dict = T1.to_dict_transaction()
dict_customer = dict_customer

customer = FileManager("files/customers.json", {"customers": [dict_customer]})
accounts = FileManager("files/accounts.json", {"accounts": [checking_dict]})
transactions = FileManager("files/transactions.json", {"transactions": [transaction_dict]})

files_list = [customer, accounts, transactions]

for file in files_list:
    file.ensure_file_exists()  
customer.save_data({"customers": [dict_customer]})
accounts.save_data({"accounts": [checking_dict]})
transactions.save_data({"transactions": [transaction_dict]})
