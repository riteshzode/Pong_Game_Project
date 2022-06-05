from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 35, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-50, 240)
        self.write(f"{self.left_score}", align=ALIGN, font=FONT)
        self.goto(50, 240)
        self.write(f"{self.right_score}", align=ALIGN, font=FONT)

    def right_score_increase(self):
        self.right_score += 1
        self.score_update()

    def left_score_increase(self):
        self.left_score += 1
        self.score_update()
