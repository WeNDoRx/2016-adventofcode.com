#!/usr/bin/env python

import re
import md5
import sys

pattern1 = re.compile(".*?(?P<A>.)(?P=A){2}.*")
pattern2 = re.compile(".*?(?P<A>.)(?P=A){4}.*")

hashes = {}
found = []

with open('day14.input', 'r') as f:
    salt = f.readline().rstrip("\n")

i = 0

def keyStretch(hexx, times):
	string = hexx.hexdigest()
	for stretch in xrange(0, times):
		a = md5.new()
		a.update(string)
		string = a.hexdigest()
	return a

# populate the hashes dict with the first 1000 extended hashes
for x in xrange(0, 1000):
	m = md5.new()
	m.update(salt+str(x))
	hashes[x] = keyStretch(m, 2016).hexdigest()

while len(found) < 64:
	extended_hash = hashes[i]

	tmp = md5.new()
	tmp.update(salt+str(i + 1000))

	hashes[1000 + i] = keyStretch(tmp, 2016).hexdigest()

	if pattern1.match(extended_hash):
		for x in xrange(i + 1, i + 1000):
			if pattern2.match(hashes[x]) and pattern1.match(hashes[i]).group('A') == pattern2.match(hashes[x]).group('A'):
				#print hashes[i], pattern1.match(hashes[i]).group('A'), i, hashes[x], x
				found += [i]
				break
	i += 1

print found[64 - 1]