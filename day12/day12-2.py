#!/usr/bin/env python

registers = {'a':0, 'b':0, 'c':1, 'd':0}

def processLine(string, pointer):
	split = string.split(' ')
	if split[0] == 'cpy':
		try:
			registers[split[2]] = int(split[1])
		except Exception as e:
			registers[split[2]] = registers[split[1]]
	if split[0] == 'jnz':
		try:
			if int(split[1]) != 0:
				return pointer + int(split[2])
			else: return pointer + 1
		except Exception as e:
			if int(registers[split[1]]) != 0:
				return pointer + int(split[2])

	if split[0] == 'inc':
		registers[split[1]] += 1
	if split[0] == 'dec':
		registers[split[1]] += -1

	return pointer + 1
	
instructions = []

with open("day12.input") as f:
	for line in f:
		instructions += [line.replace('\n', '')]


instruction_pointer = processLine(instructions[0], 0)
while True:
	if instruction_pointer > len(instructions) - 1:
		print registers['a']
		break
	instruction_pointer = processLine(instructions[instruction_pointer], instruction_pointer)
	#print registers, instruction_pointer, instructions[instruction_pointer]
	#raw_input()