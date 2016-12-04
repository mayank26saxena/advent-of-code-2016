with open('input') as f:
	content = f.readlines()
	
possible = 0
not_possible = 0

n = len(content)
print n

for i in range(0, n, 3) :
	l = content[i]
	l = l.split()
	
	l2 = content[i+1]
	l2 = l2.split()
	
	l3 = content[i+2]
	l3 = l3.split()
	
	n1 = l[0]
	n2 = l2[0]
	n3 = l3[0]
	
	m1 = l[1]
	m2 = l2[1]
	m3 = l3[1]
	
	p1 = l[2]
	p2 = l2[2]
	p3 = l3[2]
	
	num1 = int(n1)
	num2 = int(n2)
	num3 = int(n3)
	
	print 'num 1 = ' + str(num1)
	print 'num 2 = ' + str(num2)
	print 'num 3 = ' + str(num3)
	
	mum1 = int(m1)
	mum2 = int(m2)
	mum3 = int(m3)
	
	print 'mum 1 = ' + str(mum1)
	print 'mum 2 = ' + str(mum2)
	print 'mum 3 = ' + str(mum3)
	
	pum1 = int(p1)
	pum2 = int(p2)
	pum3 = int(p3)
	
	print 'pum 1 = ' + str(pum1)
	print 'pum 2 = ' + str(pum2)
	print 'pum 3 = ' + str(pum3)
	
	if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
		possible = possible + 1
	else :
		not_possible = not_possible + 1
		
	if (mum1 + mum2 > mum3) and (mum1 + mum3 > mum2) and (mum2 + mum3 > mum1):
		possible = possible + 1
	else :
		not_possible = not_possible + 1
		
	if (pum1 + pum2 > pum3) and (pum1 + pum3 > pum2) and (pum2 + pum3 > pum1):
		possible = possible + 1
	else :
		not_possible = not_possible + 1
			
print 'possible = ' + str(possible)
print 'not possible = ' + str(not_possible)
