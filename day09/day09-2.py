#!/usr/bin/env python

import sys

def processLine(line):
	if '(' not in line:
		return len(line)

	if line[0] == '(':
		close = line.find(')')
		length, times = int(line[1:close].split('x')[0]), int(line[1:close].split('x')[1])
		group = line[close + 1:close + 1 + length]
		return processLine(times * group) + processLine(line[len(group) + 0 + close + 1:])
	return 1 + processLine(line[1:])


sum = 0
with open("day09.input") as f:
	for line in f:
		sum += processLine(line[:-1])
print sum