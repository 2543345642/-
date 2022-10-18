import turtle as t
import random
t.shape("turtle")
t.speed(0)
t.colormode(255)

while True:
 	
	x = random.randint(-400, 400)
	print(x)
	y = random.randint(-200, 200)
	circles = random.randint(3, 5)
	radius = random.randint(20, 50)
	red = random.randint(0, 255)
	blue = random.randint(0, 255)
	green = random.randint(0, 255)
	t.penup()
	t.goto(x,y)

		
	for i in range(circles):
		t.fillcolor(red, green, blue)
		t.pendown()
		t.begin_fill()
		t.circle(radius)
		t.end_fill()
		t.penup()
		t.setheading(90)
		t.fd(radius * 2)
		t.setheading(0)
		radius /= 2
		if radius < 2:
			break

	


t.done()