from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_body(position)

    def add_body(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    # adds new segment to the snake
    def extend(self):
        self.add_body(self.segments[-1].position())

    # controls
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
