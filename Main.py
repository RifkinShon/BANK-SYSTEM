import random
from core.transaction import Transaction,TransactionUtils
from core.customer import Customer, CustomerRole,Customer_AccountTYPE,CustomerUtils
from core.account import Account, AccountStatus, AccountTYPE,AccountUtils
from utils.file_manager import FileManager 

Customer1 = Customer(
    customer_id=CustomerUtils.id_number("123456789"),
    name=CustomerUtils.name("John Doe"),
    email=CustomerUtils.email("johndoe@gmail.com"),
    phone=CustomerUtils.phone("0501234567"),
    account_number="1234567890",
    address=CustomerUtils.address("123 Main St, City, Country"),
    password=CustomerUtils.password("1235643223"),
    role=CustomerUtils.customerRole(CustomerRole.CLIENT),
    credit_score=CustomerUtils.credit_score(),
    created_time=CustomerUtils.created_time(),
    account_type=AccountTYPE.CHECKING
)
dict_customer=Customer1.to_dict_customer()


A1 = Account(
    account_number=dict_customer["account_number"],
    ownerId=dict_customer["customer_id"],
    account_holder=dict_customer["name"],
    account_type=dict_customer["account_type"],
    balance=AccountUtils.balance(dict_customer["account_type"]),
    status=AccountStatus.ACTIVE,
    daily_withdrawal_limit=dict_customer["credit_score"]*12.57,
    transactions=[],
    credit_score=dict_customer["credit_score"]
)
