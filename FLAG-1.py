# CREATING INDIAN FLAG

from turtle import *
t=Turtle()
t.speed(4)   #increasing the turtle speed
t.pensize(5)#increasing the pensize
t.up()
t.goto(0,-300)
t.down()
t.goto(0,400)


def flag(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
flag("orange")  #creating the orange triangle

t.goto(0,300)#creating the white
flag("white")#triangle

t.goto(0,200)# creating the green
flag("green")# triangle

t.forward(200)     #1.
t.begin_fill()     #  from no-1 to no-2
t.fillcolor("blue")#  we are creating the circle of the
t.circle(50)       #  ASHOKE CHAKRA.
t.end_fill()       #
t.left(90)         #
t.up()             #
t.forward(50)      #
t.right(90)        #
t.down()           #2.

for i in range(24):# INSIDE THE ASHOKE CHARKA
    t.forward(45)  # THE BLACK STRAIGHT LINE PART WE
    t.backward(45) # ARE CREATING
    t.left(15)     #

t.up()                  #  from this to last
t.home()                #  we have made just to
t.goto(0,-300)          #  creat the base of
t.down()                #  the INDIAN FLAG.
t.begin_fill()          #
t.fillcolor("black")    #
t.forward(200)          #
t.right(90)             #
t.forward(50)           #
t.right(90)             #
t.forward(400)          #
t.right(90)             #
t.forward(50)           #
t.right(90)             #
t.forward(200)          #
t.end_fill()            #
t.hideturtle()          #
