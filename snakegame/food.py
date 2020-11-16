from turtle import Turtle
import random

SCREEN_SIZE = 500
HALF_SCREEN = SCREEN_SIZE/2

class Food(Turtle):
    ''' Creates and controls the snake food '''

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

        food_limit = HALF_SCREEN-35

        random_location = (random.randint(-food_limit, food_limit),
                            random.randint(-food_limit, food_limit))
        self.goto(random_location)