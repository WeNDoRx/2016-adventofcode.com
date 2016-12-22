#!/usr/bin/env python

lines = []
nodes = {}

def count_viable_pairs():
	count = 0
	for k1, v1 in nodes.iteritems():
		for k2, v2 in nodes.iteritems():
			if k1 == k2:
				continue
			if v1[1] == 0:
				continue
			if v1[1] > v2[2]:
				continue
			count += 1
	print count


def generate_nodes_dict():
	global nodes
	for line in lines:
		split = line[0].split('-')
		x,y = int(split[1][1:]), int(split[2][1:])
		size, used, avail, percent = int(line[1][:-1]), int(line[2][:-1]), int(line[3][:-1]), int(line[3][:-1])
		nodes[(x,y)] = size, used, avail, percent

with open('day22.input', 'r') as f:
	f.readline()
	f.readline()
	for line in f:
		lines += [' '.join(line[:].split()).split(' ')]

generate_nodes_dict()
#print sorted(nodes.iteritems())
count_viable_pairs()