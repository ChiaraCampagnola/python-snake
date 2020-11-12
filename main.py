from turtle import Turtle, Screen
from snake import Snake
from functools import partial
import time

def set_up_screen(screen):
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

screen = Screen()
set_up_screen(screen)
snake = Snake()
screen.update()

screen.listen()
screen.onkey(partial(snake.set_direction, "Up"), key="Up")
screen.onkey(partial(snake.set_direction, "Down"), key="Down")
screen.onkey(partial(snake.set_direction, "Left"), key="Left")
screen.onkey(partial(snake.set_direction, "Right"), key="Right")

snake.move_forward()
screen.update()
snake.move_forward()
screen.update()
snake.move_forward()
screen.update()

game_over = False
while not game_over:
    snake.move()
    screen.update()

    time.sleep(0.1)



screen.exitonclick()