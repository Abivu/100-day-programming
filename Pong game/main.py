from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

scr = Screen()
scr.setup(width=800, height= 600)
scr.bgcolor("black")
scr.title("Pong Game")
scr.tracer(0)
scr.listen()


r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
scr.update()
# TODO: Change it into "hold pressing"
# TODO: Is it possible to simply/condense the code?
scr.onkey(key = "Up", fun = r_pad.move_up)
scr.onkey(key = "Down", fun = r_pad.move_down)
scr.onkey(key = "w", fun = l_pad.move_up)
scr.onkey(key = "s", fun = l_pad.move_down)

scoreboard = Scoreboard()
ball = Ball()
game_is_on = True
while game_is_on:
    ball.move()
    scr.update()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    
    # Detect collision with paddle
    if ball.distance(r_pad) < 50 and ball.xcor() >= 330 or ball.distance(l_pad) < 50 and ball.xcor() <= -330:
        ball.x_bounce()

    # Detect if the ball misses paddle
    if ball.xcor() > 340:
        ball.goto(0, 0)
        ball.x_bounce()
        scoreboard.l_score += 1
        scoreboard.up_score()
    
    
    if ball.xcor() < -340:
        ball.goto(0, 0)
        ball.x_bounce()
        scoreboard.r_score += 1
        scoreboard.up_score()



 # TODO: create func that l_pad played by computer  
 # TODO: increase speed everytime the ball hits a paddle  

 

















scr.exitonclick()