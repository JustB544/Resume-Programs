import turtle

size = 128


t = turtle.Turtle()
t.speed(10)
#creates a filled box s by s with bottom left corner being (x,y)
def box(x, y, s):
    t.penup()
    t.setpos(x, y)
    t.pendown
    t.begin_fill()
    for x in range(4):
        t.forward(s)
        t.left(90)
    t.end_fill()
#uses box() to create the rough shape of an arrow
def arrow(x, y, s):
    box(x, y+(2*s), s)
    box(x+(s), y+(3*s), s)
    box(x+(2*s), y+(4*s), s)
    box(x+(3*s), y+(3*s), s)
    box(x+(4*s), y+(2*s), s)
    box(x+(2*s), y+(3*s), s)
    box(x+(2*s), y+(2*s), s)
    box(x+(2*s), y+(s), s)
    box(x+(2*s), y, s)
#test
arrow(0, 0, 100)


