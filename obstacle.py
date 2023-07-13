from turtle import Turtle
speed=10
import random
colors=["white","purple","blue","green"]
class Obstacle():
    def __init__(self):
        self.allcars=[]

    def cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
          new_cars=Turtle()
          new_cars.penup()
          new_cars.y = random.randint(-250, 250)
          new_cars.shape("square")
          new_cars.shapesize(stretch_wid=1.2, stretch_len=2)
          new_cars.color(random.choice(colors))
          new_cars.speed("fast")
          new_cars.goto(420, new_cars.y)
          self.allcars.append(new_cars)

    def move(self):
        for i in range(0,len(self.allcars)):
            self.allcars[i].backward(speed)



