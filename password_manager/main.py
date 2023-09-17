from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_auto():
    password = password_generator()
    pw_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    # Take all values from entries
    web_data = web_input.get()
    email_user_data = email_user_input.get()
    pw_data = pw_input.get()
    new_data = {
        web_data: {
            "email": email_user_data,
            "pass": pw_data
        }
    }
    
    if len(web_data) == 0 or len(email_user_data) == 0 or len(pw_data) == 0:
        messagebox.showwarning("Missing field(s)", message="All fields must be required!")
    else:
        is_ok = messagebox.askokcancel("Information Confirm", message=f"Doublel check the info before OK:\nWebsite: {web_data}\nEmail/Username: {email_user_data}\nPassword: {pw_data}\nIs all the info correct?")
        
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Read the file
                    data = json.load(file)
                    # Add a new data into the file
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Created a new JSON file and write in.
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    # Save the updated date into the file
                    json.dump(data, file, indent=4)
            delete()

def delete():
    web_input.delete(0, END)
    # email_user_input.delete(0, END)
    pw_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
# window.minsize(1000, 1000)
window.config(padx=50, pady=50)

app = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
app.create_image(100, 100, image=pass_img)
app.grid(column=2, row=1)

# Label web, email, password
web = Label(text="Website: ")
web.grid(column=1, row=2)

email_user = Label(text="Email/Username: ")
email_user.grid(column=1, row=3)

pw = Label(text="Password: ")
pw.grid(column=1, row=4)

#Entry
web_input = Entry(width=50)
web_input.grid(column=2, row=2, columnspan=2)


email_user_input = Entry(width=50)
email_user_input.grid(column=2, row=3, columnspan=2)
email_user_input.insert(0, "abivu@gmail.com")

pw_input = Entry(width=32)
pw_input.grid(column=2, row=4)

#Button
generate_pw = Button(text="Generate Password", command=password_auto)
generate_pw.grid(column=3, row=4)

add = Button(text="Add", width=45, command=save_data)
add.grid(column=2, row=5, columnspan=2)


window.mainloop()