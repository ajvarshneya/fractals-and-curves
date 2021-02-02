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
CANVAS_WIDTH = 2560
CANVAS_HEIGHT = 1440

RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
CYAN = (0, 255, 255, 255)

START_POINT = (CANVAS_HEIGHT, CANVAS_HEIGHT)
START_ANGLE = math.radians(270) 
START_DEPTH = 0

MAX_DEPTH = 6
MAX_LINE_LENGTH = CANVAS_WIDTH / MAX_DEPTH
START_COLOR = CYAN
END_COLOR = BLUE
TURN_ANGLE = math.radians(90)

OUTFILE = "plantish.png"

# Draws a plant
def draw_plant(draw, start, depth, angle):
	if depth >= MAX_DEPTH: return
	depth += 1
	length = MAX_LINE_LENGTH / depth
	
	# Recursive pattern
	start = plantish_draw_forward(draw, start, angle, length)
	draw_plant(draw, start, depth, angle + TURN_ANGLE)
	draw_plant(draw, start, depth, angle)
	start = plantish_draw_forward(draw, start, angle, length)
	draw_plant(draw, start, depth, angle + TURN_ANGLE)
	angle -= TURN_ANGLE
	start = plantish_draw_forward(draw, start, angle, length)
	draw_plant(draw, start, depth, angle)

def get_color(start_color, end_color, i, max):
	r_diff = end_color[0] - start_color[0] * i // max
	g_diff = end_color[1] - start_color[1] * i // max
	b_diff = end_color[2] - start_color[2] * i // max
	a_diff = end_color[3] - start_color[3] * i // max

	color = (
		start_color[0] + r_diff,
		start_color[1] + g_diff,
		start_color[2] + b_diff,
		start_color[3] + a_diff,
	)

	return color

# Draws a line of length at angle from start coordinate 
def plantish_draw_forward(draw, start, angle, length):
	
	# Compute coordinate to draw from start to 
	end = (start[0] + length * math.cos(angle), 
	       start[1] + length * math.sin(angle))
	
	# Get pixels on line from start to end, then write to canvas	
	pixels = dda_line(start, end)
	for i, pixel in enumerate(pixels):
		color = get_color(START_COLOR, END_COLOR, i, len(pixels))
		draw.point(pixel, color)
		
	return end

def main():
	# Setup canvas
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT))
	draw = ImageDraw.Draw(im)
	
	# Draw the plant
	draw_plant(draw, START_POINT, START_DEPTH, START_ANGLE)
	
	# draw_square(draw, (START_POINT[0]-50,START_POINT[1]-50), 50, RED)

	filename = dir_path + os.sep + OUTFILE
	im.save(filename)

if __name__ == "__main__":
	main()


