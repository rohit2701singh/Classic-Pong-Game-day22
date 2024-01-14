import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

tim = Turtle()  # draw line in
tim.color("white")
tim.width(3)
tim.speed(0)  # fastest drawing speed

tim.penup()
tim.goto(0, 210)
tim.pendown()
tim.goto(0, -210)
tim.hideturtle()


r_paddle = Paddle((375, 0))
l_paddle = Paddle((-375, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the top and bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # detect collision with the r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350) or (ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_x()

    # detect ball missing r_paddle.
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()

    # detect ball missing r_paddle.
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
