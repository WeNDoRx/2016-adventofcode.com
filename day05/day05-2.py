import md5

with open('day05.input', 'r') as f:
    my_hash = f.readline().rstrip("\n")

i = 0
f = ['x','x','x','x','x','x','x','x']

while 'x' in f:
	m = md5.new()
	m.update(my_hash+str(i))
	if m.hexdigest()[:5] == "00000" and '0' <= m.hexdigest()[5] <= '7' and f[int(m.hexdigest()[5])] == 'x' :
	 	f[int(m.hexdigest()[5])] = m.hexdigest()[6]

	i += 1

print ''.join(f)