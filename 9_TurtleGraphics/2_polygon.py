from turtle import Turtle

tim = Turtle()
color = ["red", 'blue', 'purple', "brown", 'gray', 'green', 'violet', 'indigo',]
i = 3
for _ in range(3,11):
    tim.color(color[i-3])
    for _ in range(i):
        tim.forward(100)
        tim.left(360/i)
    i = i+1