#
# koch.py
#
# A.J. Varshneya
# ajvarshneya@gmail.com
#
# Python implementation of koch snowflake fractal.
#

import os
import random
import math
from PIL import Image, ImageFont, ImageDraw

from utilities import *
from draw_lines import *

# Constants
CANVAS_WIDTH = 2048
CANVAS_HEIGHT = 2048

START_POINT = (500, 800)
START_ANGLE = 0
START_DEPTH = 0

MAX_DEPTH = 7
LINE_LENGTH = 1
LINE_COLOR = (0, 255, 0, 255)
TURN_ANGLE = math.radians(60)

OUTFILE = "koch.png"

# Draws one edge of a koch snowflake
def draw_koch(draw, start, depth, angle):
	if depth >= MAX_DEPTH: return (start, angle)
	depth += 1
	
	# Koch pattern
	start = draw_forward(draw, start, angle, LINE_LENGTH, LINE_COLOR)
	(start, angle) = draw_koch(draw, start, depth, angle)
	angle -= TURN_ANGLE
	(start, angle) = draw_koch(draw, start, depth, angle)
	angle += TURN_ANGLE
	angle += TURN_ANGLE
	(start, angle) = draw_koch(draw, start, depth, angle)
	angle -= TURN_ANGLE
	(start, angle) = draw_koch(draw, start, depth, angle)

	return (start, angle)

def main():
	# Setup canvas
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im = Image.new("RGB", (width, height))
	draw = ImageDraw.Draw(im)
	
	# Draw the snowflake
	(start, angle) = draw_koch(draw, START_POINT, START_DEPTH, START_ANGLE)
	angle += TURN_ANGLE
	angle += TURN_ANGLE
	(start, angle) = draw_koch(draw, start, START_DEPTH, angle)
	angle += TURN_ANGLE
	angle += TURN_ANGLE
	(start, angle) = draw_koch(draw, start, START_DEPTH, angle)

	im.save(dir_path + os.sep + OUTFILE)

if __name__ == "__main__":
	main()


