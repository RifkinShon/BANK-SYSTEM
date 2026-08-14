from customtkinter import *

app = CTk()
app.geometry("500x550")  # הגדלנו מעט את הגובה כדי שיהיה מקום לכולם
set_appearance_mode("dark")

# 1. כותרת
label = CTkLabel(master=app, text="Hello, World!", font=("Arial", 24))
label.place(relx=0.5, rely=0.1, anchor=CENTER)

# 2. שדה קלט
entry = CTkEntry(master=app, placeholder_text="Enter text here", width=220, height=30, corner_radius=5)
entry.place(relx=0.5, rely=0.2, anchor=CENTER)

# 3. כפתור
btn = CTkButton(
    master=app, 
    text="Click Me", 
    corner_radius=10, 
    fg_color="transparent", 
    hover_color="green", 
    text_color="white",
    border_color="gray", 
    border_width=2, 
    font=("Arial", 16, "bold")
)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

# 4. תיבת טקסט רב-שורתית
textbox = CTkTextbox(master=app, width=300, height=80, corner_radius=5)
textbox.place(relx=0.5, rely=0.45, anchor=CENTER)

# 5. תיבת בחירה (ComboBox)
combo = CTkComboBox(
    master=app, 
    values=["Option 1", "Option 2", "Option 3"], 
    width=200, 
    height=30, 
    corner_radius=5
)
combo.place(relx=0.5, rely=0.62, anchor=CENTER)

# 6. מתג (Switch)
switch = CTkSwitch(master=app, text="Switch me", font=("Arial", 14))
switch.place(relx=0.5, rely=0.73, anchor=CENTER)

# 7. תיבת סימון (CheckBox)
checkbox = CTkCheckBox(master=app, text="Check me", font=("Arial", 14))
checkbox.place(relx=0.5, rely=0.83, anchor=CENTER)

app.mainloop()