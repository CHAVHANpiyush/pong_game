from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
paddle_1=Paddle((350,0))
paddle_2=Paddle((-350,0))

screen.listen()
screen.onkey(paddle_1.go_up,"Up")
screen.onkey(paddle_1.go_down,"Down")
screen.onkey(paddle_2.go_up,"w")
screen.onkey(paddle_2.go_down,"s")

game_is_on=True
score=Scoreboard()
ball=Ball()
score.update_score()
x=0.07
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #COLLISI ON WITH WALL
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #collision with right paddle
    if ball.distance(paddle_1)<50:
        ball.bounce_x()
    # collision with left paddle
    if ball.distance(paddle_2) < 50:
        ball.bounce_x()
    if ball.xcor()>380 :
        ball.reposition()
        score.left_point()
        score.update_score()

    if ball.xcor()<-380:
        ball.reposition()
        score.right_point()
        score.update_score()
