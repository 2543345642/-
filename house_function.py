import math
import turtle as t
t.speed(0)
t.shape ("turtle")
"""
walls_width = int(input("скажи ширину стенки"))
walls_height = int(input("скажи высоту стенки"))
walls_color = input("цвет стен HEX ну или англ буквами")
roof_height = int(input("скажи высоту крыши"))
roof_color = input("цвет крыши HEX ну или англ буквами")
door_width = int(input)
"""
"""
    x - левый нижний угол стены
    y - левый нижний угол стены
    walls_width - ширина стен
    walls_height - выота стен
    walls
    """
door_x =
door_y = 0

def draw_house(walls_x, walls_y, walls_width, walls_height, walls_colors):
    draw_walls(walls_x, walls_y, walls_width, walls_height, walls_colors)
    draw_door(door_x, door_y, door_height, door_colors)
    draw_roof()


def draw_walls(walls_x, walls_y, walls_width, walls_height, walls_colors):
    t.penup()
    t.goto(walls_x, walls_y)
    t.pendown()
    t.fillcolor(walls_colors)
    t.begin_fill()
    for i in range(2):
        t.fd(walls_width)
        t.left(90)
        t.fd(walls_height)
        t.left(90)
    t.end_fill()



def draw_door(door_x, door_y, door_width, door_height, door_colors):
    t.penup()
    t.goto(door_x, door_y)
    t.pendown()
    t.fillcolor(door_colors)
    t.begin_fill()
    for i in range(2):
        t.fd(door_width)
        t.left(90)
        t.fd(door_height)
        t.left(90)
    t.end_fill()


def draw_roof():
    print("рисуем крышу")




draw_house(100, -200, 300, 100, "#ff0000", 80, 90, "#ff0000")

t.done()