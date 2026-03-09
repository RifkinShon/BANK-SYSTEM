
from core.transaction import Transaction,TransactionTo,TransactionUtils
from core.customer import Customer,CustomerUtils
from core.account import AccountUtils, CheckingAccount, LoanAccount, SavingsAccount
from core.BANK import BANK_MONEY
from utils.file_manager import FileManager 

def login_or_create(RS):
    # True is login
    if RS == True or RS == False:
     return RS
    
def transaction_type(SR):
    #True is TRANSPER
    if SR == True or SR == False:
     return SR

login_or_create=login_or_create(False)
transaction_type=transaction_type(False)




#----------
#Customer
#---------
if login_or_create:
    data=CustomerUtils.login(356619064,1235643223)
    Customer1 = Customer.from_dict(data) 
    dict_customer_login=Customer1.to_dict_customer()
    customer_login = FileManager("files/customers.json", {"customers": [dict_customer_login]})
    customer_login.delete_data()



else:
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

    


 #----------
#Account
#---------   

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


checking_dict=CheckingAccount.to_dict_account(CheckingAccount(**common))

common_transaction = {
    "transactionId": FileManager.task_id("files/transactionId.txt"),
    "amount": TransactionUtils.amount(69),
    "timestamp": TransactionUtils.time_now_update(),
    "account_info": checking_dict,
    "fee": 7.5,
    "status": TransactionUtils.transactionStatus("COMPLETED"),
    "description": TransactionUtils.description("Initial deposit")
}



 #----------
#Transaction
#---------   


if transaction_type:
        T1 = TransactionTo(
        **common_transaction,
        transactionType=TransactionUtils.transactionType("TRANSFER"),
        account_number_To=TransactionUtils.account_number_To(356619064)
    )

else:
    T1 = Transaction(
        **common_transaction,
        transactionType=TransactionUtils.transactionType("WITHDRAWAL")
    )




if transaction_type:
    T1.cheack_status_transaction()
    transaction_dict = T1.to_dict_transaction()

    print(f"Account Balance: {T1.account_info['balance']}")
    checking_dict = CheckingAccount.to_dict_account(CheckingAccount(**common))
    balance_result = T1.change_balance()
    checking_dict["balance"] = balance_result[0] 
    T1.account_info = {k: v for k, v in checking_dict.items() if k != "transactions"}
    checking_dict["transactions"].append(transaction_dict)
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
    accountsTO=FileManager("files/accounts.json", {"accounts": [checking_dict_TO]})
    transactionsTO=FileManager("files/transactions.json", {"transactions": [transactionTO_dict]})
    files_list = [customer, accounts,transactions,accountsTO,transactionsTO]
    


  
    for file in files_list:
     file.ensure_file_exists()  

    customer.save_data()
    accounts.save_data()
    transactions.save_data()
    accountsTO.delete_data()
    accountsTO.save_data()
    transactionsTO.save_data()









else:
    T1.cheack_status_transaction()
    transaction_dict = T1.to_dict_transaction()

    print(f"Account Balance: {T1.account_info['balance']}")
    checking_dict = CheckingAccount.to_dict_account(CheckingAccount(**common))
    balance_result = T1.change_balance()
    checking_dict["balance"] = balance_result[0] 
    T1.account_info = {k: v for k, v in checking_dict.items() if k != "transactions"}
    checking_dict["transactions"].append(transaction_dict)


    #----------
    #FileManager
    #--------- 
    customer = FileManager("files/customers.json", {"customers": [dict_customer]})
    accounts = FileManager("files/accounts.json", {"accounts": [checking_dict]})
    transactions = FileManager("files/transactions.json", {"transactions": [transaction_dict]})

    files_list = [customer, accounts,transactions]
    for file in files_list:
        file.ensure_file_exists()  

    customer.save_data()
    accounts.save_data()
    transactions.save_data()





#----------
#FileManager
#--------- 
BANK_MONEY(T1.fee,T1.transactionType)