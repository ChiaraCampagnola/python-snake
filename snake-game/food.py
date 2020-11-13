from turtle import Turtle
import random

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

        print(f"\n\nNAME: {__name__}\n\n")

    def move(self):
        ''' Move the piece of food to a random location'''
         # Create food at random location
        random_location = (random.randint(-270, 270),
                            random.randint(-270, 260))
        self.goto(random_location)

if __name__ == "__main__":
    print("\n\n\nFOOOOOOOOD\n\n\n")
    print(f"\n\nNAME: {__name__}\n\n")
    