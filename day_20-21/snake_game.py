from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreBoard import Score

# screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.mode("standard")

# snake
snake = Snake()

# food
food = Food()

# scoreboard
scoreboard = Score()

# key controls
screen.listen()
screen.onkey(fun=snake.move_north, key="Up")
screen.onkey(fun=snake.move_west, key="Left")
screen.onkey(fun=snake.move_east, key="Right")
screen.onkey(fun=snake.move_south, key="Down")


# snake game
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



# exit
screen.exitonclick()
