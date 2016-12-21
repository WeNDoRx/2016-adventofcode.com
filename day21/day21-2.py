#!/usr/bin/env python
from itertools import permutations

string = list('abcdefgh')

def rotate(steps, direction):
	global string
	for x in xrange(0, steps):
		if direction < 0:
			string = [string[-1]] + string[:-1]
		else:
			string = string[1:] + [string[0]]

def swap_position(x, y):
	global string
	tmp = string[x]
	string[x] = string[y]
	string[y] = tmp

def swap_letter(x, y):
	global string
	string = ['#' if a==x else a for a in string]
	string = [x if a==y else a for a in string]
	string = [y if a=='#' else a for a in string]

def reverse(x, y):
	global string
	if x == 0:
		string = string[:y+1][::-1] + string[y+1:]
		return
	tmp = string[y:x-1:-1]
	string = string[:x] + tmp + string[y+1:]

def move(x, y):
	global string
	if x < y:
		tmp = string[x]
		string = string[:x] + string[x+1:y+1] + [tmp] + string[y+1:]
		return
	tmp = string[x]
	string = string[:y] + [tmp] + string[y:x] + string[x+1:]

def processLine(line):
	global string

	# light up the pixels
	if line[0] == 'swap' and line[1] == 'position':
		x,y = int(line[2]), int(line[5])
		swap_position(x, y)

	if line[0] == 'swap' and line[1] == 'letter':
		x,y = line[2], line[5]
		swap_letter(x, y)

	# rotate column
	if line[0] == 'rotate' and (line[1] == 'left' or line[1] == 'right'):
		steps = int(line[2])
		if line[1] == 'left': direction = 1
		else: direction = -1
		rotate(steps, direction)

	if line[0] == 'reverse':
		x,y = int(line[2]), int(line[4])
		reverse(x, y)

	if line[0] == 'move':
		x,y = int(line[2]), int(line[5])
		move(x,y)

	if line[0] == 'rotate' and line[1] == 'based':
		times = string.index(line[6])
		if times >= 4: times += 1
		times += 1
		rotate(times, -1)

# small input = BRUTEFORCE !!1
for p in permutations(string):
	string = list(p)
	with open("day21.input") as f:
		for line in f:
			processLine(line[:-1].split(' '))

	if ''.join(string) == 'fbgdceah':
	 	print ''.join(p)
	 	break