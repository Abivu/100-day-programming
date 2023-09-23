from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain): # In this new class, an argument is passed and it could be an object from another class. 
        ## By this way, this object would be able to use methods of its own class
        ## & interact with this class
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250) # width & height must be defined
        self.question_text = self.canvas.create_text(150, 125, text="", font=("Arial", 15, "italic"),fill=THEME_COLOR, width=280)
        self.canvas.grid(column=1, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image= true_img, command=self.choose_true)
        self.true_button.grid(column=1, row=2)

        self.false_button = Button(image=false_img, command=self.choose_false)
        self.false_button.grid(column=2, row=2)

        self.get_next_question()

        self.window.mainloop()
    

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def choose_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    
    def choose_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)        


