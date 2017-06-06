#
# dragon.py
#
# A.J. Varshneya
# ajvarshneya@gmail.com
#
# Python implementation of dragon curve fractal.
#

import os
import random
import math
from PIL import Image, ImageFont, ImageDraw

from utilities import *
from draw_lines import *

# Constants
CANVAS_WIDTH = 4096
CANVAS_HEIGHT = 4096

START_POINT = (2048, 2048)
START_ANGLE = math.radians(90) 
START_DEPTH = 0

MAX_DEPTH = 21 
LINE_LENGTH = 3
LINE_COLOR = (0, 255, 0, 255)
TURN_ANGLE = math.radians(90)

OUTFILE = "dragon.png"

# X-state function
def draw_dragon_x(draw, start, depth, angle):
	if depth >= MAX_DEPTH: return (start, angle)
	depth += 1
	
	# Recursive pattern (based on L-system)
	(start, angle) = draw_dragon_x(draw, start, depth, angle)
	angle += TURN_ANGLE
	(start, angle) = draw_dragon_y(draw, start, depth, angle)
	start = draw_forward(draw, start, angle, LINE_LENGTH, LINE_COLOR)
	angle += TURN_ANGLE

	return (start, angle)

# Y-state function
def draw_dragon_y(draw, start, depth, angle):
	if depth >= MAX_DEPTH: return (start, angle)
	depth += 1
	
	# Recursive pattern (based on L-system)
	angle -= TURN_ANGLE
	start = draw_forward(draw, start, angle, LINE_LENGTH, LINE_COLOR)
	(start, angle) = draw_dragon_x(draw, start, depth, angle)
	angle -= TURN_ANGLE
	(start, angle) = draw_dragon_y(draw, start, depth, angle)

	return (start, angle)

def main():
	# Setup canvas
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT))
	draw = ImageDraw.Draw(im)

	# Draw the dragon
	start = draw_forward(draw, START_POINT, START_ANGLE, LINE_LENGTH, LINE_COLOR)
	draw_dragon_x(draw, start, START_DEPTH, START_ANGLE)

	im.save(dir_path + os.sep + OUTFILE)

if __name__ == "__main__":
	main()


