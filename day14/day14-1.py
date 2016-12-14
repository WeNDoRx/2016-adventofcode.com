#!/usr/bin/env python

import re
import md5

pattern1 = re.compile(".*?(?P<A>.)(?P=A){2}.*")
pattern2 = re.compile(".*?(?P<A>.)(?P=A){4}.*")

hashes = {}
found = []

with open('day14.input', 'r') as f:
    salt = f.readline().rstrip("\n")

i = 0

while len(found) < 64:
	m = md5.new()
	m.update(salt+str(i))
	if pattern1.match(m.hexdigest()):
		for x in xrange(i + 1, i + 1000):
			n = md5.new()
			n.update(salt+str(x))
			if pattern2.match(n.hexdigest()) and pattern1.match(m.hexdigest()).group('A') == pattern2.match(n.hexdigest()).group('A'):
				#print m.hexdigest(), pattern1.match(m.hexdigest()).group('A'), i, n.hexdigest(), x
				found += [i]
				break
	i += 1

print found[64 - 1]