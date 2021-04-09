import random
import turtle
from turtle import Turtle, Screen



def random_color():
    """
    :return: A random RGB value in a tuple
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b



def graphics():
    my_turtle = Turtle()
    # my_turtle.shape("turtle")

    turtle.colormode(255)

    # # -------------A SQUARE--------------
    # for _ in range(4):
    #     my_turtle.forward(100)
    #     my_turtle.left(90)
    #
    #
    # # --------------DASHED LINE------------
    # for _ in range(15):
    #     my_turtle.pendown()
    #     my_turtle.forward(10)
    #     my_turtle.penup()
    #     my_turtle.forward(10)
    #
    #
    # # -----------VARIOUS POLYGONS-----------
    # my_turtle.speed("fastest")
    # my_turtle.width(2)
    # for sides in range(3, 11):
    #     angle = 360 / sides
    #
    #     my_turtle.color(random_color())
    #
    #     for _ in range(sides):
    #         my_turtle.forward(100)
    #         my_turtle.left(angle)
    #
    #
    # # ------------RANDOM WALK------------
    # my_turtle.speed("fastest")
    # my_turtle.width(5)
    # for _ in range(100):
    #
    #     my_turtle.color(random_color())
    #
    #     angle = random.randrange(0, 360, 90)
    #
    #     my_turtle.forward(50)
    #     my_turtle.left(angle)
    #
    #
    # # ----------------SPIROGRAPH--------------
    # size = int(input("Provide the gap-size of the spirograph: "))
    # my_turtle.speed("fastest")
    # for angle in range(int(360 / size)):
    #
    #     my_turtle.color(random_color())
    #
    #     my_turtle.circle(100)
    #     my_turtle.setheading(my_turtle.heading() + size)



    screen = Screen()
    screen.exitonclick()


if __name__ == '__main__':
    graphics()
