#!/usr/bin/env python

import collections
import sys
from collections import defaultdict


instrunctions = {}
values = {}
outputs = {}

def processLine(line):
	global instrunctions, values
	split = line.split(' ')
	if split[0] == 'bot':
					#bot gives    bot/out   number    bot/out    number
		instrunctions[int(split[1])] = split[5], int(split[6]), split[10], int(split[11])
	else:
		#       value        bot
		values[int(split[1])] = int(split[5])


def findDuplicates(values):
	newDict = defaultdict(list)
	for var, name in values.items():
		newDict[name].append(var)
	dups = ()
	for k, v in newDict.items():
		if len(v) > 1:
			dups += k, v
	return dups

def processDuplicates(tuple):
	while len(tuple) != 0:
		tuple = (tuple[0], sorted(tuple[1])) + tuple[2:]
		if tuple[1][0] == 17 and tuple[1][1] == 61:
			print tuple[0]
		#print 'bot', tuple[0], 'gives', tuple[1][0], 'to', instrunctions[tuple[0]][0], instrunctions[tuple[0]][1], 'and', tuple[1][1], 'to', instrunctions[tuple[0]][2], instrunctions[tuple[0]][3]
		if instrunctions[tuple[0]][0] == 'output':
			# insert value in outputs
			outputs[instrunctions[tuple[0]][1]] = tuple[1][0]
			# delete value from values
			del(values[tuple[1][0]])
		if instrunctions[tuple[0]][2] == 'output':
			outputs[instrunctions[tuple[0]][3]] = tuple[1][1]
			del(values[tuple[1][1]])

		if instrunctions[tuple[0]][0] == 'bot':
			values[tuple[1][0]] = instrunctions[tuple[0]][1]
		if instrunctions[tuple[0]][2] == 'bot':
			values[tuple[1][1]] = instrunctions[tuple[0]][3]


		tuple = tuple[2:]



with open("day10.input") as f:
	for line in f:
		processLine(line[:-1])

while len(values) != 0:
	processDuplicates((findDuplicates(values)))
