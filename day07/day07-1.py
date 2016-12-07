#!/usr/bin/env python

import re

pattern1 = re.compile(".*(?P<A>.)(?P<B>.)(?P=B)(?P=A).*")
pattern2 = re.compile(".*\[[\w]*(?P<A>.)(?P<B>.)(?P=B)(?P=A)[\w]*\].*")

total_part_1 = 1

with open("day07.input") as f:
	for line in f:
		string = line.replace('\n', '')
		# if no abba between brackets
		if not pattern2.match(string) or (pattern2.match(string) and pattern2.match(string).group('A') == pattern2.match(string).group('B')):
			# and if abba present
			if pattern1.match(string) and pattern1.match(string).group('A') != pattern1.match(string).group('B'):
				total_part_1 += 1

print total_part_1