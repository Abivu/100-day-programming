from turtle import Turtle
X_POS = 350; Y_POS = 0
class Paddle(Turtle):

    def __init__(self, xy_cor):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(xy_cor)


    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
