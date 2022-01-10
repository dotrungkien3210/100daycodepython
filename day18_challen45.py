import turtle as t
from turtle import Turtle,Screen
import random
t.colormode(255)
tim = Turtle()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_col = (r,g,b)
    return  random_col

tim.speed("fastest")
tim.circle(100)
tim.shape("turtle")
tim.pencolor(random_color())

# gọi ra screen là màn hình hiển thị
screen = Screen()
# click  sẽ thoát screen
screen.exitonclick()