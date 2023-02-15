import turtle
from turtle import Screen
import random


# I used the colorgram module to extract RGB colors from the 'image.jpg' (Damien Hirst painting)

turtle.colormode(255)
tim = turtle.Turtle()
color_list = [(58, 107, 147), (225, 201, 110), (133, 83, 59), (222, 137, 62), (235, 226, 204), (195, 146, 171), (223, 233, 229), (144, 179, 203),
              (138, 82, 105), (207, 91, 70)]

tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()


def left_turn():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)


def right_turn():
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)


def forward_march():
    for i in range(10):
        tim.dot(30, random.choice(color_list))
        tim.forward(50)


for _ in range(5):
    forward_march()
    left_turn()
    forward_march()
    right_turn()

screen = Screen()
screen.exitonclick()
