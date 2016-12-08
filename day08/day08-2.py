#!/usr/bin/env python

import sys

disp_h, disp_w = 6, 50

def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print []
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = 1
    print "[ ",
    for row in xrange(rows):
        if (row > 0): print "\n  ",
        print "[ ",
        for col in xrange(cols):
            # The next 2 lines print a[row][col] with the given fieldWidth
            format = "%" + str(fieldWidth) + "s"
            print format % str(a[row][col]),
        print "]",
    print "]"

# initialise the LED matrix with all leds turned off
display = [['.' for i in range(disp_w)] for j in range(disp_h)]

def lightPixels(x, y):
	global display
	for a in xrange(0,y):
		for b in xrange(0,x):
			display[a][b] = 'x'

def rotateColumn(col, by):
	global display
	for i in xrange(0,by):
		tmp = display[disp_h - 1][col]
		for x in xrange(disp_h - 2, -1, -1):
			display[x+1][col] = display[x][col]
		display[0][col] = tmp

def rotateRow(row, by):
	global display
	for i in xrange(0,by):
		tmp = display[row][disp_w - 1]
		for x in xrange(disp_w - 2, -1, -1):
			display[row][x+1] = display[row][x]
		display[row][0] = tmp

def processLine(line):
	# light up the pixels
	if 'rect' in line:
		x,y = int(line.split(' ')[1].split('x')[0]), int(line.split(' ')[1].split('x')[1])
		lightPixels(x, y)

	# rotate column
	if 'column' in line:
		split = line.split(' ')
		col, by = int(split[2].split("=")[1]), int(split[4])
		rotateColumn(col, by)

	# rotate row
	if 'row' in line:
		split = line.split(' ')
		row, by = int(split[2].split("=")[1]), int(split[4])
		rotateRow(row, by)


with open("day08.input") as f:
	for line in f:
		processLine(line[:-1])

print print2dList(display)