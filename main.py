from turtle import Screen

import obstacle
from turtles import object
from obstacle import Obstacle
import time
from scorboard import Scoreboard

score=Scoreboard()
score2=Scoreboard()
score2.scorecount()
screen=Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Crossing Game")
screen.tracer(0)
obj=object()

screen.onkey(obj.up,"Up")
screen.onkey(obj.down,"Down")
is_game_on=True
o = Obstacle()
while is_game_on:
     time.sleep(0.1)
     screen.update()
     o.cars()
     o.move()
     for cars in o.allcars:
          if obj.distance(cars)<20:
               score.game_over()
               is_game_on=False

          if obj.ycor()>300:
               obj.goto(0,-280)
               score2.clear()
               score2.level+=1
               score2.scorecount()
               obstacle.speed+=10



























screen.exitonclick()
