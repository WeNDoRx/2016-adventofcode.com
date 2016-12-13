#!/usr/bin/env python

# CODE ADAPTED FROM http://bryukh.com/labyrinth-algorithms/

from heapq import heappop, heappush

maze = []

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j] != '.'}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col] != '.':
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1] != '.':
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def find_path_astar(maze, goalx, goaly):
    start, goal = (1, 1), (goalx, goaly)
    pr_queue = []
    heappush(pr_queue, (0 + heuristic(start, goal), 0, "", start))
    visited = set()
    graph = maze2graph(maze)
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            heappush(pr_queue, (cost + heuristic(neighbour, goal), cost + 1,
                                path + direction, neighbour))
    return "NO WAY!"

def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print []
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = 1
    print "[ ",
    for row in xrange(rows):
        if (row > 0): print "\n  ",
        print "[ ",
        for col in xrange(cols):
            # The next 2 lines print a[row][col] with the given fieldWidth
            format = "%" + str(fieldWidth) + "s"
            print format % str(a[row][col]),
        print "]",
    print "]"

def getMazeCell(x, y, seed):
	cell = x*x + 3*x + 2*x*y + y + y*y + seed
	bin_ones = bin(cell).count("1")
	return '.' if bin_ones % 2 == 0 else '#'

def buildMaze(seed, x, y):
	maze = [[0 for i in range(y)] for j in range(x)]
	for a in xrange(0, x):
		for b in xrange(0, y):
			#print a, b
			maze[a][b] = getMazeCell(b, a, seed)
	return maze

seed = 0

with open("day13.input") as f:
	for line in f:
		seed = int([line.replace('\n', '')][0])
			# seed, rows, cols
maze = buildMaze(seed, 55, 55)

count = 0

for x in xrange(0,50):
	for y in xrange(0,50):
		path = find_path_astar(maze, x, y)
		if path != "NO WAY!" and len(path) <= 50:
			count += 1

print count
