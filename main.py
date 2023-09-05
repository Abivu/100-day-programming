from turtle import Screen
from snake import Snake
import time

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)


snake = Snake()


scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(0.1)
    scr.update()































scr.exitonclick()