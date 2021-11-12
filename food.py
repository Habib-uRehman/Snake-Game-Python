from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.new_postion()

    def new_postion(self):
        x_position = random.randint(-280, 230)
        y_position = random.randint(-280, 230)
        self.goto(x_position, y_position)
