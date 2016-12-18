#!/usr/bin/env python

room = []

def determineTile(left, center, right):
	if left == '^' and center == '^' and right == '.':
		return '^'
	if center == '^' and right == '^' and left == '.':
		return '^'
	if left == '^' and center == '.' and right == '.':
		return '^'
	if right == '^' and center == '.' and left == '.':
		return '^'
	return '.'


def calculateNextRow(previousRow):
	newRow = []
	for x in xrange(0, len(previousRow)):
		# leftmost character, has no coresponding character further left
		if x == 0:
			newRow += determineTile('.', previousRow[x], previousRow[x + 1])
		# rightmost character
		if x == len(previousRow) - 1:
			newRow += determineTile(previousRow[x - 1], previousRow[x], '.')
		if x != 0 and x != len(previousRow) - 1:
			newRow += determineTile(previousRow[x - 1], previousRow[x], previousRow[x + 1])
	return newRow



with open("day18.input") as f:
		room += [list(f.readline().replace('\n', ''))]

i = 0
while i < 400000 - 1 :
	room += [calculateNextRow(room[i])]
	i += 1

print sum(x.count('.') for x in room)