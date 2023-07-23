from turtle import *

#creates a square function
def square(side_length):
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)

#iterates through a list called size
sizes = [210, 410, 610, 810, 10]
for size in sizes:
    square(size)
