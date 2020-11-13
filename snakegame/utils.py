''' Some useful functions to avoid cluttering main '''

from turtle import Turtle

SCREEN_SIZE = 600

def set_up_screen(screen):
    ''' Sets up the screen size and appearance'''
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    # Make a border
    draw = Turtle()
    draw.color("white")
    draw.penup()
    draw.goto(-300, -300)
    draw.pendown()
    draw.pensize(20)
    draw.goto(-300, 300)
    draw.pensize(60)
    draw.goto(290, 300)
    draw.pensize(20)
    draw.goto(290, -290)
    draw.goto(-290, -290)
