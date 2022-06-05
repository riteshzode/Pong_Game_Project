from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ballmake()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def ballmake(self):
        self.penup()
        self.shape("circle")
        self.color("white")

    # This move function will increase x and y coordinate by 10 as it will run
    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x, y)

    # this both x and y reverse the value +ve to -ve or -ve to +ve
    def y_reverse(self):
        self.ymove *= -1
        # self.ymove = self.ymove * -1

    def x_reverse(self):
        self.xmove *= -1
        self.move_speed *= 0.9
        # self.xmove = self.xmove * -1

    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_reverse()
