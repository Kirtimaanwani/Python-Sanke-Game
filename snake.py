from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0



class Snake:
    def __init__(self):
        """
        initialize a list of snake segments
        """

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # creates a head of snake

    def create_snake(self):
        """
        creates a snake of three segments
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """creates a segment of snake"""
        new_segment = Turtle("square")
        # new_segment.speed("slowest")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """
        resets the snake segments
        """
        for segment in self.segments:
            segment.goto(1000, 1000)   # before clearing all segments it sends all turtle of segments to a location
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_tail(self):
        """
        adds a tail of turtle to current snake
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        moves snake segments forward by 20 ,
        note: segments are connected to each other
        """
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x=new_x, y=new_y)

        self.head.forward(20)   # head moving forward with 20 paces

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)            
