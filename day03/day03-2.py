#!/usr/bin/env python

count = 0

with open('day03.input') as f:
    lines = f.read().splitlines()
for x in xrange(0,len(lines)/3):
 	line0 = map(int, " ".join(lines[3*x].split()).split(" "))
 	line1 = map(int, " ".join(lines[3*x+1].split()).split(" "))
	line2 = map(int, " ".join(lines[3*x+2].split()).split(" "))

 	if line0[0] < line1[0] + line2[0] and line1[0] < line2[0] + line0[0] and line2[0] < line0[0] + line1[0]:
 		count += 1
 	if line0[1] < line1[1] + line2[1] and line1[1] < line2[1] + line0[1] and line2[1] < line0[1] + line1[1]:
 		count += 1
 	if line0[2] < line1[2] + line2[2] and line1[2] < line2[2] + line0[2] and line2[2] < line0[2] + line1[2]:
 		count += 1

print count