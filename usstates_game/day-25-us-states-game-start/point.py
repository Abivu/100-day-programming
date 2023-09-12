from turtle import Turtle

class Point(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # self.name_the_state()

    
    def name_the_state(self, x_cor, y_cor, formated_answer_state):
        self.goto(x_cor, y_cor)
        self.write(formated_answer_state)