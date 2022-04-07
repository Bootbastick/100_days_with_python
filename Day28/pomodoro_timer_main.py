from tkinter import *
import math


# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN ="#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = None


# Timer reset
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="Time", fg=GREEN)
    pomodoros_done.config(text="")
    reps = 0


# Timer mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        text.config(text="Work", fg=GREEN)


# Countdown mechanism
def count_down(count):
    global reps
    global checkmarks
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks += "✓"
            pomodoros_done.config(text=checkmarks)


# UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

text = Label(text="Time", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
text.grid(row=0, column=1)

start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

pomodoros_done = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
pomodoros_done.grid(row=3, column=1)


window.mainloop()
