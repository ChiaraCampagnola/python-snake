from turtle import Turtle

class Score(Turtle):
    ''' Keeps track of score and displays it on screen '''
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(-90,275)
        self.pencolor("black")

        self.score = 0
        self.highscore = self.get_high_score()
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
            self.save_high_score()

    def save_high_score(self):
        with open("snake_highscore.txt", mode="w") as file:
            file.write(str(self.highscore))

    def get_high_score(self):
        try:
            with open("snake_highscore.txt", mode="r") as file:
                highscore = int(file.read())
        except:
            highscore = 0
        return highscore
