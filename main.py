from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("midnightblue")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    #for seg in segments:
    #    seg.forward(20)
    snake.move()


screen.exitonclick()