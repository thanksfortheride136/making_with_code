from turtle import *

def draw_tile(size):
    "Draws one tile, which can be repeated to form a pattern."
    draw_tile_outline(size)
    draw_squiggle(size)

def draw_tile_outline(size):
    pencolor("#dddddd")
    square(size)

def draw_squiggle(size):
    forward(size/4)
    pencolor("black")
    left(90)
    quarter_arc_right(size/4)
    quarter_arc_left(size/4)
    quarter_arc_left(size/4)
    quarter_arc_right(size/4)
    left(90)
    fly(size/4)
    left(90)
    fly(size)
    left(90)

def fly(distance):
    "Moves without drawing."
    penup()
    forward(distance)
    pendown()

def square(size):
    "Draws a square of side length `size`"
    for side in range(4):
        forward(size)
        left(90)

def quarter_arc_right(radius):
    "Draws a quarter of an arc, turning to the right."
    circle(-radius, 90)

def quarter_arc_left(radius):
    "Draws a quarter of an arc, turning to the left."
    circle(radius, 90)
