# -*- coding: utf-8 -*-
import turtle
turtle.penup()
turtle.pencolor("red")
turtle.forward(-250)
turtle.pendown()
turtle.pensize(10)
turtle.right(45)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()