from get_input import get_input
from statistics import median


input = get_input(day=7)
input = [int(i) for i in input.split(',')]

allign_to = median(input)

print(sum([abs(i - allign_to) for i in input]))


'''
Part two
'''


allign_to = [
    sum([i + 1 for start_pos in input for i in range(abs(potential_pos - start_pos))])
    for potential_pos in range(min(input), max(input) + 1)
]

print(min(allign_to))


## For reference - optimized for speed

allign_to = [
    sum([abs(potential_pos - start_pos) * (abs(potential_pos - start_pos) + 1) / 2 for start_pos in input])
    for potential_pos in range(min(input), max(input) + 1)
]

print(min(allign_to))

