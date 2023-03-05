from turtle import Turtle
from typing import Tuple


class Paddle(Turtle):

    def __init__(self, cor: Tuple[int, int] = (0, 0)):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.setpos(cor[0], cor[1])

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
