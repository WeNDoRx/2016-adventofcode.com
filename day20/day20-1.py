#!/usr/bin/env python

lines = []

import operator

with open('day20.input', 'r') as f:
	for line in f:
		lines += [[int(line.rstrip("\n").split("-")[0]), int(line.rstrip("\n").split("-")[1])]]

lines.sort(key=lambda x: (x[0], x[1]))

i = 1
x = lines[0][1] + 1
while i < len(lines):
	if x < lines[i][0]:
		print x
		break
	if x < lines[i][1]:
		x = lines[i][1]
		x += 1
	i += 1
