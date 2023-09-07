from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.up_score()
   
    
    def up_score(self):
        self.clear()
        self.goto(100, 250)
        self.write(f"{self.r_score}", move= False, font= ("Courier", 25, "normal"))
        self.goto(-100, 250)
        self.write(f"{self.l_score}", move= False ,font=("Courier", 25, "normal"))
