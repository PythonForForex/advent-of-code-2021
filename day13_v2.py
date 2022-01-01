from get_input import get_input

raw_input = get_input(day=13)

dot_location, fold_locations = raw_input.split('\n\n')
dot_location = [[int(x) for x in line.split(',')] for line in dot_location.splitlines()]
fold_locations = [i.split()[-1].split('=') for i in fold_locations.splitlines()]

def to_mirror(val, fold_axis, max_val):
	val[fold_axis] = abs(val[fold_axis] - max_val)
	return val


fold = fold_locations[0]
fold_val = int(fold[1])
fold_axis = 0 if fold[0] == 'x' else 1
main_dots = [i for i in dot_location if i[fold_axis] < fold_val]
max_val = max([i[fold_axis] for i in dot_location])
folded_dots = [to_mirror(i, fold_axis, max_val) for i in dot_location if i not in main_dots]
main_dots += [i for i in folded_dots if i[fold_axis] < fold_val and i not in main_dots]

print(len(main_dots))
