from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        #self.speed("fastest")
        self.penup()
        self.move()

    def move(self):
        ''' Move the piece of food to a random location'''
         # Create food at random location
        random_location = (random.randint(-270, 270),
                            random.randint(-270, 270))
        self.goto(random_location)
