from turtle import Turtle

class object(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.speed("fast")
        self.goto(0,-280)

    def up(self):
        self.forward(30)

    def down(self):
        self.backward(10)