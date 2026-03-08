
from core.transaction import Transaction,TransactionTo,TransactionUtils
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
SR=True
checking_dict=CheckingAccount.to_dict_account(CheckingAccount(**common))
if SR==False:
    T1=Transaction(transactionId=FileManager.task_id("files/transactionId.txt"),
                    amount=TransactionUtils.amount(69),
                    transactionType=TransactionUtils.transactionType("WITHDRAWAL"),
                    timestamp=TransactionUtils.time_now_update(),
                    account_info=checking_dict,
                    fee=7.5,
                    status=TransactionUtils.transactionStatus("COMPLETED"),
                    description=TransactionUtils.description("Initial deposit")
                    
                    )
else :
    T1=TransactionTo(transactionId=FileManager.task_id("files/transactionId.txt"),
                    amount=TransactionUtils.amount(69),
                    transactionType=TransactionUtils.transactionType("TRANSFER"),
                    timestamp=TransactionUtils.time_now_update(),
                    account_info=checking_dict,
                    fee=7.5,
                    status=TransactionUtils.transactionStatus("COMPLETED"),
                    description=TransactionUtils.description("Initial deposit")
                    ,account_number_To=TransactionUtils.account_number_To(356620657)
                    )
T1.cheack_status_transaction()
transaction_dict = T1.to_dict_transaction()

print(f"Account Balance: {T1.account_info['balance']}")
checking_dict = CheckingAccount.to_dict_account(CheckingAccount(**common))
balance_result = T1.change_balance()
checking_dict["balance"] = balance_result[0] 
T1.account_info = {k: v for k, v in checking_dict.items() if k != "transactions"}
checking_dict["transactions"].append(transaction_dict)


if SR:
    checking_dict_TO=T1.to_dict_account_transaction_TO()
    TO_balance=balance_result[1]
    checking_dict_TO["balance"]=TO_balance
    print(f"{TO_balance}TO_balance")
    transactionTO_dict=T1.to_dict_transaction_TO()
    transactionTO_dict["account_info"]["balance"] =TO_balance
    checking_dict_TO["transactions"].append(transactionTO_dict)

    


customer = FileManager("files/customers.json", {"customers": [dict_customer]})
accounts = FileManager("files/accounts.json", {"accounts": [checking_dict]})
transactions = FileManager("files/transactions.json", {"transactions": [transaction_dict]})

if SR:
    accountsTO=FileManager("files/accounts.json", {"accounts": [checking_dict_TO]})
    transactionsTO=FileManager("files/transactions.json", {"transactions": [transactionTO_dict]})

    files_list = [customer, accounts,transactions,accountsTO,transactionsTO]
else:
        files_list = [customer, accounts,transactions]




for file in files_list:
    file.ensure_file_exists()  

if SR:
 customer.save_data()
 accounts.save_data()
 transactions.save_data()
 accountsTO.delete_data()
 accountsTO.save_data()
 transactionsTO.save_data()

else:
    customer.save_data()
    accounts.save_data()
    transactions.save_data()

