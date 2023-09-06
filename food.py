from turtle import Turtle
import random
class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        x_cor = random.randint(-260, 260)
        y_cor = random.randint(-260, 260)
        self.goto(x_cor, y_cor)

