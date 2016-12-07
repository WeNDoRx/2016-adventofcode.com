#!/usr/bin/env python

# I FUCKING HATED THIS ONE ! installed the new regex package to make it quicker

import regex as re

pattern1 = re.compile("(?P<A>[\w])(?P<B>[\w])(?P=A)")

total_part_2 = 0

with open("day07.input") as f:
    for line in f:
    	string = line.replace('\n', '')
    	inside_brackets = '|'.join(re.findall('\[(.*?)\]',string))
    	bab = re.findall(pattern1, inside_brackets, overlapped=True)
    	bab = filter(lambda x : x[0] != x[1], bab)

    	outside_brackets = re.sub(r'\[.*?\]', '|', string)

    	aba = re.findall(pattern1, outside_brackets, overlapped=True)
    	aba = filter(lambda x : x[0] != x[1], aba)

    	for x in bab:
    		if (x[1], x[0]) in aba:
    			total_part_2 +=1
    			break

print total_part_2