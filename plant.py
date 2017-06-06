#
# plant.py
#
# A.J. Varshneya
# ajvarshneya@gmail.com
#
# Python implementation of a plant drawn recursively.
#

import os
import random
import math
from PIL import Image, ImageFont, ImageDraw

from utilities import *
from draw_lines import *

# Constants
CANVAS_WIDTH = 1024
CANVAS_HEIGHT = 1024

START_POINT = (100, 500)
START_ANGLE = math.radians(0) 
START_DEPTH = 0

MAX_DEPTH = 6
MAX_LINE_LENGTH = 100
LINE_COLOR = (0, 255, 0, 255)
TURN_ANGLE = math.radians(25)

OUTFILE = "plant.png"

# Draws a plant
def draw_plant(draw, start, depth, angle):
	if depth >= MAX_DEPTH: return
	depth += 1
	length = MAX_LINE_LENGTH / depth
	
	# Recursive pattern
	start = draw_forward(draw, start, angle, length, LINE_COLOR)
	draw_plant(draw, start, depth, angle + TURN_ANGLE)
	draw_plant(draw, start, depth, angle)
	start = draw_forward(draw, start, angle, length, LINE_COLOR)
	draw_plant(draw, start, depth, angle + TURN_ANGLE)
	angle -= TURN_ANGLE
	start = draw_forward(draw, start, angle, length, LINE_COLOR)
	draw_plant(draw, start, depth, angle)

def main():
	# Setup canvas
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT))
	draw = ImageDraw.Draw(im)
	
	# Draw the plant
	draw_plant(draw, START_POINT, START_DEPTH, START_ANGLE)

	im.save(dir_path + os.sep + OUTFILE)

if __name__ == "__main__":
	main()


