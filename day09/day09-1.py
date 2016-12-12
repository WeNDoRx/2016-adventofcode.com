#!/usr/bin/env python

import sys

def processLine(line):
	newline = ''
	while len(line) != 0:
		if line[0] == '(':
			close = line.find(')')
			length, times = int(line[1:close].split('x')[0]), int(line[1:close].split('x')[1])
			group = line[close + 1:close + 1 + length]

			for time in xrange(0, times):
				newline += group
			line = line[close + 1 + length:]
		else:
			newline += line[0]
			line = line[1:]
	return newline
			

sum = 0
with open("day09.input") as f:
	for line in f:
		sum += len(processLine(line[:-1]))
print sum