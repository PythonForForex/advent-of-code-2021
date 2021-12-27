from get_input import get_input


raw_input = get_input(day=10)
raw_input = raw_input.splitlines()

open_symbols = ["(", "[", "{", "<"]
closing_symbols = [")", "]", "}", ">"]

syntax_errors = []
incomplete_lines = []
for line in raw_input:

	for _ in range(len(line) ** 2):
		for open_string, close_string in zip(open_symbols, closing_symbols):
			if open_string + close_string in line:
				line = line.replace(open_string + close_string, "")
				break
		else:
			break

	for symbol in line:
		if symbol in closing_symbols:
			syntax_errors.append(symbol)
			break
	else:
		incomplete_lines.append(line)	


point_system = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137,
}

score = [point_system.get(points) for points in syntax_errors]
print(sum(score))


"""
Part two  ***** Inspired by - https://github.com/timothyquan
"""


closing_map = {open_: close_ for open_, close_ in zip(open_symbols, closing_symbols)}
point_system = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4,
}


def get_answers(line):
	to_add = [closing_map.get(symbol) for symbol in reversed(line)]
	points = [point_system.get(val) for val in to_add]

	score = 0
	for point in points:
		score *= 5
		score += point

	return score


answers = [get_answers(line) for line in incomplete_lines]

idx = len(answers) // 2
print(sorted(answers)[idx])
