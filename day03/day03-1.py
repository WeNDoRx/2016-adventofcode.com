#!/usr/bin/env python

count = 0

f = open("day03.input","r")
for line in f:
 	line = map(int, " ".join(line.split()).split(" "))
 	if line[0] < line[1] + line[2] and line[1] < line[2] + line[0] and line[2] < line[0] + line[1]:
 		count += 1
print count