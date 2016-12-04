# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 5, 5 
Matrix = [[0 for x in range(w)] for y in range(h)] 
Matrix[0][0] = -1
Matrix[0][1] = -1
Matrix[0][2] = 1
Matrix[0][3] = -1
Matrix[0][4] = -1
Matrix[1][0] = -1
Matrix[1][1] = 2
Matrix[1][2] = 3
Matrix[1][3] = 4
Matrix[1][4] = -1
Matrix[2][0] = 5
Matrix[2][1] = 6
Matrix[2][2] = 7
Matrix[2][3] = 8
Matrix[2][4] = 9
Matrix[3][0] = -1
Matrix[3][1] = 100 #A
Matrix[3][2] = 101 #B
Matrix[3][3] = 102 #C
Matrix[3][4] = -1
Matrix[4][0] = -1
Matrix[4][1] = -1
Matrix[4][2] = 103 #D
Matrix[4][3] = -1
Matrix[4][4] = -1


print Matrix

with open('input') as f:
	content = f.readlines()
	
line_0 = content[0]
line_1 = content[1]
line_2 = content[2]
line_3 = content[3]
line_4 = content[4]

d = 'D'
l = 'L'
u = 'U'
r = 'R'


row = 1
col = 2

for i in range(0, len(line_4)):
	c = line_4[i]
	if c == d :
		if (row != 4) and (Matrix[row+1][col] != -1) :
			row = row + 1
	if c == u :
		if (row != 0) and (Matrix[row-1][col] != -1) :
			row = row - 1
	if c == r :
		if (col != 4) and (Matrix[row][col+1] != -1) :
			col = col + 1
	if c == l :
		if (col != 0) and (Matrix[row][col-1] != -1) :
			col = col - 1
	 
	
print 'col = ' + str(col)
print 'row = ' + str(row)
