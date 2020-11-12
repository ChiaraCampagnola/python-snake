SCREEN_SIZE = 600

from turtle import Turtle, Screen
from functools import partial
import time

from snake import Snake
from food import Food
from score import Score
from utils import set_up_screen

screen = Screen()
set_up_screen(screen)

snake = Snake()
food = Food()
score = Score()
screen.update()

screen.listen()
screen.onkey(partial(snake.set_direction, "Up"), key="Up")
screen.onkey(partial(snake.set_direction, "Down"), key="Down")
screen.onkey(partial(snake.set_direction, "Left"), key="Left")
screen.onkey(partial(snake.set_direction, "Right"), key="Right")

keep_playing = True

while keep_playing:

    game_over = False
    while not game_over:

        snake.move()
        screen.update()

        # Eat food
        if snake.head.distance(food) < 15:
            score.update()
            food.move()
            snake.extend()

        # Hit wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280:
            game_over = True
        if snake.head.ycor() > 260 or snake.head.ycor() < -280:
            game_over = True

        # Hit tail
        for segment in snake.tail:
            if snake.head.distance(segment) < 10:
                game_over = True

        time.sleep(0.1)

    user_choice = screen.numinput("Game over", f"Your score: {score.score}\nInput 1 to play again or 2 to exit.", 1, minval=1, maxval=2)
    if user_choice == 2:
        keep_playing = False
    else:
        food.move()
        snake.delete_snake()
        snake.create_snake()
        score.reset()
        screen.update()
        screen.listen()