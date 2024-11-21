import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
for _ in range (4):
    for _ in range(50):
        tim.pendown()
        tim.forward(2)
        tim.penup()
        tim.forward(2)
    tim.left(90)








screen = Screen()
screen.exitonclick()