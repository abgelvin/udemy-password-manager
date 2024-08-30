from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please make sure you have not left any fields empty.')
    else:
        try:
            with open('data.json', 'r') as f:
                # Read old data
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                # Create data file with new data
                json.dump(new_data, f, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open('data.json', 'w') as f:
                # Save updated data
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get().lower()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            password = data[website]['password']
            messagebox.showinfo(title=website.title(), message=f'email: {email_entry.get()}\npassword: {password}')
    except KeyError:
        messagebox.showerror(title='Saved Password', message=f'No password found for {website}')
            


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=23)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(text='Search', command=find_password, width=13)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.insert(0, 'abgelvin@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()