from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="]

# Password generator

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = []
    for i in range(0, (nr_numbers + nr_letters + nr_symbols)):
        b = random.randint(1, 11)
        if b % 5 == 0:
            letter = random.choice(letters)
            password.append(letter)
        if b % 3 == 0:
            symbol = random.choice(symbols)
            password.append(symbol)
        if b % 2 == 0:
            number = random.choice(numbers)
            password.append(number)

    password_entry.insert(0, "".join(password))
    pyperclip.copy("".join(password))


# Save password
def save():
    input_data = f"{website_entry.get()} / {email_entry.get()} / {password_entry.get()}"
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

        else:
            with open("data.json", mode="w") as file:
                data.update(new_data)
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            website_entry.insert(0, "")

            password_entry.delete(0, END)
            password_entry.insert(0, "")

# Search password
def find_password():
    website_is_found = False
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except:
        messagebox.showinfo(title="Error", message="You don't have any saved websites!")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Your email on that website: {data[website]['email']}\n"
                                                        f"Your password on that website:{data[website]['password']}")
            password_entry.insert(0, data[website]["password"])
            website_is_found = True
        if not website_is_found:
            messagebox.showinfo(title="Error", message="No matching websites found")

# UI Setup
window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 94.5, image=lock_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.insert(0, "boikoff.nikita@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", command=find_password)
search.grid(row=1, column=2)


window.mainloop()
