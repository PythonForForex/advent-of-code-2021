#%%
from get_input import get_input


raw_input = get_input(day=9)
matrix = raw_input.splitlines()

filtered_matrix =[f'9{line}9' for line in matrix]
filtered_matrix.insert(0, '9' * len(filtered_matrix[0]))
filtered_matrix.append('9' * len(filtered_matrix[0]))

x_len = len(matrix)
y_len = len(matrix[0])

low_points_sum = 0

for x in range(1,x_len+1):
	for y in range(1,y_len+1):
		if filtered_matrix[x][y] < filtered_matrix[x][y-1] and filtered_matrix[x][y] < filtered_matrix[x][y+1]:
			if filtered_matrix[x][y] < filtered_matrix[x-1][y] and filtered_matrix[x][y] < filtered_matrix[x+1][y]:
				low_points_sum += int(filtered_matrix[x][y]) + 1
		
print(low_points_sum)


'''
Part two
'''


starting_cordinates = []
for x in range(1,x_len+1):
	for y in range(1,y_len+1):
		if filtered_matrix[x][y] < filtered_matrix[x][y-1] and filtered_matrix[x][y] < filtered_matrix[x][y+1]:
			if filtered_matrix[x][y] < filtered_matrix[x-1][y] and filtered_matrix[x][y] < filtered_matrix[x+1][y]:
				starting_cordinates.append([x-1,y-1])


def flowing(x, y):
	num = matrix[x][y] 
	if num != 9:
		count.append((x,y))
	
	if num + 1 !=9:

	
		left = x - 1
		if left >=0 and matrix[left][y] > num:
			flowing(left, y)

		right = x + 1
		if right < len(matrix) and matrix[right][y] > num:
			flowing(right, y)

		up = y - 1
		if up >= 0 and matrix[x][up] > num:
			flowing(x, up)

		down = y + 1 
		if down < len(matrix[0]) and matrix[x][down] > num:
			flowing(x, down)


matrix = [[int(i) for i in list(line)] for line in matrix]

counts = []
for cordinate in starting_cordinates:
	x,y = cordinate
	count = []
	flowing(x,y)
	counts.append(len(set(count)))
	

a,b,c = sorted(counts)[-3:]

print(a*b*c)
