from get_input import get_input


input = get_input(day=5)
raw_input = [i.split('->') for i in input.splitlines()]


# Flatten
flat = [item.strip() for line in raw_input for item in line]
cleaned = [a.split(',') for a in flat]
flat_ints = [int(i) for i in sum(cleaned, [])]
max_val = max(flat_ints) + 1

#  Empty array
diagram = [[0 for i in range(max_val)] for j in range(max_val)]

for line in raw_input:

    x1, y1 = [int(i.strip()) for i in line[0].split(',')]
    x2, y2 = [int(i.strip()) for i in line[1].split(',')]

    if x1 == x2:
        range_start, range_end = sorted([y1, y2])
        y_vals = [i for i in range(range_start, range_end + 1)]
        for val in y_vals:
            diagram[val][x1] += 1

    if y1 == y2:
        range_start, range_end = sorted([x1, x2])
        x_vals = [i for i in range(range_start, range_end + 1)]
        for val in x_vals:
            diagram[y1][val] += 1


flatten_list = sum(diagram, [])
answer = [i for i in flatten_list if i >= 2]

print(len(answer))


'''
Part two
'''


diagram = [[0 for i in range(max_val)] for j in range(max_val)]

for line in raw_input:

    x1, y1 = [int(i.strip()) for i in line[0].split(',')]
    x2, y2 = [int(i.strip()) for i in line[1].split(',')]

    range_start, range_end = sorted([y1, y2])
    y_vals = [i for i in range(range_start, range_end + 1)]
    if x1 == x2:
        for val in y_vals:
            diagram[val][x1] += 1

    range_start, range_end = sorted([x1, x2])
    x_vals = [i for i in range(range_start, range_end + 1)]
    if y1 == y2:
        for val in x_vals:
            diagram[y1][val] += 1

    # Add diagonals

    if len(x_vals) == len(y_vals):
        x_vals = x_vals if x1 < x2 else x_vals[::-1]
        y_vals = y_vals if y1 < y2 else y_vals[::-1]

        for coordinates in zip(y_vals, x_vals):
            diagram[coordinates[0]][coordinates[1]] += 1


flatten_list = sum(diagram, [])
answer = [i for i in flatten_list if i >= 2]

print(len(answer))
