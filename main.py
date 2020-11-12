SCREEN_SIZE = 600

from turtle import Turtle, Screen
from functools import partial
import time

from snake import Snake
from food import Food
from utils import set_up_screen

screen = Screen()
set_up_screen(screen)

snake = Snake()
food = Food()
screen.update()

screen.listen()
screen.onkey(partial(snake.set_direction, "Up"), key="Up")
screen.onkey(partial(snake.set_direction, "Down"), key="Down")
screen.onkey(partial(snake.set_direction, "Left"), key="Left")
screen.onkey(partial(snake.set_direction, "Right"), key="Right")

game_over = False
while not game_over:
    snake.move()
    screen.update()

    if snake.head.distance(food) < 15:
        print("YAY!!!!")
        food.move()

    time.sleep(0.1)



screen.exitonclick()