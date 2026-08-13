from tkinter import messagebox

from customtkinter import *
from Main_GUI import *
answers_list = []

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

def login_info():
    try:
        rew_account_number = login_acc_entry.get()
        rew_password = login_pass_entry.get()

        valid_account_number, valid_password = CustomerUtils.login_GUI(rew_account_number, rew_password)
        Customer_login(valid_account_number, valid_password)
        messagebox.showinfo("Success", "Login successful")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
   
    

from tkinter import messagebox
from core.customer import CustomerUtils  # ייבוא המחלקה שיצרת
from Main_GUI import Customer_create      # או איפה שפונקציית היצירה יושבת

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
        Customer_create(
            valid_id, valid_name, valid_age, 
            valid_email, valid_phone, valid_address, valid_password
        )

        # 4. הודעת הצלחה
        messagebox.showinfo("Success", "Account created successfully!")

    except ValueError as e:
        # 5. ה-except תופס את ה-raise הראשון שנזרק מ-CustomerUtils!
        # המשתנה e מכיל את ההודעה המדויקת שהגדרת ב-CustomerUtils
        messagebox.showerror("Input Error", str(e))















app = CTk()
app.geometry("500x550")  # Expanded height slightly to accommodate the sign-up inputs nicely
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
btn_signup.place(relx=0.5, rely=0.88, anchor=CENTER)


app.mainloop()