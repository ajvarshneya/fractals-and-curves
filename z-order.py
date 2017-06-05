import os
import random
import math
import heapq
from PIL import Image, ImageFont, ImageDraw

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

# Splice bits of two numbers, return corresponding integer
def splice(x, y):
	bin_x = '{:032b}'.format(x)
	bin_y = '{:032b}'.format(y)
	spliced = "".join(i for tup in zip(bin_y, bin_x) for i in tup)
	return int(spliced, 2)

def unsplice(n):
	bin_n = '{:064b}'.format(n)
	bin_y = bin_n[0::2]
	bin_x = bin_n[1::2]

	return (int(bin_x, 2), int(bin_y, 2))

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

	# Try to draw z-order curve
	for x in range(0, width, zoom):
		for y in range(0, height, zoom):
			heapq.heappush(heap, (splice(x//zoom, y//zoom), (float(x), float(y))))


	# Get pixels of line between last point and next point on curve for every point on curve
	cur = heapq.heappop(heap)[1]
	last = cur
	while heap:
		cur = heapq.heappop(heap)[1]
		pixels += dda_line(last, cur)
		last = cur

	# Draw the pixels
	for pixel in pixels:
		draw.point(pixel, (255, 0, 0, 255))

	im.save(dir_path + os.sep + "z-order.png")

if __name__ == "__main__":
	main()