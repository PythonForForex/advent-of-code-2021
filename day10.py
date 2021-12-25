from get_input import get_input


raw_input = get_input(day=10)
raw_input = raw_input.splitlines()

open_symbols = ['(', '[', '{', '<']
closing_symbols = [')', ']', '}', '>']

syntax_errors = []
for line in raw_input:

	for _ in range(len(line)**2):
		for open_string, close_string in zip(open_symbols, closing_symbols):
			if open_string+close_string in line:
				line = line.replace(open_string+close_string, '')
				break
		else:
			break
		
	for symbol in line:
		if symbol in closing_symbols:
			syntax_errors.append(symbol)
			break


point_system = {
	')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
	}

score = [point_system.get(points) for points in syntax_errors]
print(sum(score))
