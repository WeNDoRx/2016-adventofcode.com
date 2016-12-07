f = open ( 'day06.input' , 'r')
l = [ map(str, list(line[:-1])) for line in f ]

sol = []
for x in xrange(0,len(l[0])):
	sol += min(set([row[x] for row in l]), key=[row[x] for row in l].count)

print ''.join(sol)