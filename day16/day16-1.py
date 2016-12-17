#!/usr/bin/env python

leng = 272

def generate(a):
	return a + '0' + a[::-1].replace('0', 'u').replace('1', '0').replace('u', '1')

def checksum(a):
	check = ''
	for x in xrange(0, len(a) - 1, 2):
		if a[x:x+2] in ['00', '11']:
			check += '1'
		else:
			check += '0'
	return check
	

with open("day16.input") as f:
	for line in f:
		inp = line.replace('\n', '')
		while len(inp) <= leng:
			inp = generate(inp)
		inp = inp[:leng]

		check = checksum(inp)
		while len(check)  % 2 != 1:
			check = checksum(check)
		print check