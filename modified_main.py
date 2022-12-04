import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome To Snake World!")


screen.tracer(0)  # tracer Turns turtle animation on/off and set delay for update drawings

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # detecting collision with food by turtle.distance() method
    if snake.head.distance(food) < 15:
        # since food have size 10*10 and head have 20*20 so 5+10=15 gives collision of their outer body
        # print("nom, nom, nom")
        food.refresh()
        snake.extend_tail()

        score_board.increase_score()
        score_board.display_score()

        # add tail
        snake.extend_tail()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        score_board.reset()
        snake.reset()

    # Detect collision with tail,
        # trigger game over sequence
    # for segment in snake.segments:  # use -> snake.segments[1::]
    #     if segment == snake.head:
    #         pass
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score_board.reset()
            snake.reset()


screen.exitonclick()
