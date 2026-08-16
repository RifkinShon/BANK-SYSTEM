
from core.transaction import Transaction,TransactionTo,TransactionUtils
from core.customer import Customer,CustomerUtils
from core.account import AccountUtils, CheckingAccount, LoanAccount, SavingsAccount
from core.BANK import BANK
from utils.file_manager import FileManager 

def login_or_create(RS):
     print(RS)
     return RS
    
def transaction_type(SR):
    #True is TRANSPER
    if SR == True or SR == False:
     return SR





#----------
#Customer
#---------
def Customer_login(account_number,password):
    data=CustomerUtils.login(account_number,password)
    customer = Customer.from_dict(data) 
    dict_customer_login=customer.to_dict_customer()
    customer_login = FileManager("files/customers.json", {"customers": [dict_customer_login]})
    customer_login.delete_data()




def Customer_create(id_number,name,age,email,phone,address,password):
    customer = Customer(
        customer_id=CustomerUtils.id_number(id_number),
        name=CustomerUtils.name(name),
        age=CustomerUtils.age(age),
        email=CustomerUtils.email(email),
        phone=CustomerUtils.phone(phone),
        account_number=CustomerUtils.account_number(),
        address=CustomerUtils.address(address),
        password=CustomerUtils.password(password),
        role=CustomerUtils.customerRole("CLIENT"),
        credit_score=CustomerUtils.credit_score(),
        created_time=CustomerUtils.created_time(),
    )

    return customer.to_dict_customer()




 #----------
#Account
#---------   
def login_account(account_number):
    loged_accounts_data=AccountUtils.search_accounts(account_number)
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
    return checking_dict,saving_dict,loan_dict
    




    
def create_account(dict_customer):
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
    return checking_dict,saving_dict,loan_dict


#מקשר בין המילוןים
def accounts_for_transaction(checking_dict,saving_dict,loan_dict):
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




def transaction(common_transaction,checkingAccount,checking_dict,dict_customer,saving_dict,loan_dict,checking,saving,loan):
    T1 = Transaction(
        **common_transaction,
        transactionType=TransactionUtils.transactionType("WITHDRAWAL")
    )



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
    if  login_or_create:
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









def transaction_TO(common_transaction,account_number_To,Account,checking_dict,dict_customer,saving_dict,loan_dict):
    account_number_To=str(account_number_To)
    T1 = TransactionTo(
        **common_transaction,
        transactionType=TransactionUtils.transactionType("TRANSFER"),
        account_number_To=TransactionUtils.account_number_To(account_number_To)
    )   
    T1.cheack_status_transaction()
    transaction_dict = T1.to_dict_transaction()

    print(f"Account Balance: {T1.account_info['balance']}")
    Account = Account.to_dict_account()
    balance_result = T1.change_balance()
    Account["balance"] = balance_result[0] 
    T1.account_info = {k: v for k, v in Account.items() if k != "transactions"}
    Account["transactions"].append(transaction_dict)


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
#BANK_MONEY
#--------- 
"""def BANK_MONEY(T1.fee,T1.transactionType):
 BANK.BANK_MONEY(T1.fee,T1.transactionType)"""