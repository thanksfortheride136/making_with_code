# drawtiles.py
# ------------
# By MWC Contributors
#
# Provides a command-line interface for drawing a grid of tiles.
# Run `python drawtiles.py --help` for usage instructions.

from tile import draw_tile
from tile_grid import draw_tile_grid
from superturtle.movement import no_delay
from argparse import ArgumentParser

parser = ArgumentParser("python drawtiles.py", description="Draws a grid of tiles.")
parser.add_argument("width", type=int, help="How many tiles across the grid should be")
parser.add_argument("height", type=int, help="How many tiles high the grid should be")
parser.add_argument("size", type=int, help="Side length of each tile")
parser.add_argument("--fast", action="store_true", help="Skip turtle animation and show the result")
args = parser.parse_args()

if args.fast:
    with no_delay():
        draw_tile_grid(args.width, args.height, args.size, draw_tile)
else:
    draw_tile_grid(args.width, args.height, args.size, draw_tile)
input()

