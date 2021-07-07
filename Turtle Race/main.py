from turtle import Turtle, Screen
import random




def race():

    colors = ["red", "yellow", "green", "blue", "orange", "purple"]

    screen = Screen()
    screen.setup(height=400, width=600)

    race_on = False

    user_bet = screen.textinput(title="Bet", prompt="Which turtle will win? Enter a color: ")

    turtles = []


    y = -80

    for _ in range(6):
        turtle = Turtle("turtle")
        turtle.color(colors[_])
        turtle.penup()
        turtle.setpos(-280, y)
        y += 30

        turtles.append(turtle)

    if user_bet:
        race_on = True

    while race_on:

        for turtle in turtles:
            if turtle.xcor() > 280:
                race_on = False
                if user_bet == turtle.pencolor():
                    print(f"Congratulations!! You have won! The {turtle.pencolor()} turtle is the winner.")
                else:
                    print(f"Sorry, you have lost. The {turtle.pencolor()} turtle is the winner.")

            turtle.forward(random.randint(0, 10))




    screen.exitonclick()



if __name__ == '__main__':
    race()