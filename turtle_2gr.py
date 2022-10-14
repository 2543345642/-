import math
import turtle as t
t.speed ()
t.shape ("turtle")
"""		
walls_width = int(input("скажи ширину стенки"))
walls_height = int(input("скажи высоту стенки"))
walls_color = input("цвет стен HEX ну или англ буквами")
roof_height = int(input("скажи высоту крыши"))
roof_color = input("цвет крыши HEX ну или англ буквами")
door_width = int(input)
"""



walls_width = int(input("скажи ширину стенки"))
walls_height = int(input("скажи высоту стенки"))
walls_color = input("цвет стен HEX ну или англ буквами")
roof_height = int(input("скажи высоту крыши"))
roof_color = input("цвет крыши HEX ну или англ буквами")
door_width = (walls_width / 4)
door_height = (walls_height / 4)
door_color = input("цвет двери HEX ну или англ буквами")

roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))

t.fillcolor(walls_color)
t.begin_fill()
for i in range(2):
	t.fd(walls_width)
	t.right(90)
	t.fd(walls_height)
	t.right(90)
t.end_fill()

t.fillcolor(roof_color)
t.begin_fill()
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.setheading(180)
t.fd(walls_width)
t.end_fill()

t.fillcolor(door_color)
t.begin_fill()
t.left(90)
t.fd(walls_height)
t.left(90)
t.fd(walls_width / 2.5)
t.left(90)
t.fd(door_width)
t.right(90)
t.fd(door_height)
t.right(90)
t.fd(door_width)
t.end_fill()

t.done()






































t.done()