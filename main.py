from turtle import Screen
from snake import Snake
import time

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)


snake = Snake()


game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.05)

    snake.move()
































scr.exitonclick()