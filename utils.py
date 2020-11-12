SCREEN_SIZE = 600
from turtle import Turtle
import time

from snake import Snake
from food import Food
from score import Score

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
    draw.pensize(60)
    draw.goto(290, 300)
    draw.pensize(20)
    draw.goto(290, -290)
    draw.goto(-290, -290)

def play_game(screen):
    game_over = False

    snake = Snake()
    food = Food()
    score = Score()

    while not game_over:
        snake.move()
        screen.update()

        # Eat food
        if snake.head.distance(food) < 15:
            score.update_score()
            food.move()

        # Hit wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280:
            game_over = True
        if snake.head.ycor() > 260 or snake.head.ycor() < -280:
            game_over = True

        time.sleep(0.1)

    user_choice = screen.numinput("Game over", f"Your score: {score.score}\nInput 1 to play again or 2 to exit.", 1, minval=1, maxval=2)

    return user_choice