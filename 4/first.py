import re
from operator import itemgetter

total = 0

with open('input') as f:
	content = f.readlines()

#content = "aaaaa-bbb-z-y-x-123[abxyz] " #Real
#content = "a-b-c-d-e-f-g-h-987[abcde] " #Real
#content = "not-a-real-room-404[oarel] " #Real
#content = "totally-real-room-200[decoy] " #Not real
#line = content

for line in content :
	m = re.search("\d", line)
	n = m.start()
	p = line.find("[")
	number = line[n:p]
	name = line[:n-1]
	l = len(line)
	checksum = line[p+1:l-2]
	old_name = name
	name = name.replace('-', '')
	dic = dict((letter,name.count(letter)) for letter in set(name))
	d = sorted(dic.items(), key = itemgetter(1), reverse = True)
	s = "" 
	for item in sorted(dic.items(), key=lambda it: (-it[1], it[0])):
		s += item[0]
	s = s[:5]
	if s == checksum :
		#total += int(number)
		shift = int(number)
		print "Shift is %d" % shift
		
		data = []
		strs = 'abcdefghijklmnopqrstuvwxyz'      #use a string like this, instead of ord() 

		for i in old_name:                     #iterate over the text not some list
			if i.strip() and i in strs:                 # if the char is not a space ""  
				data.append(strs[(strs.index(i) + shift) % 26])    
			else:
				data.append(i)           #if space the simply append it to data
		output = ''.join(data)
		
		output = output.replace('-', ' ')
    	
    	print "output is %s " % output
    	
    	f = open('output','a')
    	f.write(output)
    	f.write(' - ')
    	f.write(number)
    	f.write('\n')
    	f.close()
		
	#print "Number %d " % int(number)
	#print "Name %s " % str(name)
	#print "Checksum %s " % checksum
	#print "S is %s" % s
	#print "Total is %d " % total
	
print total
	
		
