#!/usr/bin/env python

from collections import Counter

#copied from http://stackoverflow.com/a/8886969
def caesar(plainText, shift):
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  return cipherText


f = open("day04.input","r")
for line in f:
	c = Counter()
 	line = line.strip('\n')
 	# find last occurance of the dash
 	lastoccc = line.rfind("-")
 	# get the id using the last occurence of [
 	id = int(line[lastoccc + 1:line.rfind("[")])
 	# get counter for frequency
 	c += Counter(line[:lastoccc].replace("-",""))
 	# sort counter first by value then by key, and get first 5 elements
 	top5 = [v for v in sorted(c.items(), key=lambda(k, v): (-v, k))][:5]
 	# boolean for valid or not
 	valid = True
 	for x in xrange(0,4):
 		# comparing
 		if top5[x][0] != line[line.rfind("[") + 1 + x]:
 			valid = False
 			break
 	# if pole in the decrypred room name
 	if valid and 'pole' in caesar(line[:lastoccc],id % 26):
 		print id#, caesar(line[:lastoccc],id % 26)