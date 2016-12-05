import hashlib

door_id = 'wtnhxymk'
index = 0
count = 0
word = 'ssssssss'
zeros = '00000'

while count < 8 :
	s = door_id + str(index)
	hash_object = hashlib.md5(s)
	hexa = hash_object.hexdigest()
	first_five = hexa[0:5]
	if first_five == zeros :
		position = hexa[5]
		i = int(position, 16)
		char = hexa[6]
		if i < 8 :
			print "Position %s i %d " % (position , i)
			if word[i] == 's' :
				count = count + 1
				word = word[:i] + char + word[i + 1:]
			print "Word is %s " % word
			#print 's = %s ' % s
	index = index + 1

print "Password is %s " % word
