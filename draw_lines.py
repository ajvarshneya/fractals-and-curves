#
# draw_lines.py
#
# A.J. Varshneya
# ajvarshneya@gmail.com
#
# Functions used to compute pixel lines and draw to canvas.
#

import math
from utilities import *

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

# Draws a line of length at angle from start coordinate 
def draw_forward(draw, start, angle, length, color):
	
	# Compute coordinate to draw from start to 
	end = (start[0] + length * math.cos(angle), 
	       start[1] + length * math.sin(angle))
	
	# Get pixels on line from start to end, then write to canvas	
	pixels = dda_line(start, end)
	for pixel in pixels:
		draw.point(pixel, color) 
		
	return end



