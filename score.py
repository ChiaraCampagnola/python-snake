from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(-40,275)
        self.pencolor("black")

        self.score = 0
        self.write(f"Score: {self.score}", align="left", font=("Courier", 14, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Courier", 14, "normal"))

    def reset(self):
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Courier", 14, "normal"))

