from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(30)

def move_backwards():
    tim.backward(30)

def move_left():
    tim.left(90)
    tim.forward(30)    

def move_right():
    tim.right(90)
    tim.forward(30)

def clear():
    tim.clear()
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(clear, "c")


screen.exitonclick()