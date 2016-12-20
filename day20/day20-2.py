#!/usr/bin/env python

# it's complicated ... but basically, we start at 0, and if we find i in the starts aray,
# i becomes the coresponding end + 1. Then, we go downwards from there to find i in starts array again.
# if we find it, i becomes the coresponding end + 1 again. And so on. Except if we find i -1 in the starts array
# which means that we went through the whole range between end and start and could not find i in the starts.
# this means i + 1 is the one number we are looking for. Or something like that. It's more clear as a paper sketch.

start = []
end = []
lines = []

import operator

i = 0
with open('day20.input', 'r') as f:
	for line in f:
		lines += [[int(line.rstrip("\n").split("-")[0]), int(line.rstrip("\n").split("-")[1])]]

lines.sort(key=lambda x: x[0])

x = 0
while True:
	if lines[x][0] > lines[x + 1][1]:
		del lines[x + 1]

	if lines[x][0] > lines[x + 1][0]:
		lines[x + 1][0] = lines[x][0]
		x += 1

	if lines[x][1] > lines[x + 1][0]:
		print lines[x][1], lines[x + 1][0]
		print lines
		break
	x += 1
	print x

	if x + 2 > len(lines):
		break