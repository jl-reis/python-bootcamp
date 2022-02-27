from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Courier", 14, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generate password with letters, numbers and symbols"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    """Save password to file"""
    password_input = password_entry.get()
    website_input = website_entry.get()
    username_input = username_entry.get()
    new_password_data = {
        website_input: {
            "Email": username_input,
            "Password": password_input,
        }
    }

    # Warn user about empty field
    if len(password_input) == 0 or len(website_input) == 0 or len(username_input) == 0:
        messagebox.showwarning(title="Field empty", message="You forgot to fill the infos required")

    else:
        # Ask user to confirm information before saving
        is_ok = messagebox.askokcancel(title=website_input, message="The following information will be saved:\n"
                                       f"Website: {website_input} \nPassword: {password_input}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_password_data, data_file, indent=4)
            else:
                data.update(new_password_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    """Search password saved in file"""
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No entry found")
    else:
        website_input = website_entry.get()
        if website_input in data.keys():
            messagebox.showinfo(title=website_input, message=f"Username: {data[website_input]['Email']}\n"
                                                             f"Password: {data[website_input]['Password']}")
        else:
            messagebox.showerror(title="Error", message="No entry found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=19)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_label = Label(text="Email/Username", font=FONT)
username_label.grid(row=2, column=0)

username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "email@email.com")

password_label = Label(text="Password", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", command=search_password, width=15)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_password_button = Button(text="Add", width=35, command=save_password)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
