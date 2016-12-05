import hashlib

door_id = 'wtnhxymk'

index = 0

count = 0

password = ''

zeros = '00000'

while count < 8 :
	s = door_id + str(index)
	hash_object = hashlib.md5(s)
	hexa = hash_object.hexdigest()
	first_five = hexa[0:5]
	if first_five == zeros :
		password += hexa[5]
		count = count + 1
		print 's = %s ' % s
	index = index + 1
	

#hash_object = hashlib.md5(door_id)
#hexa = hash_object.hexdigest()
#print hexa

print "Password is %s " % password
