import os
import random
import math
import heapq
from PIL import Image, ImageFont, ImageDraw

MAX_LINE_DISTANCE = 100
MAX_DEPTH = 6
TURN_ANGLE = 0.43633

# These functions do math with tuples
def tuple_add(tuple1, tuple2):
	add = lambda x,y: x + y
	return map(add, tuple1, tuple2)

def tuple_sub(tuple1, tuple2):
	sub = lambda x,y: x - y
	return map(sub, tuple1, tuple2)

def tuple_mul(tuple1, scale):
	mul = lambda x: x * scale
	return map(mul, tuple1)

def tuple_div(tuple1, scale):
	div = lambda x: x / scale
	return map(div, tuple1)

# Implements algorithm based on digital differential analyzer algorithm
def dda_line(point1, point2):
	# List of pixels that will be built 
	line_pixels = []
	
	# Line to same point
	if point1 == point2: return []
	
	# Compute difference in pixels
	point_diff = tuple_sub(point2, point1)
	
	# Step in columns or rows
	if abs(point_diff[0]) > abs(point_diff[1]): i = 0
	else: i = 1

	# Difference in step is negative, swap points to make it positive
	if point_diff[i] < 0:
		point1, point2 = point2, point1

		point_diff = tuple_mul(point_diff, -1)

	slope = tuple_div(point_diff, point_diff[i])

	# To get first pixel on line
	init_diff = math.ceil(point1[i]) - point1[i]
	init_slope = tuple_mul(slope, init_diff)

	current_point = tuple_add(point1, init_slope)

	# Scan
	while (current_point[i] < point2[i]):	
		# Pixels stored as floats, rounding done when drawing
		point_to_draw = (int(current_point[0] + 0.5), int(current_point[1] + 0.5))
		line_pixels.append(point_to_draw)
		
		# Compute next pixel
		current_point = tuple_add(current_point, slope)

	return line_pixels

def draw_plant(draw, start, depth, angle):
	if depth >= MAX_DEPTH: return
	
	depth += 1
	length = MAX_LINE_DISTANCE / depth

	# Move forward
	start = draw_forward(draw, start, length, angle)

	# Split left
	draw_plant(draw, start, depth, angle + TURN_ANGLE)

	# Split
	draw_plant(draw, start, depth, angle)

	# Move forward
	start = draw_forward(draw, start, length, angle)

	# Split left
	draw_plant(draw, start, depth, angle + TURN_ANGLE)

	# Turn right
	angle -= TURN_ANGLE

	# Move forward
	start = draw_forward(draw, start, length, angle)

	# Split
	draw_plant(draw, start, depth, angle)

def draw_forward(draw, start, length, angle):
	end = (start[0] + length * math.cos(angle), 
		   start[1] + length * math.sin(angle))

	pixels = dda_line(start, end)
	for pixel in pixels:
		draw.point(pixel, (0, 255, 0, 255))
		
	return end

def main():
	# Canvas dimensions
	width = 1024
	height = 1024

	# Scale
	zoom = 64

	pixels = []
	heap = []

	# Setup canvas
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im = Image.new("RGB", (width, height))
	draw = ImageDraw.Draw(im)

	start = (100, 500)
	depth = 0
	angle = 0

	draw_plant(draw, start, depth, angle)

	im.save(dir_path + os.sep + "plant.png")

if __name__ == "__main__":
	main()