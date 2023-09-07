from turtle import Turtle
import time


class Ball(Turtle):
    
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.speed(1)
        self.color("white")
        self.pos_x = 5
        self.pos_y = 5
         
    

    def move(self):
        new_x = self.xcor() + self.pos_x
        new_y = self.ycor() + self.pos_y
        time.sleep(0.05)
        self.goto(new_x, new_y)

    
    def y_bounce(self):
        self.pos_y *= -1

    
    def x_bounce(self):
        self.pos_x *= -1
        