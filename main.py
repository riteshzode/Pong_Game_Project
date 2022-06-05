from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PING PONG GAME")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_reverse()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.x_reverse()

    if ball.xcor() > 380:
        ball.ball_reset()
        score.left_score_increase()

    if ball.xcor() < -380:
        ball.ball_reset()
        score.right_score_increase()

screen.exitonclick()
