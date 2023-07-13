from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.level=0


    def game_over(self):
        self.write("Game Over")

    def scorecount(self):

        self.goto(0,280)
        self.write(f"Level {self.level }")
