# tile_grid.py
# ------------
# By MWC Contributors
#
# Implements `draw_tile_grid`, which draws a grid of tiles. 

from turtle import *
from tile import fly

def draw_tile_grid(width, height, tile_size, tile_function):
    """Draws a (width x height) grid, with tile_function drawn on each tile.

    (Your explanation here.)
    """
    for y in range(height):
        for x in range(width):
            tile_function(tile_size)
            fly(tile_size)
        return_to_x_origin(tile_size, width)
        move_up_one_row(tile_size)
    return_to_y_origin(tile_size, height)

def return_to_x_origin(tile_size, width):
    "After drawing a row of tiles, returns the turtle to the starting x position"
    fly(-1 * tile_size * width)

def return_to_y_origin(tile_size, height):
    "After drawing all rows of tiles, returns the turtle to the starting y position"
    right(90)
    fly(tile_size * height)
    left(90)

def move_up_one_row(tile_size):
    "Moves the turtle up one row"
    left(90)
    fly(tile_size)
    right(90)





