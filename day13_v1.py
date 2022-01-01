from get_input import get_input
import numpy as np

raw_input = get_input(day=13)

dot_location, fold_location = raw_input.split('\n\n')
dot_location = [[int(x) for x in line.split(',')] for line in dot_location.splitlines()]
fold_location = [i.split()[-1] for i in fold_location.splitlines()]

array_max_x = max([i[0] for i in dot_location])
array_max_y = max([i[1] for i in dot_location])

dot_array = np.ones([array_max_y + 1, array_max_x + 1])

for x, y in dot_location:
	dot_array[y,x] = 0

for folds in fold_location[0]:
	x = y = None
	exec(folds)
	if x:
		folded_array = dot_array[:, x+1:]
		folded_array = np.flip(folded_array, 1)
		dot_array = dot_array[:, :x]
	elif y:
		folded_array = dot_array[y+1:, :]
		folded_array = np.flip(folded_array, 0)
		dot_array = dot_array[:y, :]
		
dot_array = dot_array * folded_array
print(np.count_nonzero(dot_array == 0))
