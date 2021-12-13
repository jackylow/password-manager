from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_new_pass():
    new_web = web_input.get()
    new_user = user_input.get()
    new_pass = pass_input.get()
    new_password_manager = {
        new_web: {
            "email": new_user,
            "password": new_pass,
        }
    }

    # Dialog boxed and Pop-Ups
    if len(new_web) == 0 or len(new_pass) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("password_manager.json", "r") as file_with_password:
                # reading old file
                file = json.load(file_with_password)
        except FileNotFoundError:
            with open("password_manager.json", "w") as file_with_password:
                json.dump(new_password_manager, file_with_password, indent=4)
        else:
            # updating old file with new password manager
            file.update(new_password_manager)

            with open("password_manager.json", "w") as file_with_password:
                # saving updated file
                json.dump(file, file_with_password, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
            web_input.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    new_web = web_input.get()
    try:
        with open("password_manager.json", "r") as file_with_password:
            # reading old file
            file = json.load(file_with_password)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File Not Find")
    else:
        if new_web in file:
            email = file[new_web]["email"]
            password = file[new_web]["password"]
            messagebox.showinfo(title=new_web, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {new_web} exists")
    finally:
        web_input.delete(0, END)
        web_input.focus()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
web_input = Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()

user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "testing@mail.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)

pass_gen_button = Button(text="Generate Password", width=10, command=generate_password)
pass_gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=add_new_pass)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
