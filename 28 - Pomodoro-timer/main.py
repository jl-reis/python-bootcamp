from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
cycles = 0
breaks = 0
reset = False
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """Reset the timer"""
    global checks
    global reset
    global cycles
    cycles = 0
    reset = True
    checks = ""
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text=checks, bg=YELLOW)
    timer_label.config(text="Break", bg=YELLOW)
    canvas.config(bg=YELLOW)
    window.config(bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    """Start the timer"""
    global checks
    global cycles
    global reset
    reset = False
    cycles += 1

    # Checks the number of cycles for long or short breaks
    if cycles % 8 == 0:
        countdown(LONG_BREAK_MIN - 1)
        check_label.config(text=checks, bg=RED)
        timer_label.config(text="Break", bg=RED)
        canvas.config(bg=RED)
        window.config(bg=RED)
    elif cycles % 2 == 0:
        checks += "✓"
        check_label.config(text=checks, bg=PINK)
        timer_label.config(text="Break", bg=PINK)
        canvas.config(bg=PINK)
        window.config(bg=PINK)
        countdown(SHORT_BREAK_MIN - 1)
    else:
        countdown(WORK_MIN - 1)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(minutes, seconds=60):
    """Countdown for n number of minutes"""
    global reset
    if not reset:
        if minutes >= 0:
            seconds -= 1
            if minutes < 10:
                minutes = f"0{minutes}"
            if seconds < 10:
                seconds = f"0{seconds}"
            canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
            minutes = int(minutes)
            seconds = int(seconds)
            if seconds == 0:
                minutes -= 1
                seconds = 60
            window.after(1000, countdown, minutes, seconds)
        else:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #

checks = ""

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

check_label = Label(text=checks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
check_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
