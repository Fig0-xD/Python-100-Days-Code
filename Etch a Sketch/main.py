import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()


def etch_a_sketch():

    screen.listen()
    screen.onkeypress(key="Up", fun=lambda: my_turtle.forward(10))
    screen.onkeypress(key="w", fun=lambda: my_turtle.forward(10))

    screen.onkeypress(key="Down", fun=lambda: my_turtle.backward(10))
    screen.onkeypress(key="s", fun=lambda: my_turtle.backward(10))

    screen.onkeypress(key="Left", fun=lambda: my_turtle.left(10))
    screen.onkeypress(key="a", fun=lambda: my_turtle.left(10))

    screen.onkeypress(key="Right", fun=lambda: my_turtle.right(10))
    screen.onkeypress(key="d", fun=lambda: my_turtle.right(10))

    screen.onkey(key="c", fun=screen.reset)

    screen.exitonclick()


if __name__ == '__main__':
    etch_a_sketch()
