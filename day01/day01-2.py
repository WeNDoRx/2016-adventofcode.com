#!/usr/bin/env python

import sys

f = open("day01.input","r")
for line in f:
	line = line.strip('\n').split(', ')
	x,y,d,v = 0,0,0,[]
	for step in line:
		oldx, oldy = x,y
		if step[0] == 'R':
			d = d + 1
		if step[0] == 'L':
			d = d - 1
		d = d % 4
		steps = int(step[1:])
		if d == 0:
			y = y + steps
			for a in xrange(1, abs(y - oldy)):
				if [x, oldy+a] in v:
					print abs(x) + abs(oldy+a)
					sys.exit(0)
				else:
					v += [[x,oldy+a]]
		if d == 1:
			x = x + steps
			for a in xrange(1, abs(x - oldx)):
				if [oldx+a, y] in v:
					print abs(oldx+a) + abs(y)
					sys.exit(0)
				else:
					v += [[oldx+a, y]]
		if d == 2:
			y = y - steps
			for a in xrange(1, abs(y - oldy)):
				if [x, oldy-a] in v:
					print abs(x) + abs(oldy-a)
					sys.exit(0)
				else:
					v += [[x,oldy-a]]
		if d == 3:
			x = x - steps
			for a in xrange(1, abs(x - oldx)):
				if [oldx-a, y] in v:
					print abs(oldx-a) + abs(y)
					sys.exit(0)
				else:
					v += [[oldx-a, y]]

		if [x,y] in v:
			break
		else:
			v += [[x,y]]

	print v
	print abs(x)+abs(y)