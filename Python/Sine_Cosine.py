#Breyton Pabst
#9/23/20
#creates sine and cosine waves
#created for programming class
import turtle
import math

def sineWave(t, c, s, T, x, y):
	#t is turtle, c is color, s is scale, T is how many waves, x is setpos x coord, and y is setpos y coord
	t.penup()
	t.setpos(x, y)
	t.color(c)
	t.pendown()
	p1 = 0
	times = int(math.ceil(T*90))
	for x in range(times):
		p2 = 45*s*math.sin(4*(x+1)*(math.pi/180))
		ang = math.degrees(math.atan((p2-p1)/abs(s)))
		len = math.sqrt((p2-p1)**2 + s**2)
		t.setheading(0)
		t.left(ang)
		t.forward(len)
		p1 = p2
def cosWave(t, c, s, T, x, y):
	#t is turtle, c is color, s is scale, T is how many waves, x is setpos x coord, and y is setpos y coord
	t.penup()
	t.setpos(x, y + s*45)
	t.color(c)
	t.pendown()
	p1 = 45*s
	times = int(math.ceil(T*90))
	for x in range(times):
		p2 = 45*s*math.cos(4*(x+1)*(math.pi/180))
		ang = math.degrees(math.atan((p2-p1)/abs(s)))
		len = math.sqrt((p2-p1)**2 + s**2)
		t.setheading(0)
		t.left(ang)
		t.forward(len)
		p1 = p2
def main():
	turt = turtle.Turtle()
	turt.speed(100)
	
	sineWave(turt, "royal blue", 5, 4, -960, 0)
	cosWave(turt, "royal blue", 5, 4, -960, 0)
main()
