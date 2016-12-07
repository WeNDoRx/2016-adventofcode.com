import md5

with open('day05.input', 'r') as f:
    my_hash = f.readline().rstrip("\n")

i = 0
f = []

while len(f) < 8:
	m = md5.new()
	m.update(my_hash+str(i))
	if m.hexdigest()[:5] == "00000":
	 	f += m.hexdigest()[5],

	i += 1

print "".join(f)