from turtle import Screen
from functools import partial
import time

from snakegame.snake import Snake
from snakegame.food import Food
from snakegame.score import Score
from snakegame.utils import set_up_screen

SCREEN_SIZE = 500
HALF_SCREEN = SCREEN_SIZE/2

def play():
    ''' Plays game '''

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

    wall_limit = HALF_SCREEN-40

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
            if snake.head.xcor() > wall_limit or snake.head.xcor() < -wall_limit-20:
                game_over = True
            if snake.head.ycor() > wall_limit or snake.head.ycor() < -wall_limit:
                game_over = True

            # Hit tail
            for segment in snake.tail:
                if snake.head.distance(segment) < 10:
                    game_over = True

            time.sleep(0.1)

        score.update_highscore()

        user_choice = screen.numinput("Game over",
            f"Your score: {score.score}\nInput 1 to play again or 2 to exit.",
            1, minval=1, maxval=2)
        if user_choice == 2:
            keep_playing = False
        else:
            food.move()
            snake.delete_snake()
            snake.create_snake()
            score.reset()
            screen.update()
            screen.listen()