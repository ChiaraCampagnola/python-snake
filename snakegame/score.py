import pkg_resources
from turtle import Turtle
from snakegame.utils import get_high_score, save_high_score
SCREEN_SIZE = 500
HALF_SCREEN = SCREEN_SIZE/2

class Score(Turtle):
    ''' Keeps track of score and displays it on screen '''
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(-90,HALF_SCREEN-25)
        self.pencolor("black")

        self.score = 0
        self.highscore = get_high_score()
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align="left", font=("Courier", 14, "normal"))

    def update(self):
        ''' Increases score by 1 '''
        self.score += 1
        self.update_screen()

    def reset(self):
        ''' Sets score to 0 '''
        self.score = 0
        self.update_screen()

    def update_highscore(self):
        ''' Saves highscore '''
        if self.score > self.highscore:
            self.highscore = self.score
            save_high_score(self.highscore)
