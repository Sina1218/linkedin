#python
from turtle import*
import turtle
t=turtle.Turtle()
t.speed(9)
t.getscreen().bgcolor("blue")
def box ():
    t.fillcolor('black')
turtle.bgcolor("black")
turtle.title('Linkedin Logo')
#BOX
t.pencolor("black")


t.left(90)
t.forward(200)
t.right(90)
t.forward(100)
t.pencolor("#104E8B")
t.begin_fill()
t.fillcolor('#104E8B')
s = 360
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
    
t.forward(180)
s = 270
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(200)
s = 180
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(180)
s = 90
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
t.forward(200)    
t.end_fill()

t.begin_fill()
t.pencolor("#104E8B")
t.right(90)
#i
t.forward(75)
t.right(90)
t.forward(210)
t.end_fill()
#fillcolor
t.pencolor("#F8F8FF")
t.begin_fill()
t.fillcolor("#F8F8FF")
#line1
t.left(90)
t.forward(160)
#line2
t.left(90)
t.forward(30)
#line3
t.left(90)
t.forward(160)
#line4
t.left(90)
t.forward(30)
t.end_fill()

#circle line
t.begin_fill()
t.pencolor("#104E8B")
t.fillcolor("#104E8B")
t.right(90)
t.forward(15)
t.right(90)
t.forward(15)
t.end_fill()
#cicle
t.begin_fill()
t.pencolor("#F8F8FF")
t.fillcolor("#F8F8FF")
t.circle(20, 360)
t.end_fill()

#n lines
t.begin_fill()
t.pencolor("#104E8B")
t.fillcolor("")
#line1
t.right(90)
t.forward(14.9)
#line2
t.left(90)
t.forward(50)
t.backward(65)
t.forward(65)
t.end_fill()
# #line n
t.begin_fill()
t.pencolor("#F8F8FF")
t.fillcolor("#F8F8FF")
t.right(90)
t.forward(160)
t.end_fill()
#line1
t.begin_fill()
t.pencolor("#F8F8FF")
t.fillcolor("#F8F8FF")
t.left(90)
t.forward(30)
#line2
t.left(90)
t.forward(160)
#line3
t.left(90)
t.forward(30)
t.end_fill()
t.backward(30)
#line circle
t.left(90)
t.forward(70)
#line2
t.left(90)
t.forward(-14)
t.left(90)
#line circle
t.begin_fill()
t.pencolor("#F8F8FF")
t.fillcolor("#F8F8FF")
t.circle(-65,180)

#line1
t.forward(90)
t.right(90)
t.forward(25)

#line2
t.right(90)
t.forward(80)


t.circle(45 , 180)
t.end_fill()
t.right(90)
t.forward(10)
mainloop()
