from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADINGS = {
    "Up": 90,
    "Down": 270,
    "Left": 180,
    "Right": 0
}

OPPOSITE_DIRECTIONS = {
    90: 270,
    270: 90,
    180: 0,
    0: 180
}

class Snake:
    ''' Controls everything to do with the snake'''
    def __init__(self):
        self.create_snake()


    def create_snake(self):
        ''' Creates a snake made of three segments '''
        self.body = []
        for position in INITIAL_POSITIONS:
            self.add_segment(position)
        self.head = self.body[0]
        self.tail = self.body[1:]


    def add_segment(self, position):
        ''' Adds one segment at a specified position on the screen '''
        new_segment = Turtle(shape="square")
        new_segment.color("white", "white")
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        ''' Adds a segment to the tail of the snake '''
        last_position = self.body[-1].position()
        self.add_segment(last_position)
        self.tail = self.body[1:]

    def delete_snake(self):
        ''' Clears the drawing of the dead snake and deletes all
        objects related to it '''
        for segment in self.body:
            segment.reset()
            del segment
        del self.body

    def follow_head(self):
        '''Gets each bit of the snake except for the head to
        go to the position of its preceding bit'''

        length = len(self.body)

        for segment in range(length-1, 0, -1):
            next_pos = self.body[segment-1].pos()
            self.body[segment].goto(next_pos)

    def move(self):
        ''' Moves the snake forward '''
        self.follow_head()
        self.head.forward(MOVE_DISTANCE)

    def set_direction(self, direction):
        ''' Changes the direction of the snake
        based on user input '''
        direction = HEADINGS[direction] # Get direction in degrees from string

        if direction == OPPOSITE_DIRECTIONS[self.head.heading()]:
            # If user is trying to go the opposite way as the current direction
            # (eg snake is going up and user tries to go down) do nothing as it's not allowed
            return

        self.head.setheading(direction)
        