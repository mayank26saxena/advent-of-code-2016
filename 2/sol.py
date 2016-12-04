# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 3, 3 
Matrix = [[0 for x in range(w)] for y in range(h)] 
Matrix[0][0] = 1
Matrix[0][1] = 2
Matrix[0][2] = 3
Matrix[1][0] = 4
Matrix[1][1] = 5
Matrix[1][2] = 6
Matrix[2][0] = 7
Matrix[2][1] = 8
Matrix[2][2] = 9

print Matrix

with open('input') as f:
	content = f.readlines()
	
line_0 = content[0]
line_1 = content[1]
line_2 = content[2]
line_3 = content[3]
line_4 = content[4]

n = len(line_4)

d = 'D'
l = 'L'
u = 'U'
r = 'R'

num = 5

row = 0
col = 1

for i in range(0, n):
	c = line_4[i]
	if c == d :
		if row != 2 :
			row = row + 1
	if c == u :
		if row != 0 :
			row = row - 1
	if c == r :
		if col != 2 :
			col = col + 1
	if c == l :
		if col != 0 :
			col = col - 1
	 
	
print 'col = ' + str(col)
print 'row = ' + str(row)
