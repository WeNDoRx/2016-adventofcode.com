#!/usr/bin/env python

f = open("day01.input","r")
for line in f:
	line = line.strip('\n').split(', ')
	x,y,d = 0,0,0
	for step in line:
		if step[0] == 'R':
			d = d + 1
		if step[0] == 'L':
			d = d - 1
		d = d % 4
		steps = int(step[1:])
		if d == 0:
			y = y + steps
		if d == 1:
			x = x + steps
		if d == 2:
			y = y - steps
		if d == 3:
			x = x - steps
		#print d, x, y

	print abs(x)+abs(y)