import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((WIDTH // 2 - 50, 0))
l_paddle = Paddle((-WIDTH // 2 + 50, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > HEIGHT / 2 - ball.width() or ball.ycor() < -HEIGHT / 2 - ball.width():
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > WIDTH / 2 - 80) \
            or (ball.distance(l_paddle) < 50 and ball.xcor() < -WIDTH / 2 + 80):
        ball.bounce_x()
    screen.update()

screen.exitonclick()
