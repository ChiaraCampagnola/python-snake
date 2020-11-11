from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

def move_forward(snake):
    for bit in range(len(snake)-1, 0, -1):
        print(f"bit: {bit}")
        next_pos = snake[bit-1].pos()
        print(f"next_post: {next_pos}")
        snake[bit].goto(next_pos)
    snake[0].forward(20)
    screen.update()


# Create starting snake
snake = []
for i in range(3):
    new_snake_bit = Turtle(shape="square")
    new_snake_bit.color("white", "white")
    new_snake_bit.penup()
    new_snake_bit.goto(x=-i*20, y=0)
    snake.append(new_snake_bit)
screen.update()

game_is_on = True

move_forward(snake)
move_forward(snake)
move_forward(snake)
move_forward(snake)





screen.exitonclick()