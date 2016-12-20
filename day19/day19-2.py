#!/usr/bin/env python

from math import log

with open('day19.input', 'r') as f:
	line = int(f.readline().rstrip("\n"))
	# way too smart solution from https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/dbdobax/
	# just too beautiful to let it slip away ...
	p = 3 ** int(log(line - 1, 3))
	print line - p + max(line -2 * p, 0)