import re
from operator import itemgetter

total = 0

with open('input') as f:
	content = f.readlines()
	
for line in content :
	m = re.search("\d", line)
	n = m.start()
	p = line.find("[")
	number = line[n:p]
	name = line[:n]
	l = len(line)
	checksum = line[p+1:l-2]
	name = name.replace('-', '')
	dic = dict((letter,name.count(letter)) for letter in set(name))
	d = sorted(dic.items(), key = itemgetter(1), reverse = True)
	s = "" 
	for i in range(0, 5):
		s += d[i][0]
	if s == checksum :
		total += int(number)
	print "Number %d " % int(number)
	print "Name %s " % str(name)
	print "Checksum %s " % checksum
	print "S is %s" % s
	print "Total is %d " % total
	#break
print total
	
		
