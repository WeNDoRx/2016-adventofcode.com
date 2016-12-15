#!/usr/bin/env python

discs = {}

with open("day15.input") as f:
	for line in f:
		split = line.replace('\n', '').split(' ')
		#		# disc number		# positions		at time 0
		discs[int(split[1][1:])] = int(split[3]), int(split[-1][:-1])

i = 0
while True:
	found = True
	for x in xrange(1, len(discs) + 1):
		if (x + i + discs[x][1]) % (discs[x][0]) != 0:
			found = False
			break
	if found:
		print i
		break
	i += 1