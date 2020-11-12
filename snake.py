INITIAL_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
HEADINGS = {
    "Up": 90,
    "Down": 270,
    "Left": 180,
    "Right": 0
}

from turtle import Turtle, Screen

class Snake:
    def __init__(self):

        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white", "white")
            new_segment.penup()
            new_segment.goto(position)
            self.body.append(new_segment)

    def follow_head(self):
        '''Get each bit of the snake except for the head to 
        go to the position of its preceding bit'''

        length = len(self.body)

        for segment in range(length-1, 0, -1):
            next_pos = self.body[segment-1].pos()
            self.body[segment].goto(next_pos)

    def move(self):
        self.follow_head()
        self.head.forward(MOVE_DISTANCE)

    def set_direction(self, direction):
        self.head.setheading(HEADINGS[direction])