from turtle import *


def square(side_length):
    for i in range(4):
        forward(side_length)
        left(90)
        #forward(side_length)

sizes = [20, 40, 60, 80, 100]
for size in sizes:
    square(size)

done()
