import pkg_resources
from turtle import Turtle

HIGH_SCORE_FILE = pkg_resources.resource_filename('snakegame', 'resources/highscore.txt')
SCREEN_SIZE = 500
HALF_SCREEN = SCREEN_SIZE/2

def set_up_screen(screen):
    ''' Sets up the screen size and appearance'''
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    # Make a border
    draw = Turtle()
    draw.color("white")
    draw.pensize(20)
    draw.penup()
    draw.goto(HALF_SCREEN-10, HALF_SCREEN)
    draw.pendown()
    draw.goto(HALF_SCREEN-10, -(HALF_SCREEN-10))
    draw.goto(-HALF_SCREEN, -(HALF_SCREEN-10))
    draw.goto(-HALF_SCREEN, HALF_SCREEN)
    draw.pensize(60)
    draw.goto(HALF_SCREEN, HALF_SCREEN)

def get_high_score():
    with open(HIGH_SCORE_FILE, mode="r") as file:
        highscore = int(file.read())
    return highscore

def save_high_score(highscore):
    with open(HIGH_SCORE_FILE, mode="w") as file:
        file.write(str(highscore))