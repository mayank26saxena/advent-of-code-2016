with open('input') as f:
	content = f.readlines()
	
possible = 0
not_possible = 0
	
for line in content :
	l = line.split()
	n1 = l[0]
	n2 = l[1]
	n3 = l[2]
	
	num1 = int(n1)
	num2 = int(n2)
	num3 = int(n3)
	
	print 'num 1 = ' + str(num1)
	print 'num 2 = ' + str(num2)
	print 'num 3 = ' + str(num3)
	
	if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
		possible = possible + 1
	else :
		not_possible = not_possible + 1
			
print 'possible = ' + str(possible)
print 'not possible = ' + str(not_possible) 

