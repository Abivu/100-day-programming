from turtle import Screen
from snake import Snake
from food import Food
import time


scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)


snake = Snake()
food = Food()


scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # print("nom nom nom")
        food.refresh()


































scr.exitonclick()