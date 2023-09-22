from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250) # width & height must be defined
        self.question_text = self.canvas.create_text(100, 50, text="Hello world", font=("Arial", 20, "italic"),fill=THEME_COLOR)
        self.canvas.grid(column=1, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image= true_img)
        self.true_button.grid(column=1, row=2)

        self.false_button = Button(image=false_img)
        self.false_button.grid(column=2, row=2)





        self.window.mainloop()