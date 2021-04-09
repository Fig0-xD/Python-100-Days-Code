import colorgram
import turtle
import random


def make_color_list():
    colors = colorgram.extract("painting.jpg", 50)

    color_list = []
    for color in colors:
        color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

    print(color_list)


def painting():
    color_list = [(132, 166, 205), (221, 148, 106),
                  (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
                  (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55),
                  (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
                  (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56),
                  (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

    turtle.colormode(255)

    my_turtle = turtle.Turtle()
    my_turtle.speed("fastest")
    my_turtle.hideturtle()

    my_turtle.penup()
    my_turtle.setpos(-250, -250)


    for __ in range(10):
        for _ in range(10):
            my_turtle.dot(15, random.choice(color_list))
            my_turtle.forward(50)

        my_turtle.setpos(-250.00, my_turtle.ycor() + 50)


    screen = turtle.Screen()
    screen.exitonclick()


if __name__ == '__main__':
    # make_color_list()
    painting()