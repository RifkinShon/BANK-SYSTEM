from customtkinter import *

app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")


label = CTkLabel(master=app, text="Hello, World!", font=("Arial", 24))
label.place(relx=0.5, rely=0.3, anchor=CENTER)

entry = CTkEntry(master=app, placeholder_text="Enter text here", width=200, height=30, corner_radius=5)
entry.place(relx=0.5, rely=0.4, anchor=CENTER)

textbox = CTkTextbox(master=app, width=300, height=100, corner_radius=5)
textbox.place(relx=0.5, rely=0.6, anchor=CENTER)


btn = CTkButton(master=app, text="Click Me", corner_radius=10, fg_color="transparent", hover_color="green", text_color="white",
                border_color="gray", border_width=2, font=("Arial", 16, "bold"))
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

CTkComboBox(master=app, values=["Option 1", "Option 2", "Option 3"], width=200, height=30, corner_radius=5).place(relx=0.5, rely=0.7, anchor=CENTER)

checkbox = CTkCheckBox(master=app, text="Check me", font=("Arial", 14))
checkbox.place(relx=0.5, rely=0.9, anchor=CENTER)

switch = CTkSwitch(master=app, text="Switch me", font=("Arial", 14))
switch.place(relx=0.5, rely=0.8, anchor=CENTER)

app.mainloop()