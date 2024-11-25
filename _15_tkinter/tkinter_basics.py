from tkinter import *

window = Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

#label
my_label = Label(text="A text", font=("arial", 24, "bold"))
# my_label.pack()
# my_label["text"]= "new text"
# my_label.config(text="again the next one")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
#button
def clicked():
    my_label["text"]= "button got clicked"  #better use cofig, looks clean
    print(user_input.get())

button = Button(text="click me", command=clicked)
# button.pack()
button.grid(column=1, row=1)


#entry
user_input = Entry(width=10)
# user_input.pack()
user_input.grid(column=2, row=2)
window.mainloop()

