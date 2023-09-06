from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)


snake = Snake()
food = Food()
score_board = ScoreBoard()


scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    scr.update()
    snake.move()
    time.sleep(0.1)


    # Detect collision with food
    if snake.head.distance(food) < 25:
        food.refresh()
        score_board.upgrade()
        snake.extend()


    # Detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        score_board.game_over()


    # Detect collision with any segment of the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            score_board.game_over()




















scr.exitonclick()