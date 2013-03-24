source = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
target = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
alpha_map = dict(zip(source,target)+[('z','q'), ('q','z')])
for i in xrange(input()):
	print "Case #%d:" % (i+1), reduce(lambda out, x: out+alpha_map[x], raw_input(), '')