from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_turtle(position)

    def add_turtle(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.setpos(position)
        self.turtles.append(turtle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            x_cor = self.turtles[num - 1].xcor()
            y_cor = self.turtles[num - 1].ycor()
            self.turtles[num].setpos(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)