t = input()
for i in xrange(t):
	m, length = [int(x) for x in raw_input().split()]
	n = length - m
	probs = [1]
	map(lambda x:probs.append(float(x)), raw_input().split())
	expected_min = length + 2
	for k in xrange(m):
		prob = reduce(lambda product,x: product*x, probs[:m-k+1])
		keystroked = 2*k + n + 1
		expected  = prob * keystroked + (1 - prob) * (keystroked + length +1)
		if expected < expected_min: expected_min = expected
	print 'Case #%d:'%(i+1),expected_min