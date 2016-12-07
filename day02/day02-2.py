#!/usr/bin/env python

solution = []
# a dial pad for fun
pad = [['', '', '1', '', ''],
       ['', '2','3','4', ''],
       ['5','6','7','8','9'],
       ['', 'A','B','C', ''],
       ['', '', 'D', '', '']]

# start on 5
x,y = 2,0
# directions dict
directions = {'U':{'x':-1, 'y':0}, 'D':{'x':1, 'y':0}, 'L':{'x':0, 'y':-1}, 'R':{'x':0, 'y':1}}
#print(np.matrix(pad))
f = open("day02.input","r")
for line in f:
 	line = list(line.strip('\n'))
 	for step in line:
 		x,y = x+directions[step]['x'], y+directions[step]['y']
 		if x < 0: x = 0
 		if x > 4: x = 4
 		if y < 0: y = 0
 		if y > 4: y = 4
 		if pad[x][y] == '':
 			x = x-directions[step]['x']
 		if pad[x][y] == '':
 			y = y-directions[step]['y']
	solution += [pad[x][y]]
print ''.join(map(str, solution))