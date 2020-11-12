SCREEN_SIZE = 600
from turtle import Turtle

def set_up_screen(screen):
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
    draw.goto(290, 300)
    draw.goto(290, -290)
    draw.goto(-290, -290)