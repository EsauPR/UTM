#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys;
import random
import numpy
import math
import os
from PIL import Image

def loadImage( path ) :
	size = 28

	f = Image.open( path )

	A = list(f.getdata())
	print(A)

	newImage = Image.new("L", (size,size))
	pixels = newImage.load()
	pos = 0
	for x in range( size ) :
		for y in range( size ) :
			color = A[pos]
			pos += 1
			pixels[y,x] = color
			
	newImage.save( "otro.gif" )

	f2 = Image.open( "otro.gif" )
	print( list(f2.getdata()) )

	print(f.format, f.mode)
	print(f2.format, f2.mode)
	f.show()
	f2.show()

def main() :
	loadImage("n5.gif")

if __name__ == '__main__':
	main()