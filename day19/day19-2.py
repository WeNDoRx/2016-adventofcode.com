#!/usr/bin/env python

with open('day19.input', 'r') as f:
	line = int(f.readline().rstrip("\n"))
	elves = range(5)
	i = 0
	while len(elves) > 1:
		remove = len(elves[:i]) 