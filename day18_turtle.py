from turtle import Turtle, Screen
# tạo một đối tượng turtle
turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
"""turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)"""
for _ in range(15):
    turtle.color("green")
    turtle.forward(10)
    turtle.color("yellow")
    turtle.penup()
    turtle.color("red")
    turtle.forward(10)
    turtle.color("green")
    turtle.pendown()
    turtle.color("yellow")





















# gọi ra screen là màn hình hiển thị
screen = Screen()
# click  sẽ thoát screen
screen.exitonclick()