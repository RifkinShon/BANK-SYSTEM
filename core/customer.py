from enum import Enum
class CustomerUtils:
    @staticmethod
    def name(name):
            if name:
                return name
            raise ValueError("Name cannot be empty.")
    @staticmethod
    def acount_number():
        import random
        account_number="356"+str(random.randint(100,999999))
        return account_number
        
    @staticmethod
    def age(age):
        if not isinstance(age, int):
            raise ValueError("Age must be an integer.")
        if 0 < age < 120:
            return age
        raise ValueError("Please enter a valid age between 1 and 119.")
    @staticmethod
    def email(email):
        if email.endswith("@gmail.com") and len(email) >= 11:
            return email
        raise ValueError("Email must end with '@gmail.com' and be valid.")
    @staticmethod
    def phone(phone):
        if phone.startswith("05") and len(phone) == 10 and phone.isdigit():
            return phone
        raise ValueError("Phone number must start with 05 and contain exactly 10 digits.")
    @staticmethod
    def id_number(id_number):

        if len(id_number) == 9 and id_number.isdigit():
            return id_number
        raise ValueError("ID number must contain exactly 9 digits.")
    @staticmethod
    def credit_score():
        import random
        return random.randint(300, 850)
    @staticmethod
    def address(address):
            
            if address:
                return address
            raise ValueError("address cannot be empty.")
    @staticmethod
    def customerRole(customerRole):

        if customerRole in CustomerRole:
            return CustomerRole
        raise ValueError("Invalid Customer Role") 
    @staticmethod
    def password(password):
        if password:
                return password
        raise ValueError("password cannot be empty.")
    @staticmethod
    def cheack_login(self, account_number, password):
        if self.account_number == account_number and self.password == password:
            return True
        return False
    @staticmethod
    def created_time():
     from transaction import time_now_update
     return time_now_update()
    @staticmethod
    def account_type(account_type):
        if account_type in Customer_AccountTYPE:
            return Customer_AccountTYPE
        raise ValueError("Invalid Account Type")
#להוסיף שזה יבדוק עם יש מילון בל סיסמה כזה ומספר חשבון
class Customer_AccountTYPE(Enum):
  CHECKING = 1
  SAVINGS = 2
  CREDIT = 3

class CustomerRole(Enum):
    CLIENT = 1
    ADMIN = 2

class Customer:
    
    def __init__(self, customer_id, name, email, phone, account_number,created_time,account_type, address,password, role,credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.account_number = account_number
        self.created_time = created_time
        self.account_type=account_type
        self.address = address
        self.role = role
        self.credit_score=credit_score
        self.password=password




    def to_dict_customer(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "account_number": self.account_number,
            "address": self.address,
            "role": self.role,
            "credit_score": self.credit_score,
            "created_time": self.created_time,
            "account_type": self.account_type,
        }
Customer1 = Customer(
    customer_id=CustomerUtils.id_number("123456789"),
    name=CustomerUtils.name("John Doe"),
    email=CustomerUtils.email("johndoe@gmail.com"),
    phone=CustomerUtils.phone("0501234567"),
    account_number=CustomerUtils.account_number(),
    address=CustomerUtils.address("123 Main St, City, Country"),
    password=CustomerUtils.password("1235643223"),
    role=CustomerUtils.customerRole(CustomerRole.CLIENT),
    credit_score=CustomerUtils.credit_score(),
    created_time=CustomerUtils.created_time(),
    account_type=CustomerUtils.account_type()
)