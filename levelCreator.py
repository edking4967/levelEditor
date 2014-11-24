#!/usr/bin/python
from PIL import Image
import json

#convert from png
file_in = "levelmap2.png"
img = Image.open(file_in)
r, g, b, a = img.split()
img = Image.merge("RGB", (r, g, b))
file_out = "levelmap2.bmp"
img.save(file_out)

#read in values
pixels = list( img.getdata() )
width, height = img.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

pxls=[[0 for x in range(width)] for y in range(height)]

#create 2-d array of values:
for i in range(width):
	for j in range(height):
		if (pixels[i][j][0]==0):
			pxls[i][j]=0;
		else:
			pxls[i][j]=1;
for i in range(height):
	print pxls[i]


with open('data.txt', 'w') as outfile:
		json.dump(pxls, outfile)
