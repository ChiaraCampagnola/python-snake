FOOD_SIZE = 0.5
SCREEN_SIZE = 300 # 600 x 600

from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=FOOD_SIZE, stretch_len=FOOD_SIZE)
        self.color("red")
        #self.speed("fastest")
        self.penup()
        self.move()

    def move(self):
        ''' Move the piece of food to a random location'''
         # Create food at random location
        random_location = (random.randint(-(SCREEN_SIZE-40), SCREEN_SIZE-40),
                            random.randint(-(SCREEN_SIZE-40), SCREEN_SIZE-40))
        self.goto(random_location)
