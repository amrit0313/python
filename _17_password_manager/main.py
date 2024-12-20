import json
from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbol
    password =  "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{
        "email": email,
        "password":password,
    }}

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Hey! make sure you haven't left fields empty")
    else:
        try:
           with open("data.json",'r') as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
           with open("data.json", "w") as data_file:
               json.dump(new_data, data_file, indent=4)
        else:
            # updating data with new data
            data.update(new_data)
            # saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



#-----------------------------search option ---------------------------#

def search_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="not data yet", message="site not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="error", message="website not found")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx= 40, pady=40)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas_img = canvas.create_image(100, 100, image = logo)
canvas.grid(column = 2, row = 1)

website_label = Label(text="website: ")
website_label.grid(column = 1, row = 2)

website_entry = Entry(width=25)
website_entry.grid(column = 2, row = 2)

search_button = Button(text="search", command=search_password, width=10)
search_button.grid(column = 3, row = 2)


email_label = Label(text="Email/Username: ")
email_label.grid(column = 1, row = 3)

email_entry = Entry(width = 40)
email_entry.insert(END,"amrit@gmail.com")
email_entry.grid(column = 2, row = 3, columnspan = 2)


password_label = Label(text="password: ")
password_label.grid(column = 1, row = 4)

password_entry = Entry(width = 26)
password_entry.grid(column = 2, row = 4)

generate_password_button = Button(text="Generate", width=10, command=generate_password)
generate_password_button.grid(column = 3, row = 4)


add_button = Button (text="Add", width=36, command=add_data)
add_button.grid(column = 2, row = 5, columnspan = 2)



window.mainloop()