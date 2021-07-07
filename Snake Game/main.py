from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snakenzia")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

level = screen.textinput("Level Selector", "1. Easy\n2. Hard")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()

    screen.onkey(key='Right', fun=snake.right)
    screen.onkey(key='Up', fun=snake.up)
    screen.onkey(key='Left', fun=snake.left)
    screen.onkey(key='Down', fun=snake.down)
    screen.onkey(key='e', fun=lambda: not game_on)


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if level == '1':
        if snake.head.xcor() > 280 or snake.head.xcor() < -280:
            new_x = -(snake.head.xcor())
            new_y = snake.head.ycor()
            snake.head.goto(new_x, new_y)
        elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
            new_x = snake.head.xcor()
            new_y = -(snake.head.ycor())
            snake.head.goto(new_x, new_y)

    if level == '2':
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            game_on = False


    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()