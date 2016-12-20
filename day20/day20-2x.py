#!/usr/bin/env python

# it's complicated ... but basically, we start at 0, and if we find i in the starts aray,
# i becomes the coresponding end + 1. Then, we go downwards from there to find i in starts array again.
# if we find it, i becomes the coresponding end + 1 again. And so on. Except if we find i -1 in the starts array
# which means that we went through the whole range between end and start and could not find i in the starts.
# this means i + 1 is the one number we are looking for. Or something like that. It's more clear as a paper sketch.

start = []
end = []

with open('day20.input', 'r') as f:
	for line in f:
		split = line.rstrip("\n").split("-")
		start += [int(split[0])]
		end += [int(split[1])]

found = []

for i in xrange(0, max(end)):
	notInList = True
	for x in xrange(0, len(start) - 1):
		if i >= start[x] and i <= end[x]:
			notInList = False
			break
	if i > end[x]:
		del start[x]
		del end[x]
	if notInList:
		found.append(i)
		print len(found), i, max(end)

print len(found)