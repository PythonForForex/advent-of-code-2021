from get_input import get_input


raw_input = get_input(day=12)
raw_input = raw_input.splitlines()

paths_map = {}

for line in raw_input:
    a, b = line.split('-')
    paths_map.setdefault(a, []).append(b)
    paths_map.setdefault(b, []).append(a)


def main(custom_func):
    paths = [['start']]
    completed = []

    while paths:
        path = paths.pop()
        current_pos = path[-1]
        path_from_here = paths_map.get(current_pos)

        for potential in path_from_here:
            if potential == 'end' and path not in completed:
                completed.append(path)
                continue

            if potential.islower() and custom_func(potential, path):
                continue

            paths.append(path + [potential])

    return len(completed)


def part_one(potential, path):
    return potential in path


def part_two(potential, path):
    all_lower = [i for i in path if i.islower()]
    restriced = [i for i in set(all_lower) if all_lower.count(i) == 2]
    return restriced and potential in all_lower or potential == 'start'


print(main(part_one))
print(main(part_two))
