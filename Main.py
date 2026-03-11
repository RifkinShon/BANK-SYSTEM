
from core.transaction import Transaction,TransactionTo,TransactionUtils
from core.customer import Customer,CustomerUtils
from core.account import AccountUtils, CheckingAccount, LoanAccount, SavingsAccount
from core.BANK import BANK
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
    data=CustomerUtils.login("356822024",1235643223)
    customer = Customer.from_dict(data) 
    dict_customer_login=customer.to_dict_customer()
    customer_login = FileManager("files/customers.json", {"customers": [dict_customer_login]})
    customer_login.delete_data()




else:
    customer = Customer(
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
    )
    
dict_customer=customer.to_dict_customer()

    


 #----------
#Account
#---------   
if  login_or_create:
    loged_accounts_data=AccountUtils.search_accounts("356822024")
    checking_dict = loged_accounts_data["CHECKING"]
    checking_dict["account_type"] = "CHECKING"

    saving_dict = loged_accounts_data["SAVINGS"]
    saving_dict["account_type"] = "SAVINGS"

    loan_dict = loged_accounts_data["LOAN"]
    loan_dict["account_type"] = "LOAN"

    checking_dict_deletion=checking_dict
    saving_dict_deletion=saving_dict
    loan_dict_deletion=loan_dict


    



    checkingAccount=CheckingAccount.from_dict_checking(checking_dict)
    savingsAccount=SavingsAccount.from_dict_savings(saving_dict)
    loanAccount=LoanAccount.from_dict_loan(loan_dict)

    checking = FileManager("files/accounts.json", {"accounts": [checking_dict_deletion]})
    saving = FileManager("files/accounts.json", {"accounts": [saving_dict_deletion]})
    loan = FileManager("files/accounts.json", {"accounts": [loan_dict_deletion]})
    




    
else:
    common = {
            "account_number": dict_customer["account_number"],
            "ownerId": dict_customer["customer_id"],
            "account_holder": dict_customer["name"],
            "status": "ACTIVE",
            "daily_withdrawal_limit": dict_customer["credit_score"] * 12.57,
            "transactions": [],
            "credit_score": dict_customer["credit_score"],
            "created_time": dict_customer["created_time"],
            "updata_time": dict_customer["created_time"] 
        }
        
        


    checkingAccount = CheckingAccount(**common,
        balance=AccountUtils.balance("CHECKING")
    )

    savingsAccount = SavingsAccount(**{**common, "transactions": []},  # ← רשימה חדשה
        balance=AccountUtils.balance("SAVINGS")
    )

    loanAccount = LoanAccount(**{**common, "transactions": []},        # ← רשימה חדשה
        balance=AccountUtils.balance("LOAN")
    )

    checking_dict=checkingAccount.to_dict_account()
    saving_dict=savingsAccount.to_dict_account()
    loan_dict=loanAccount.to_dict_account()
#מקשר בין המילוןים
accounts_link=[checking_dict,saving_dict,loan_dict]
#-------------------------------
#-------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#להוסיף בui שאם יש raise זה מחזיר חשבנות מחוקים
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
        account_number_To=TransactionUtils.account_number_To("356822024-S")
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
    checking_dict = checkingAccount.to_dict_account()
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

    
    #----------
    #FileManager
    #--------- 

    checking.delete_data()
    saving.delete_data()
    loan.delete_data()


    customer = FileManager("files/customers.json", {"customers": [dict_customer]})

    account_checking = FileManager("files/accounts.json", {"accounts": [checking_dict]})
    account_saving = FileManager("files/accounts.json", {"accounts": [saving_dict]})
    account_loan = FileManager("files/accounts.json", {"accounts": [loan_dict]})


    transactions = FileManager("files/transactions.json", {"transactions": [transaction_dict]})
    accountsTO=FileManager("files/accounts.json", {"accounts": [checking_dict_TO]})
    transactionsTO=FileManager("files/transactions.json", {"transactions": [transactionTO_dict]})
    files_list = [customer,account_checking ,account_saving,account_loan,transactions,accountsTO,transactionsTO]
    


  
    for file in files_list:
     file.ensure_file_exists()  

    customer.save_data()
    account_checking.save_data()
    if saving_dict["account_number"] != checking_dict_TO["account_number"]:
        account_saving.save_data()
    if loan_dict["account_number"] != checking_dict_TO["account_number"]:
        account_loan.save_data()
    transactions.save_data()
    accountsTO.delete_data()
    accountsTO.save_data()
    transactionsTO.save_data()









else:
    T1.cheack_status_transaction()
    transaction_dict = T1.to_dict_transaction()

    print(f"Account Balance: {T1.account_info['balance']}")
    checking_dict = checkingAccount.to_dict_account()
    balance_result = T1.change_balance()
    checking_dict["balance"] = balance_result[0] 
    T1.account_info = {k: v for k, v in checking_dict.items() if k != "transactions"}
    checking_dict["transactions"].append(transaction_dict)


    #----------
    #FileManager
    #--------- 

    customer = FileManager("files/customers.json", {"customers": [dict_customer]})

    account_checking = FileManager("files/accounts.json", {"accounts": [checking_dict]})
    account_saving = FileManager("files/accounts.json", {"accounts": [saving_dict]})
    account_loan = FileManager("files/accounts.json", {"accounts": [loan_dict]})

    transactions = FileManager("files/transactions.json", {"transactions": [transaction_dict]})

    files_list = [customer, account_checking,transactions]
    for file in files_list:
        file.ensure_file_exists()  

    customer.save_data()
    account_checking.save_data()
    account_saving.save_data()
    account_loan.save_data()

    transactions.save_data()





#----------
#FileManager
#--------- 
BANK.BANK_MONEY(T1.fee,T1.transactionType)