from customtkinter import *
from tkinter import messagebox
from Main_GUI import *
answers_list = []
valid_account_number=None
dict_customer =None
def login_signup():
    selected_option = combo_box.get()
    frame.pack_forget()  # Hide frame 1
    answers_list.append(selected_option)
    login_or_create(selected_option)
    if selected_option == "login":
        print("Login selected")

        frame2.pack(expand=True, fill=BOTH, padx=20, pady=20)  # Show frame 2
    elif selected_option == "sign up":
        print("Sign up selected")
        frame3.pack(expand=True, fill=BOTH, padx=20, pady=20)  # Show frame 3

def Go_back(frame_num):
    print("Go back")
    if frame_num ==2:
     frame2.pack_forget()
     frame.pack(expand=True, fill=BOTH, padx=20, pady=20)
    elif frame_num ==3:
        frame3.pack_forget()
        frame.pack(expand=True, fill=BOTH, padx=20, pady=20)




def login_info():
    try:
        rew_account_number = login_acc_entry.get()
        rew_password = login_pass_entry.get()
        global valid_account_number
        valid_account_number, valid_password = CustomerUtils.login_GUI(rew_account_number, rew_password)
        dict_customer_login = Customer_login(valid_account_number, valid_password)
        messagebox.showinfo("Success", "Login successful")
        frame2.pack_forget()
        tabview_def(TRUE,dict_customer_login,FALSE)


    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
   
    


def sign_up_info():
    try:
        # 1. קריאת הנתונים מהשדות ב-GUI
        raw_id = signup_entries["id_number"].get()
        raw_name = signup_entries["name"].get()
        raw_age = signup_entries["age"].get()
        raw_email = signup_entries["email"].get()
        raw_phone = signup_entries["phone_number"].get()
        raw_address = signup_entries["address"].get()
        raw_password = signup_entries["password"].get()

        # בדיקה מקומית קטנה להמרת גיל למספר
        if not raw_age.isdigit():
            raise ValueError("Age must be a valid number.")
        parsed_age = int(raw_age)

        # 2. הלתקף (Validation) בעזרת המחלקה שלך!
        # אם שדה מסוים לא תקין, ה-CustomerUtils יבצע raise מיד!
        valid_id = CustomerUtils.id_number(raw_id)
        valid_name = CustomerUtils.name(raw_name)
        valid_age = CustomerUtils.age(parsed_age)
        valid_email = CustomerUtils.email(raw_email)
        valid_phone = CustomerUtils.phone(raw_phone)
        valid_address = CustomerUtils.address(raw_address)
        valid_password = CustomerUtils.password(raw_password)

        # 3. אם הגענו לכאן - כל הנתונים תקינים! שולחים ליצירת הלקוח
        global dict_customer
        dict_customer_sign_up=dict_customer = Customer_create(
            valid_id, valid_name, valid_age, 
            valid_email, valid_phone, valid_address, valid_password
        )

        # 4. הודעת הצלחה
        messagebox.showinfo("Success", "Account created successfully!")
        frame3.pack_forget() 
        tabview_def(FALSE,dict_customer_sign_up,FALSE)    


    except ValueError as e:
        # 5. ה-except תופס את ה-raise הראשון שנזרק מ-CustomerUtils!
        # המשתנה e מכיל את ההודעה המדויקת שהגדרת ב-CustomerUtils
        messagebox.showerror("Input Error", str(e))



def login_or_create_account(TRUE_or_FALSE):
    if TRUE_or_FALSE:
        checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File,checkingAccount,savingsAccount,loanAccount = login_account(valid_account_number)
        return checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File,checkingAccount,savingsAccount,loanAccount
    else:
        checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File,checkingAccount,savingsAccount,loanAccount = create_account(dict_customer)
        return checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File,checkingAccount,savingsAccount,loanAccount


def DEPOSIT( dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount, amount):
   try:
    common_transaction = accounts_for_transaction(checking_dict, saving_dict, loan_dict, amount,"DEPOSIT")
    transaction(common_transaction, dict_customer, checking_dict, saving_dict, loan_dict, checking_File, saving_File, loan_File,checkingAccount,savingsAccount,loanAccount,"DEPOSIT")
    messagebox.showinfo("Success", "deposit got send !")
    tabview_def(True,dict_customer,True)
   except ValueError as e:
        messagebox.showerror("Input Error", str(e))
   
    


def WITHDRAWAL( dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount, amount):
    try:
        common_transaction = accounts_for_transaction(checking_dict, saving_dict, loan_dict, amount,"WITHDRAWAL")
        transaction(common_transaction, dict_customer, checking_dict, saving_dict, loan_dict, checking_File, saving_File, loan_File,checkingAccount,savingsAccount,loanAccount,"WITHDRAWAL")
        messagebox.showinfo("Success", "withdrawal got send !")
        tabview_def(True,dict_customer,True)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
   


def TRANSFER (dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount, amount,account_number_To):
    try:
        common_transaction = accounts_for_transaction(checking_dict, saving_dict, loan_dict, amount,"Transfer")
        transaction_TO(common_transaction, dict_customer, checking_dict, saving_dict, loan_dict, checking_File, saving_File, loan_File,checkingAccount,savingsAccount,loanAccount,account_number_To)
        messagebox.showinfo("Success", "transfer got send !")
        tabview_def(True,dict_customer,True)   
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
   

def LOAN_SAVING_DEPOSIT_WITHDRAWAL(dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount, amount,account_number_To,transactionType):
    try:
        common_transaction = accounts_for_transaction(checking_dict, saving_dict, loan_dict, amount,transactionType)
        transaction_TO(common_transaction, dict_customer, checking_dict, saving_dict, loan_dict, checking_File, saving_File, loan_File,checkingAccount,savingsAccount,loanAccount,account_number_To)
        messagebox.showinfo("Success", "withdrawal/deposit got send !")
        tabview_def(True,dict_customer,True)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
   
 


app = CTk()
app.geometry("800x550")  # Expanded height slightly to accommodate the sign-up inputs nicely
set_appearance_mode("dark")

# ========== Frame 1 ==========
frame = CTkFrame(master=app, width=400, height=300, corner_radius=10)
frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

label = CTkLabel(master=frame, text="Hello, World!", font=("Arial", 24))
label.place(relx=0.5, rely=0.3, anchor=CENTER)

combo_box = CTkComboBox(
    master=frame, 
    values=["login", "sign up"], 
    width=200, 
    height=30, 
    corner_radius=5, 
    state="readonly"
)
combo_box.place(relx=0.5, rely=0.5, anchor=CENTER)

btn = CTkButton(
    master=frame, 
    text="Click Me", 
    corner_radius=10, 
    fg_color="transparent", 
    hover_color="green", 
    text_color="white",
    border_color="gray", 
    border_width=2, 
    font=("Arial", 16, "bold"), 
    command=login_signup)

btn.place(relx=0.5, rely=0.7, anchor=CENTER)











# ========== Frame 2 (login) ==========
frame2 = CTkFrame(master=app, width=400, height=300, corner_radius=10)
label2 = CTkLabel(master=frame2, text="Login", font=("Arial", 24))
label2.place(relx=0.5, rely=0.25, anchor=CENTER)

login_acc_entry = CTkEntry(master=frame2, placeholder_text="Enter account_number", width=200, height=30, corner_radius=5)
login_acc_entry.place(relx=0.5, rely=0.45, anchor=CENTER)

login_pass_entry = CTkEntry(master=frame2, placeholder_text="Enter password", show="*", width=200, height=30, corner_radius=5)
login_pass_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

btn = CTkButton(
    master=frame2, 
    text="Click Me", 
    corner_radius=10, 
    fg_color="transparent", 
    hover_color="green", 
    text_color="white",
    border_color="gray", 
    border_width=2, 
    font=("Arial", 16, "bold"), 
    command=login_info
)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)

btn = CTkButton(
    master=frame2, 
    text="Go back", 
    corner_radius=10, 
    fg_color="transparent", 
    hover_color="green", 
    text_color="white",
    border_color="gray", 
    border_width=2, 
    font=("Arial", 16, "bold"), 
    command= lambda : Go_back(2)
)
btn.place(relx=0.5, rely=0.8, anchor=CENTER)










# ========== Frame 3 (sign up) ==========
frame3 = CTkFrame(master=app, width=400, height=450, corner_radius=10)
label3 = CTkLabel(master=frame3, text="Sign Up", font=("Arial", 24))
label3.place(relx=0.5, rely=0.08, anchor=CENTER)

entry_fields = ["id_number", "name", "age", "email", "phone_number", "address", "password"]
signup_entries = {}

for i, field_name in enumerate(entry_fields):
    # הגדרת שדה הסיסמה כסתור (show="*")
    show_char = "*" if field_name == "password" else ""
    
    entry = CTkEntry(
        master=frame3, 
        placeholder_text=f"Enter {field_name}", 
        width=200, 
        height=30, 
        corner_radius=5,
        show=show_char
    )
    entry.place(relx=0.5, rely=0.18 + (i * 0.09), anchor=CENTER)
    
    # *** התיקון המרכזי: שמירת שדה הקלט במילון ***
    signup_entries[field_name] = entry

# הכפתור מחוץ ללולאה (נוצר רק פעם אחת)
btn_signup = CTkButton(
    master=frame3, 
    text="Sign Up", 
    corner_radius=10, 
    fg_color="transparent", 
    hover_color="green", 
    text_color="white",
    border_color="gray", 
    border_width=2, 
    font=("Arial", 16, "bold"),
    command=sign_up_info 
)
btn_signup.place(relx=0.5, rely=0.8, anchor=CENTER)


btn = CTkButton(
    master=frame3, 
    text="Go back", 
    corner_radius=10, 
    fg_color="transparent", 
    hover_color="green", 
    text_color="white",
    border_color="gray", 
    border_width=2, 
    font=("Arial", 16, "bold"), 
    command= lambda : Go_back(3)
)
btn.place(relx=0.5, rely=0.88, anchor=CENTER)





# נניח ש-tabview מוגדר כמשתנה גלובלי או ששומרים אותו נכון
def tabview_def(TRUE_or_FALSE, dict_customer, refreash):
    global tabview # אם הוא משתנה גלובלי
    
    if refreash:
        try:
            tabview.destroy() # מוחק את הישן מהזיכרון
        except NameError:
            pass # אם הוא עוד לא היה קיים מעולם, לא עושים כלום

    tabview = CTkTabview(master=app, width=400, height=300)
    tabview.pack(expand=True, fill="both", padx=20, pady=20)
    if (TRUE_or_FALSE):
        checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File,checkingAccount,savingsAccount,loanAccount = login_or_create_account(TRUE_or_FALSE)
    elif(TRUE_or_FALSE==FALSE):
        checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File,checkingAccount,savingsAccount,loanAccount = login_or_create_account(TRUE_or_FALSE)


    else:
        raise("tabview_def raise ")
    tabview.add("Tab 1")
    label_tab1 = CTkLabel(master=tabview.tab("Tab 1"), text=f"welcome to your account {checking_dict['account_holder']} & {dict_customer['account_number']}", font=("Arial", 24))
    label_tab1.place(relx=0.5, rely=0.25, anchor=CENTER)

    label_tab2 = CTkLabel(
        master=tabview.tab("Tab 1"), 
        text=f" Status: {checking_dict['status']} | Credit Score: {checking_dict['credit_score']} | Daily Limit: ${checking_dict.get('daily_withdrawal_limit', 0):.2f}", 
        font=("Arial", 20)  # אפשר להקטין קצת ל-20 כדי שלא יחרוג מהמסך
    )
    label_tab2.place(relx=0.5, rely=0.4, anchor=CENTER)

    label_tab3 = CTkLabel(master=tabview.tab("Tab 1"), text=f"Balance: ${checking_dict['balance']:.2f}", font=("Arial", 24))
    label_tab3.place(relx=0.5, rely=0.6, anchor=CENTER)


    # 1. הוספת Tab 2
    tab2 = tabview.add("Tab 2")

    # 2. יצירת פריים נגלל בתוך Tab 2
    scrollable_frame2 = CTkScrollableFrame(master=tabview.tab("Tab 2"))
    scrollable_frame2.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # 3. כותרת בתוך הפריים הנגלל
    label_tab2 = CTkLabel(master=scrollable_frame2, text="All Transactions", font=("Arial", 22, "bold"))
    label_tab2.pack(pady=15)

    # 4. הוספת תוכן רב כדי שיהיה אפשר לגלול למטה
    for transaction in checking_dict['transactions']:
        trans_label = CTkLabel(
            master=scrollable_frame2, 
            text=f"{transaction['timestamp']}: {transaction['transactionType']} ${transaction['amount']:.2f} | Fee: ${transaction['fee']:.2f} | {transaction['status']}", 
            font=("Arial", 14)
        )
        trans_label.pack(pady=8, anchor="w", padx=15)









    tab3 = tabview.add("Tab 3")
    scrollable_frame3 = CTkScrollableFrame(master=tabview.tab("Tab 3"))
    scrollable_frame3.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def handle_close_saving():
     try:
        from utils.file_manager import FileManager
        account_number = saving_dict['account_number']
        edit_dict = FileManager("files/accounts.json", {"edit": [{"account_number": account_number, "attribute": "status", "value": "CLOSED"}]})
        edit_dict.edit_data()
        messagebox.showinfo("Success", "SAVING CLOSED")
        tabview_def(True,dict_customer,True)
     except ValueError as e:
        messagebox.showerror("Input Error", str(e))

    # כותרת בתוך הפריים הנגלל
    label_tab3 = CTkLabel(master=scrollable_frame3, text="savings Account", font=("Arial", 22, "bold"))
    label_tab3.pack(pady=15)

    label_tab3_2 = CTkLabel(
        master=scrollable_frame3, 
        text=f"SAVING Balance: ${saving_dict['balance']} | Status: {saving_dict['status']}", 
        font=("Arial", 20)
    )
    label_tab3_2.pack(pady=20)


    Money_Saving_entry = CTkEntry(master=scrollable_frame3, placeholder_text="Enter number to Withdraw or Deposit", width=200, height=30, corner_radius=5)
    Money_Saving_entry.pack(pady=25)

    # Frame לכפתורים
    btn_frame3 = CTkFrame(master=scrollable_frame3, fg_color="transparent")
    btn_frame3.pack(pady=25)

    btn_withdraw_savings = CTkButton(
        master=btn_frame3, 
        text="Withdraw from savings", 
        corner_radius=10, 
        fg_color="transparent", 
        hover_color="green", 
        text_color="white",
        border_color="gray", 
        border_width=2, 
        font=("Arial", 16, "bold"),
        command=lambda: LOAN_SAVING_DEPOSIT_WITHDRAWAL(dict_customer,saving_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount,Money_Saving_entry.get(),checking_dict['account_number'],"WITHDRAWAL")  
    )

    btn_withdraw_savings.pack(side="left", padx=10)

    btn_deposit_savings = CTkButton(
        master=btn_frame3, 
        text="Deposit to savings", 
        corner_radius=10, 
        fg_color="transparent", 
        hover_color="green", 
        text_color="white",
        border_color="gray", 
        border_width=2, 
        font=("Arial", 16, "bold"),
        command=lambda: LOAN_SAVING_DEPOSIT_WITHDRAWAL(dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount,Money_Saving_entry.get(),saving_dict['account_number'],"DEPOSIT")  
    )
    btn_deposit_savings.pack(side="left", padx=10)



    btn_CLOSED = CTkButton(
        master=btn_frame3, 
        text="Close Savings Account", 
        corner_radius=10, 
        fg_color="transparent", 
        hover_color="red", 
        text_color="white",
        border_color="red", 
        border_width=2, 
        font=("Arial", 16, "bold"),
        command=lambda: handle_close_saving()
    )
    btn_CLOSED.pack(side="left", padx=10)


    # הוספת תוכן רב כדי שיהיה אפשר לגלול למטה
    try:
        for transaction in saving_dict['transactions']:
            trans_label = CTkLabel(
                master=scrollable_frame3, 
                text=f"{transaction['timestamp']}: {transaction['transactionType']} ${transaction['amount']:.2f} | Fee: ${transaction['fee']:.2f} | {transaction['status']}", 
                font=("Arial", 14)
            )
            trans_label.pack(pady=10, anchor="w", padx=15)
    except :
        pass



    tab4 = tabview.add("Tab 4")
    scrollable_frame4 = CTkScrollableFrame(master=tabview.tab("Tab 4"))
    scrollable_frame4.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # כותרת בתוך הפריים הנגלל
    label_tab4 = CTkLabel(master=scrollable_frame4, text="Loan Account", font=("Arial", 22, "bold"))
    label_tab4.pack(pady=15)


    label_tab4_2 = CTkLabel(
        master=scrollable_frame4, 
        text=f"LOAN Balance: ${loan_dict['balance']} | Status: {loan_dict['status']}", 
        font=("Arial", 20)
    )
    label_tab4_2.pack(pady=20)


    Money_Loan_entry = CTkEntry(master=scrollable_frame4, placeholder_text="Enter number to Withdraw or Deposit", width=200, height=30, corner_radius=5)
    Money_Loan_entry.pack(pady=20)

    btn_deposit_loan = CTkButton(
        master=scrollable_frame4, 
        text="Deposit to loan", 
        corner_radius=10, 
        fg_color="transparent", 
        hover_color="green", 
        text_color="white",
        border_color="gray", 
        border_width=2, 
        font=("Arial", 16, "bold"),
        command=lambda: LOAN_SAVING_DEPOSIT_WITHDRAWAL(dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount,Money_Loan_entry.get(),loan_dict['account_number'],"DEPOSIT") 
    )
    btn_deposit_loan.pack(pady=15)

    # הוספת תוכן רב כדי שיהיה אפשר לגלול למטה
    try:
        for transaction in loan_dict['transactions']:
            trans_label = CTkLabel(
                master=scrollable_frame4, 
                text=f"{transaction['timestamp']}: {transaction['transactionType']} ${transaction['amount']:.2f} | Fee: ${transaction['fee']:.2f} | {transaction['status']}", 
                font=("Arial", 14)
            )
            trans_label.pack(pady=8, anchor="w", padx=15)
    except :
        pass
    tab5 = tabview.add("Tab 5")

    # כותרות בחלק העליון
    label_tab1 = CTkLabel(master=tab5, text="TRANSACTIONS", font=("Arial", 24, "bold"))
    label_tab1.place(relx=0.5, rely=0.08, anchor=CENTER)

    label_tab2 = CTkLabel(master=tab5, text="WITHDRAWALS • DEPOSITS • TRANSFERS", font=("Arial", 14))
    label_tab2.place(relx=0.5, rely=0.16, anchor=CENTER)

    # ==================== שורה ראשונה: Entry Fields ===================
    Withdraw_entry = CTkEntry(master=tab5, placeholder_text="Enter amount to Withdraw", width=200, height=35, corner_radius=5)
    Withdraw_entry.place(relx=0.15, rely=0.32, anchor=CENTER)

    Deposit_entry = CTkEntry(master=tab5, placeholder_text="Enter amount to Deposit", width=200, height=35, corner_radius=5)
    Deposit_entry.place(relx=0.5, rely=0.32, anchor=CENTER)

    Transfer_entry = CTkEntry(master=tab5, placeholder_text="Enter amount to Transfer", width=200, height=35, corner_radius=5)
    Transfer_entry.place(relx=0.85, rely=0.32, anchor=CENTER)

    Transfer_account_number_entry = CTkEntry(master=tab5, placeholder_text="Enter account number to Transfer", width=200, height=35, corner_radius=5)
    Transfer_account_number_entry.place(relx=0.85, rely=0.42, anchor=CENTER)





    # ==================== שורה שנייה: Buttons ===================
    btn_Withdraw = CTkButton(
        master=tab5, 
        text="Withdraw", 
        corner_radius=10, 
        fg_color="transparent", 
        hover_color="green", 
        text_color="white",
        border_color="gray", 
        border_width=2, 
        font=("Arial", 14, "bold"),
        command=lambda: WITHDRAWAL( dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount,Withdraw_entry.get())
    )
    btn_Withdraw.place(relx=0.15, rely=0.60, anchor=CENTER)
    
    btn_Deposit = CTkButton(
        master=tab5, 
        text="Deposit", 
        corner_radius=10, 
        fg_color="transparent", 
        hover_color="green", 
        text_color="white",
        border_color="gray", 
        border_width=2, 
        font=("Arial", 14, "bold"),
            command=lambda: DEPOSIT(dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount,Deposit_entry.get())
        )
    btn_Deposit.place(relx=0.5, rely=0.60, anchor=CENTER)

    btn_Transfer = CTkButton(
        master=tab5, 
        text="Transfer", 
        corner_radius=10, 
        fg_color="transparent", 
        hover_color="green", 
        text_color="white",
        border_color="gray", 
        border_width=2, 
        font=("Arial", 14, "bold"),
            command=lambda: TRANSFER(dict_customer,checking_dict,saving_dict,loan_dict,checking_File,saving_File,loan_File, checkingAccount,savingsAccount,loanAccount,Transfer_entry.get(),Transfer_account_number_entry.get())
        )
    btn_Transfer.place(relx=0.85, rely=0.60, anchor=CENTER)



app.mainloop()