from get_input import get_input


raw_input = get_input(day=8)
raw_input = raw_input.splitlines()

nums = 0
num_lens = [2,4,3,7]
for line in raw_input:
	line = line.split('|')[1]
	phrases = line.split()
	for phrase in phrases:
		if len(phrase) in num_lens:
			nums +=1

print(nums)


'''
Part two
'''


### Example
example_map = {
	0: 'abcefg',
	1: 'cf',
	2: 'acdeg',
	3: 'acdfg',
	4: 'bcdf',
	5: 'abdfg',
	6: 'abdefg',
	7: 'acf',
	8: 'abcdefg',
	9: 'abcdfg',
}

possibilities = {}

for k,v in example_map.items():
	if len(v) not in possibilities.keys():
		possibilities[len(v)] = [k]
	else:
		possibilities[len(v)].append(k)

unknown_values = {x:y for x,y in possibilities.items() if len(y) != 1}  # {6: [0, 6, 9], 5: [2, 3, 5]}

### End Example


def len_is_five(value): #possible 2,3,5
	if all([i in value for i in list(digit_map[7])]):
		return 3
	#2,5 left
	if sum([i in value for i in list(digit_map[4])]) == 2:
		return 2
	#5 left
	return 5


def len_is_six(value): #possible 0,6,9
	if all([i in value for i in list(digit_map[4])]):
		return 9
	#0,6 left
	if all([i in value for i in list(digit_map[1])]):
		return 0
	#6 left
	return 6


known_values = {2:1, 4:4, 3:7, 7:8}  #{digit:len}
answer_list = []

for line in raw_input:
	values, answers = line.split('|')

	digit_map = {known_values[len(val)]: val for val in values.split() if len(val) in known_values.keys()}
	unknown_values = [val for val in values.split() if len(val) not in known_values.keys()]

	for value in unknown_values:
		if len(value) == 5:
			digit_map[len_is_five(value)] = value
		elif len(value) == 6:
			digit_map[len_is_six(value)] = value
		else:
			raise AssertionError(f'Unexpected lenght {len(value)}')

	phrase_answer = ''	
	for answer in answers.split():
		for k,v in digit_map.items():
			if sorted(answer) == sorted(v):
				phrase_answer += str(k)
				break
		else:
			raise AssertionError('Answer key not found')

	answer_list.append(int(phrase_answer))


print(sum(answer_list))

