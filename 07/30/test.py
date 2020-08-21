def myreduce(function,seq):
	tally = seq[0]
	for x in seq[1:]:
		tally = function(tally,x)
	return tally

print(myreduce(lambda x,y:x*y, [1,2,3,4]))
