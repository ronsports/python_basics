import turtle

turtle.speed(3)
while True:
    turtle.right(100)
    turtle.left(90)
    turtle.forward(20)
    if turtle.xcor() == 0 and turtle.ycor() == 0:
        break

turtle.exitonclick()