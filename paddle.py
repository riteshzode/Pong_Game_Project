from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        y = self.ycor() + 50
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 50
        self.goto(self.xcor(), y)
