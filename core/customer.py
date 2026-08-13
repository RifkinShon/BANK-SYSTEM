class CustomerUtils:
    @staticmethod
    def name(name):
            if name:
                print("name is valid.")
                return name
            raise ValueError("Name cannot be empty.")
    @staticmethod
    def account_number():
        import random
        account_number="356"+str(random.randint(100,999999))
        account_number=str(account_number)
        return account_number
        
    @staticmethod
    def age(age):
        if not isinstance(age, int):
            raise ValueError("Age must be an integer.")
        if 0 < age < 120:
            print("Age is valid.")
            return age
        raise ValueError("Please enter a valid age between 1 and 119.")
    @staticmethod
    def email(email):
        if email.endswith("@gmail.com") and len(email) >= 11:
            print("email is valid.")
            return email
        raise ValueError("Email must end with '@gmail.com' and be valid.")
    @staticmethod
    def phone(phone):
        if phone.startswith("05") and len(phone) == 10 and phone.isdigit():
            print("phone is valid.")
            return phone
        raise ValueError("Phone number must start with 05 and contain exactly 10 digits.")
    @staticmethod
    def id_number(id_number):

        if len(id_number) == 9 and id_number.isdigit():
            print("id_number is valid.")
            return id_number
        raise ValueError("ID number must contain exactly 9 digits.")
    @staticmethod
    def credit_score():
        import random
        return random.randint(300, 850)
    @staticmethod
    def address(address):        
            if address:
                print("address is valid.")
                return address
            raise ValueError("address cannot be empty.")
    @staticmethod
    def customerRole(customerRole):

        if customerRole in ("CLIENT", "ADMIN"):
            print("customerRole is valid.")
            return customerRole
        raise ValueError("Invalid Customer Role") 
    @staticmethod
    def password(password):
        if password:
                print("password is valid.")
                return password
        raise ValueError("password cannot be empty.")

    @staticmethod
    def created_time():
        from datetime import datetime
        now = datetime.now()
        return now.strftime("%Y-%m-%d ")
    @staticmethod
    def account_type(account_type):
        if account_type in ("CHECKING", "SAVINGS", "LOAN"):
            print("account_type is valid.")
            return account_type
        raise ValueError("Invalid Account Type")
    @staticmethod
    def login(account_number,password):
        import os
        import sys
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from utils.file_manager import FileManager 
        data = FileManager("files/customers.json", {"customers": []}).load_data()
        for customer in data["customers"]:
            if customer["account_number"] == str(account_number):
                print("customers account is correct")
                if str(customer["password"]) == str(password):
                    print("customers password is correct")
                    print("Login successful.")
                    return  customer
        raise ValueError("account number or password not correct")

    @staticmethod
    def login_GUI(account_number,password):
        import os
        import sys
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from utils.file_manager import FileManager 
        data = FileManager("files/customers.json", {"customers": []}).load_data()
        for customer in data["customers"]:
            if customer["account_number"] == str(account_number):
                print("customers account is correct")
                if str(customer["password"]) == str(password):
                    print("customers password is correct")
                    print("Login successful.")
                    return  account_number,password
        raise ValueError("account number or password not correct")


        


class Customer:
    
    def __init__(self, customer_id, name,age, email, phone, account_number,created_time, address,password, role,credit_score):
        self.customer_id = customer_id
        self.name = name
        self.age=age
        self.email = email
        self.phone = phone
        self.account_number = account_number
        self.created_time = created_time
        self.address = address
        self.role = role
        self.credit_score=credit_score
        self.password=password




    def to_dict_customer(self):
        print("Converting Customer object to dictionary.")
        return {
            "customer_id": self.customer_id,
            "account_number": self.account_number,
            "password":self.password,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "role": self.role,
            "credit_score": self.credit_score,
            "created_time": self.created_time,
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            customer_id=data["customer_id"],
            name=data["name"],
            age=data["age"],
            email=data["email"],
            phone=data["phone"],
            account_number=data["account_number"],
            created_time=data["created_time"],
            address=data["address"],
            role=data["role"],
            credit_score=data["credit_score"],
            password=data["password"]
        )
    
