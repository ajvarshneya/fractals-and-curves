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
import random
import time
from PIL import Image, ImageFont, ImageDraw

from utilities import *
from draw_lines import *

# Constants
CANVAS_WIDTH = 2560
CANVAS_HEIGHT = 1440
FOREST_GREEN = (58, 95, 11, 255)

START_POINT = (CANVAS_HEIGHT, CANVAS_HEIGHT)
START_ANGLE = math.radians(270) 
START_DEPTH = 0

MAX_DEPTH = 10
MAX_LINE_LENGTH = 200
LINE_COLOR = FOREST_GREEN
TURN_ANGLE_MIN = 10
TURN_ANGLE_MAX = 30
BRANCH_CHANCE = 0.40

OUTFILE = "plant_stochastic.png"

# Draws a plant
def draw_plant(im, draw, start, depth, angle, color):
	if depth >= MAX_DEPTH: return
	if random.random() > BRANCH_CHANCE: return

	depth += 1
	length = MAX_LINE_LENGTH / depth
	
	# Recursive pattern
	turn_angle = math.radians(random.randint(TURN_ANGLE_MIN, TURN_ANGLE_MAX))
	start = draw_forward_refresh(im, draw, start, angle, length, color)
	draw_plant(im, draw, start, depth, angle + turn_angle, color)
	draw_plant(im, draw, start, depth, angle, color)
	start = draw_forward_refresh(im, draw, start, angle, length, color)
	draw_plant(im, draw, start, depth, angle + turn_angle, color)
	angle -= turn_angle
	start = draw_forward_refresh(im, draw, start, angle, length, color)
	draw_plant(im, draw, start, depth, angle, color)

# Draws a line of length at angle from start coordinate 
def draw_forward_refresh(im, draw, start, angle, length, color):
	
	# Compute coordinate to draw from start to 
	end = (start[0] + length * math.cos(angle), 
	       start[1] + length * math.sin(angle))
	
	# Get pixels on line from start to end, then write to canvas	
	pixels = dda_line(start, end)
	for pixel in pixels:
		draw.point(pixel, color) 
		
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im.save(dir_path + os.sep + OUTFILE)
	time.sleep(0.05)
	return end

def main():
	# Setup canvas
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT))
	draw = ImageDraw.Draw(im)
	
	# Draw the plant
	draw_plant(im, draw, START_POINT, START_DEPTH, START_ANGLE, LINE_COLOR)

	im.save(dir_path + os.sep + OUTFILE)

if __name__ == "__main__":
	main()


