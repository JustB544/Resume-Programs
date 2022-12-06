import turtle

angFormula = str(input("Input curve. "))
powerTower = []
check = 1
number = 0
prevPower = 0

#change precision and size to change the output
#precision: lowers change in x for polynomial
#size: change the left number to change the movement per tick
precision = 5
size = 1/precision

times = 360*precision
rol = 1
ang = 0
t = turtle.Turtle()
t.speed(100)
#translates input from a*x^n+b*x^n... to polynomial
for x in angFormula:
    number += 1
    if check == 1 and x != "x" and x != "+" and x != "-":
        if prevPower < int(angFormula[number+2]):
            powerTower.append(rol*int(x))
            prevPower = int(angFormula[number+2])
            check = 0
        elif prevPower - 1 == int(angFormula[number+2]):
            powerTower.append(rol*int(x))
            prevPower = int(angFormula[number+2])
            check = 0
        else:
            while prevPower - 1 != int(angFormula[number+2]):
                powerTower.append(0)
                prevPower -= 1
            powerTower.append(rol*int(x))
            prevPower = int(angFormula[number+2])
            check = 0
    elif check == 1 and x == "x":
        if prevPower < int(angFormula[number+1]):
            powerTower.append(rol)
            prevPower = int(angFormula[number+1])
            check = 0
        elif prevPower - 1 == int(angFormula[number+1]):
            powerTower.append(rol)
            prevPower = int(angFormula[number+1])
            check = 0
        else:
            while prevPower - 1 != int(angFormula[number+1]):
                powerTower.append(0)
                prevPower -= 1
            powerTower.append(rol)
            prevPower = int(angFormula[number+1])
            check = 0
    elif x == "+" or x == "-":
        check = 1
        if x == "-": 
            rol = -1
        else:
            rol = 1
if prevPower != 0:
    while prevPower != 0:
        powerTower.append(0)
        prevPower -= 1
t.penup()
number = -2
t.setpos(0, 0)
t.pendown()
#takes polynomial and makes that the rotation per movement (creates beautiful pictures after a long time)
for x in range(times):
    number -= 1/precision
    ang = 0
    for x in powerTower:
        ang += x*(number**(len(powerTower)-1))
    t.setheading(0)
    t.left(ang)
    t.forward(size)
t.penup()
number = 2
t.setpos(0,0)
t.pendown()
for x in range(times):
    number += 1/precision
    ang = 0
    for x in powerTower:
        ang += x*(number**(len(powerTower)-1))
    t.setheading(180)
    t.left(ang)
    t.forward(size)
