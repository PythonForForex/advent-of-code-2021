from get_input import get_input
import numpy as np


raw_input = get_input(day=11)

matrix = [[int(i) for i in line] for line in raw_input.splitlines()]
matrix = np.array(matrix)

shape_x, shape_y = matrix.shape
overlap_array = np.zeros((shape_x + 2, shape_y + 2))
zeros_array = np.zeros((shape_x, shape_y))

flashes = 0
steps = 100

answer_part1 = None
answer_part2 = None

for step_num in range(1, steps ** steps):
    checked = []
    matrix += 1
    overlap_array[1:shape_x+1, 1:shape_y+1] = matrix

    while True:
        matrix = overlap_array[1:shape_x+1, 1:shape_y+1]
        nine_idx = np.nonzero(matrix > 9)
        idxs = [[x, y] for x, y in zip(*nine_idx) if [x, y] not in checked]

        if not idxs:
            break

        for x, y in idxs:
            for x_shift in range(3):
                for y_shift in range(3):
                    overlap_array[x + x_shift, y + y_shift] += 1

            checked.append([x, y])

    matrix = np.where(matrix <= 9, matrix, 0)
    flashes += np.count_nonzero(matrix == 0)

    if step_num == steps:
        answer_part1 = flashes

    if np.array_equal(matrix, zeros_array):
        answer_part2 = step_num

    if answer_part1 and answer_part2:
        break


print(answer_part1)
print(answer_part2)
