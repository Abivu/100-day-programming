import random
import schedule
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[random.randint(0, len(COLORS)-1)])
        self.goto(300, random.randint(-250, 250))

    
    def running(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    
    def car_generate(self):
        schedule.every(10).seconds.do(CarManager)
        schedule.run_pending()



