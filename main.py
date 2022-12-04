import random
import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome To Snake World!")


screen.tracer(0)  # tracer Turns turtle animation on/off and set delay for update drawings


starting_position = [(0, 0), (-20, 0), (-40, 0)]
# segment1 = Turtle()
# segment1.color('white')
# segment1.shape('square')
#
# segment2 = Turtle()
# segment2.color('white')
# segment2.shape('square')
# segment2.goto(x=-20, y=0)
#
# segment3 = Turtle()
# segment3.color('white')
# segment3.shape('square')
# segment3.goto(x=-40, y=0)
# segments = []

# for position in starting_position:
#     new_segment = Turtle("square")
#     # new_segment.speed("slowest")
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
# # screen.update()
snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # for seg in segments:   # by this method if a turn is happened then segments got broken and only single segment
    #     seg.forward(20)              # gets turned other are moved forward

    # for segment in range(len(segments)-1, 0, -1):
    #     new_x = segments[segment - 1].xcor()
    #     new_y = segments[segment - 1].ycor()
    #     segments[segment].goto(x=new_x, y=new_y)
    #
    # segments[0].forward(20)
    # # segments[0].right(90)

screen.exitonclick()
