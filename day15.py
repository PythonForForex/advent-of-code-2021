from get_input import get_input
import numpy as np


def get_new_paths(x, y, max_x, max_y):
    new = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [i for i in new if 0 <= i[0] < max_x and 0 <= i[1] < max_y]


def main(matrix):
    max_x, max_y = matrix.shape

    cost_map = {}
    for x in range(max_x):
        for y in range(max_y):
            cost_map[x, y] = matrix.max() * sum(matrix.shape)

    start_paths = [[0, (0, 0)]]

    while start_paths:
        start_paths.sort()
        cost, start = start_paths.pop(0)

        new_paths = get_new_paths(*start, max_x, max_y)

        for path in new_paths:
            new_cost = cost + matrix[path]

            if new_cost < cost_map[path]:
                cost_map[path] = new_cost
                start_paths.append([new_cost, path])

    return cost_map[max_x-1, max_y-1]


raw_input = get_input(day=15)
matrix = np.array([list(i) for i in raw_input.splitlines()]).astype(int)

print(main(matrix))  # Part 1

for ax in [1, 0]:
    new_matrix_piece = matrix.copy()
    for i in range(4):
        new_matrix_piece += 1
        new_matrix_piece = np.where(new_matrix_piece <= 9, new_matrix_piece, 1)
        matrix = np.concatenate((matrix, new_matrix_piece), axis=ax)

print(main(matrix))  # Part 2
