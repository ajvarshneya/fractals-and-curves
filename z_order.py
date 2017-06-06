#
# z_order.py
#
# A.J. Varshneya
# ajvarshneya@gmail.com
#
# Python implementation of z_order curve.
#

import heapq
import math
import os
import random
from PIL import Image, ImageFont, ImageDraw

from utilities import *
from draw_lines import *

# Constants
CANVAS_WIDTH = 1024
CANVAS_HEIGHT = 1024
ZOOM = 16 

LINE_COLOR = (255, 0, 0, 255)
OUTFILE = "z_order.png"

# Splice bits of two integers into one integer
def splice(x, y):
	bin_x = '{:032b}'.format(x)
	bin_y = '{:032b}'.format(y)
	spliced = "".join(i for tup in zip(bin_y, bin_x) for i in tup)
	return int(spliced, 2)

# Unsplice bits of integer into two integers 
def unsplice(n):
	bin_n = '{:064b}'.format(n)
	bin_y = bin_n[0::2]
	bin_x = bin_n[1::2]
	return (int(bin_x, 2), int(bin_y, 2))

def draw_z_order(draw):
	
	# Iterate over coordinates and add them to heap with spliced value as the key 
	heap = []
	for x in range(0, CANVAS_WIDTH, ZOOM):
		for y in range(0, CANVAS_HEIGHT, ZOOM):
			heapq.heappush(heap, (splice(x // ZOOM, y // ZOOM), (float(x), float(y))))

	# Compute line pixels between traversed z-ordered coordinates 
	pixels = []
	cur = heapq.heappop(heap)[1]
	last = cur
	while heap:
		cur = heapq.heappop(heap)[1]
		pixels += dda_line(last, cur)
		last = cur

	# Draw the pixels to canvas
	for pixel in pixels:
		draw.point(pixel, LINE_COLOR)

def main():
	# Setup canvas
	dir_path = os.path.dirname(os.path.abspath(__file__))
	im = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT))
	draw = ImageDraw.Draw(im)
	
	# Draw the curve	
	draw_z_order(draw)

	im.save(dir_path + os.sep + OUTFILE)

if __name__ == "__main__":
	main()


