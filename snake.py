from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.tails = []
        self.createSnake()
        self.head = self.tails[0]

    def createSnake(self):
        for i in POSITIONS:
            self.add_tail(i)

    def add_tail(self,position):
        tail = Turtle("square")
        tail.penup()
        tail.color('white')
        tail.goto(position)
        self.tails.append(tail)

    def extent_tail(self):
        self.add_tail(self.tails[-1].position())

    def move(self):
        for t in range(len(self.tails) - 1, 0, -1):
            new_x = self.tails[t - 1].xcor()
            new_y = self.tails[t - 1].ycor()
            self.tails[t].goto(new_x, new_y)
        self.head.forward(DISTANCE)
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

