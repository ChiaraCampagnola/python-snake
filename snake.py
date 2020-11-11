from turtle import Turtle, Screen

class Snake:
    def __init__(self):

        self.snake = []

        for i in range(3):
            new_snake_bit = Turtle(shape="square")
            new_snake_bit.color("white", "white")
            new_snake_bit.penup()
            new_snake_bit.goto(x=-i*20, y=0)
            self.snake.append(new_snake_bit)

    def move_forward(self):
        length = len(self.snake)
        for bit in range(length-1, 0, -1):
            next_pos = self.snake[bit-1].pos()
            self.snake[bit].goto(next_pos)
        self.snake[0].forward(20)