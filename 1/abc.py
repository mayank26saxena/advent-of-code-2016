import csv
#data = ['R2' , 'L3']
#data = ['R2' , 'R2', 'R2']
#data = ['R5' , 'L5', 'R5', 'R3']
#data = ['R3', 'L3' , 'L10']
data = []
with open('input.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		data = data + row
		
west_total = 0
east_total = 0
north_total = 0
south_total = 0
direction = 0
r = 'R'
l = 'L'

# North = 0 , South = 1, East = 2, West = 3

first_direction = data[0][0]
first_steps = int(data[0][1:])

if first_direction == r :
	direction = 2
	east_total += first_steps
else :
	direction = 3
	west_total += first_steps
	
for i in range(1, len(data)):
	direction2 = data[i][0]
	steps = int(data[i][1:])
	if direction == 0 :
		print 'direction is north'
		if direction2 == r :
			direction = 2
			east_total += steps
		else :
			direction = 3
			west_total += steps
	elif direction == 1 :
		print 'direction is south'
		if direction2 == r :
			direction = 3
			west_total += steps
		else :
			direction = 2
			east_total += steps
	elif direction == 2 :
		print 'direction is east'
		if direction2 == r :
			direction = 1
			south_total += steps
		else :
			direction = 0
			north_total += steps
	else :
		print 'direction is west'
		if direction2 == r :
			direction = 0
			north_total += steps
		else:
			direction = 1
			south_total += steps

print 'north total = ' + str(north_total)
print 'south total = ' + str(south_total)
print 'east total = ' + str(east_total)
print 'west total = ' + str(west_total)
	
vertical = abs(north_total - south_total)
horizontal = abs(east_total - west_total)

total = vertical + horizontal

print 'total = ' + str(total)
