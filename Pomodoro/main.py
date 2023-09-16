from tkinter import *
# import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
start_count = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(start_count)
    # Reset the UI
    canvas.itemconfig(timer_text, text = "00:00")
    timer.config(text="Timer", fg=GREEN)
    check.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # count_down(15) #count by minute count=300s
    global REPS
    work_session = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    REPS += 1
    if REPS % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break)
    elif REPS == 8:
        timer.config(text="Break", fg=RED)
        count_down(long_break)
        REPS = 0
    elif REPS % 2 != 0:
        timer.config(text="Work", fg=GREEN)
        count_down(work_session)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" #Dynamic typing. unique in Python
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global start_count
        start_count = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(REPS//2):
            mark += "✓"
        check.config(text=mark)
            


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./Pomodoro/tomato.png") #? Haven't really understood the filepath works. Ask later!!!
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


# Label Timer & Checkmark
timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(row=1, column=2)

check = Label(text="", bg=YELLOW, fg=GREEN)
check.grid(row=4, column=2)

# Button Start & Reset
start = Button(text="Start", command=start_timer)
start.grid(row=3, column=1)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=3, column=3)

window.mainloop()
