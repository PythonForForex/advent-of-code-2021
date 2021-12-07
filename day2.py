from get_input import get_input

input = get_input(day=2)
input = input.splitlines()


def position(input):

	horizontal_pos = 0
	depth_pos = 0

	for line in input:
		dir, num = line.split()
		num = int(num)

		if dir == 'forward':
			horizontal_pos += num
		
		elif dir == 'down':
			depth_pos += num
		
		elif dir == 'up':
			depth_pos -= num
		
		else:
			print(dir, num)

	
	return horizontal_pos * depth_pos


print(position(input))


'''
Part Two
'''


def position_part2(input):

	horizontal_pos = 0
	depth_pos = 0
	aim_pos = 0

	for line in input:
		dir, num = line.split()
		num = int(num)

		if dir == 'forward':
			horizontal_pos += num
			depth_pos += (aim_pos * num)
		
		elif dir == 'down':
			aim_pos += num
		
		elif dir == 'up':
			aim_pos -= num
		
		else:
			print(dir, num)

	
	return horizontal_pos * depth_pos


print(position_part2(input))

