from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
score = ScoreBoard()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_postion()
        score.increase_score()
        snake.extent_tail()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()
        score.reset()
    for part in snake.tails[1:]:
        # if part == snake.head:
        #     pass
        # elif snake.head.distance(part) < 10:
        #     is_game_on = False
        #     score.game_over()
        if snake.head.distance(part) < 10:
            is_game_on = False
            score.game_over()
            score.reset()

screen.exitonclick()
