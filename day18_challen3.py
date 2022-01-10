from turtle import Turtle,Screen

ex = Turtle()
ex.shape("turtle")
ex.color("red")
for i in range(3,100):
    angle = 360/i
    for j in range(i):
        ex.forward(50)
        ex.right(angle)


















# gọi ra screen là màn hình hiển thị
screen = Screen()
# click  sẽ thoát screen
screen.exitonclick()