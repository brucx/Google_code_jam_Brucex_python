class Level(object):
	def __init__(self, two_numbers):
		self.a, self.b = two_numbers
		self.level_stars = 2
	def __repr__(self):
		return "%d:%d->%d"%(self.a, self.b, self.level_stars)

def find_next(levels, stars):
	if len(levels)>0 and stars >= levels[-1].b:
		return levels[-1], True
	for level in levels:
		if stars >= level.a and level.level_stars == 2:
			return level, False
	return None, None

# test = 5

for i in xrange(input()):
	levels = []
	for k in xrange(input()):
		levels.append(Level([int(a) for a in raw_input().split()]))
	levels.sort(key=lambda x: x.b, reverse = True)
	stars, count = 0, 0
	level, big_enough = find_next(levels, stars)
	while level != None:
		if big_enough:
			stars += level.level_stars
			level.level_stars = 0
		else:
			stars += 1
			level.level_stars -= 1
		count += 1
		# if i == test-1:
		# 	print levels, "\n","#%d CHOOSED:"%count, level, "All_stars:", stars,"\n"
		if level.level_stars == 0: levels.remove(level)
		level, big_enough = find_next(levels, stars)
	if levels != []:
		count = "Too Bad"
	print "Case #%d:"%(i+1), count