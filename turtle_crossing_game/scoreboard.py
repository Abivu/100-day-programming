from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.curr_score = 0
        self.penup()
        self.hideturtle()
        self.score()

    
    def score(self):
        self.goto(-260, 260)
        self.clear()
        self.write(f"Score: {self.curr_score}", move=False, align="left", font=FONT)


    def upgrade(self):
        self.curr_score += 1
        self.score()


    def game_over(self):
        self.goto(-20, 0)
        self.write("Game Over", move=False, align="left", font=FONT)

