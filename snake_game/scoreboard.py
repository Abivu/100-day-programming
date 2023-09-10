from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self): 
        super().__init__()
        self.curr_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score()
   

    def score(self):
        self.goto(0, 240)
        self.clear()
        self.write(f"Score: {self.curr_score} - High score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))


    def is_high_score(self):
        if self.curr_score > self.high_score:
            self.high_score = self.curr_score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
            return True
        return False
    
    
    def reset(self):
        if self.is_high_score():
            self.curr_score = 0
            self.score()
    

    def upgrade(self):
        self.curr_score += 1
        self.score()
