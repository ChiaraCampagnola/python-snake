import pkg_resources
from turtle import Turtle

HIGH_SCORE_FILE = pkg_resources.resource_filename('snakegame', 'resources/highscore.txt')
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

def get_high_score():
    with open(HIGH_SCORE_FILE, mode="r") as file:
        highscore = int(file.read())
    return highscore

def save_high_score(highscore):
    with open(HIGH_SCORE_FILE, mode="w") as file:
        file.write(str(highscore))