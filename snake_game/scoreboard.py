from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self): 
        super().__init__()
        self.curr_score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score()
   

    def score(self):
        self.goto(0, 240)
        self.clear()
        self.write(f"Score: {self.curr_score} - High score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", move=False, align="center", font=("Arial", 20, "normal"))

    def is_high_score(self):
        if self.curr_score > self.high_score:
            self.high_score = self.curr_score
            return True
        return False
    
    
    def reset(self):
        if self.is_high_score():
            self.curr_score = 0
            self.score()
    

    def upgrade(self):
        self.curr_score += 1
        self.score()
