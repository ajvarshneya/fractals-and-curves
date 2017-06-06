#
# sierpinsky.py
#
# A.J. Varshneya
# ajvarshneya@gmail.com
#
# Python implementation of sierpinsky triangle fractal.
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

START_POINT = (512, 512)
START_DEPTH = 0
START_ANGLE = math.radians(90)

LINE_LENGTH = 1
LINE_COLOR = (0, 255, 0, 255)
MAX_DEPTH = 10
TURN_ANGLE = math.radians(60)

OUTFILE = "sierpinsky.png"

# A-state function
def draw_sierpinsky_a(draw, start, depth, angle):
	if depth >= MAX_DEPTH: return (start, angle)
	depth += 1
	
	# Recursive pattern (based on L-system)
	start = draw_forward(draw, start, angle, LINE_LENGTH, LINE_COLOR)
	angle -= TURN_ANGLE
	(start, angle) = draw_sierpinsky_b(draw, start, depth, angle)
	angle += TURN_ANGLE
	(start, angle) = draw_sierpinsky_a(draw, start, depth, angle)
	angle += TURN_ANGLE
	(start, angle) = draw_sierpinsky_b(draw, start, depth, angle)
	angle -= TURN_ANGLE

	return (start, angle)

# B-state function
def draw_sierpinsky_b(draw, start, depth, angle):
	if depth >= MAX_DEPTH: return (start, angle)
	depth += 1
	
	# Recursive pattern (based on L-system)
	start = draw_forward(draw, start, angle, LINE_LENGTH, LINE_COLOR)
	angle += TURN_ANGLE
	(start, angle) = draw_sierpinsky_a(draw, start, depth, angle)
	angle -= TURN_ANGLE
	(start, angle) = draw_sierpinsky_b(draw, start, depth, angle)
	angle -= TURN_ANGLE
	(start, angle) = draw_sierpinsky_a(draw, start, depth, angle)
	angle += TURN_ANGLE

	return (start, angle)

def main():
	# Setup canvas
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT))
	draw = ImageDraw.Draw(im)
	
	# Draw the triangle
	start = draw_forward(draw, START_POINT, START_ANGLE, LINE_LENGTH, LINE_COLOR)
	draw_sierpinsky_a(draw, start, START_DEPTH, START_ANGLE)

	im.save(dir_path + os.sep + OUTFILE)

if __name__ == "__main__":
	main()



