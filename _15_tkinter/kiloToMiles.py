from tkinter import *

def milestokm():
    miles = float(user_input.get())
    km = round((miles* 1.609))
    output.config(text=f"{km}")

window = Tk()
window.title("miles to km converter")
window.minsize(width=500, height=300)
window.config(padx= 100, pady = 100)

label = Label(text= "miles")
label.grid(column = 3, row = 1)

is_equal_to = Label(text= "is equal to")
is_equal_to.grid(column = 1, row = 2)

user_input = Entry(width=7)
user_input.grid(column = 2, row = 1)

kms = Label(text="km")
kms.grid(column = 3, row = 2)

output = Label(text="0")
output.grid(column = 2, row = 2)

button = Button(text="calculate", command=milestokm)
button.grid(column = 2, row = 3)


window.mainloop()