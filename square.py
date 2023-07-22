from turtle import *

def square(side_length):
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)

sizes = [20, 40, 60, 80, 100]
for size in sizes:
    square(size)

