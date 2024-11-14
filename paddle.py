from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.create_paddle()
        

    def create_paddle(self):
        self.shape("square")
        self.color('red')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.pos)

    def move_up(self):
        new_yup = self.ycor() + 30
        x = self.xcor()
        self.goto(x, new_yup)

    def move_down(self):
        new_ydown = self.ycor() - 30
        x = self.xcor()
        self.goto(x, new_ydown)

