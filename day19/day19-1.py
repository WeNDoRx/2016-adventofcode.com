#!/usr/bin/env python

with open('day19.input', 'r') as f:
	line = f.readline().rstrip("\n")
	print int( bin(int(line))[3:] + bin(int(line))[2:3], 2)