from tkinter import *
import math
from click import style, command
from matplotlib.pyplot import title

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer =None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text ="00:00")
    text.config(text="Timer")
    checkmark.config(text = "")
    global reps
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8 == 0:
        count_down(long_break_sec)
        text.config(text="chill", fg=RED)
    elif reps%2 == 0:
        count_down(short_break_sec)
        text.config(text="break", fg=PINK)
    else:
        count_down(work_sec)
        text.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec<10 :
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text = count)
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count  >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range (math.floor(reps/2)):
            marks += "✓"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=40, pady=50, bg=YELLOW)
window.title("pomodoro")

text = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME,40))
text.grid(column = 2, row = 1)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(101,130, text="00:00", fill="white", font=(FONT_NAME, 30))
canvas.grid(column = 2, row = 2)



start_button = Button(text="Start", command=start_timer)
start_button.grid(column = 1, row = 3)


reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column = 3, row = 3)

checkmark = Label(bg=YELLOW )
checkmark.grid(column = 2, row = 3)

window.mainloop()