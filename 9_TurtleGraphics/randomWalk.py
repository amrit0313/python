import random
import turtle
from turtle import Turtle, Screen

tim =Turtle()

color = ["red", 'blue', 'purple', "brown", 'gray', 'green', 'violet', 'indigo',]
direction = [0, 90, 180, 270]
turtle.colormode(255)
tim.pensize(10)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return  random_color


for _ in range(200):
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()