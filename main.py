from turtle import *
import random

is_race_on = False
screen = Screen()

color = "grey"
screen.bgcolor(color)

screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")

colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-180, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


def display_game_over():
    write("Game Over", align="center", font=("Courier", 24, "normal"))


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            display_game_over()
            is_race_on = False
            winning_color =turtle.pencolor()
            if winning_color == user_bet:
                
                print(f"You've won! The {winning_color} turtle is the winner!")
                
            else:
                print(f"You've loose! The {winning_color} turtle is the winner!")


        rand_distances = random.randint(0, 10)
        turtle.forward(rand_distances)


screen.exitonclick()

