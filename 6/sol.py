import numpy as np
with open('input', 'r') as f:
	content = f.readlines()
	
m = np.zeros((8, 26))
print m
def convert_char(old):
    new = ord(old)
    if 97 <= new <= 122:
        # Lower case letter
        return new - 97
    # Unrecognized character
    return 0
        
n = len(content)

for i in range (0, 8):
	for j in range(0, n):
		c = content[j][i]
		ch = int(convert_char(c))
		m[i][ch] = m[i][ch] + 1
		#print 'c = %s ch = %d' % (c, ch)
	#break
				
maxi = [27]*8
ma = [-1]*8
for i in range(0, 8):
	for j in range(0, 26):
		if (m[i][j] < maxi[i]) :
			maxi[i] = m[i][j]
			ma[i] = j
print ma
print m
