import turtle

akna_pind = turtle.Screen()
kilpkonn = turtle.Turtle()


kylgi_joonistatud = 0


while kylgi_joonistatud < 4:
    kilpkonn.forward(100)
    kilpkonn.left(90)
    kylgi_joonistatud = kylgi_joonistatud + 1

akna_pind.exitonclick()
