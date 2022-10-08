import math
from tkinter import *
import time

user_name = str(input('What is your name?: ')).title()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 35  # 25
SHORT_BREAK_MIN = 10  # 5
LONG_BREAK_MIN = 30  # 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    mark = ''
    check_marks.config(text=mark)
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if rep % 2 != 0:
        countdown(work_sec)
        timer_label.config(text=f'Time to Work {user_name}', fg=GREEN)
    elif rep % 8 == 0:
        countdown(long_break_min)
        timer_label.config(text=f'Take A Long Break {user_name}', fg=RED)
    elif rep % 2 == 0 and rep != 8:
        countdown(short_break_sec)
        timer_label.config(text=f'Here\'s A Short Break {user_name}', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ''
        checked_reps = math.floor(rep/2)
        for _ in range(checked_reps):
            mark += '✔'
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


# Tomato with clock
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='day_28_tomato.png')
canvas.create_image(100, 112, image=tomato)
canvas_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Timer heading on top
timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.config(padx=5, pady=10)
timer_label.grid(column=1, row=0)

# Start Button
start_button = Button(text='Start', bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text='Reset', bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Text
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.config(pady=10, padx=5)
check_marks.grid(column=1, row=3)

window.mainloop()
