from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self): 
        super().__init__()
        self.curr_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score()
   

    def score(self):
        self.goto(0, 240)
        self.clear()
        self.write(f"Score: {self.curr_score}", move=False, align="center", font=("Arial", 20, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Arial", 20, "normal"))

    
    def upgrade(self):
        self.curr_score += 1
        self.score()
