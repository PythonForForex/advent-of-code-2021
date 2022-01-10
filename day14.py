from get_input import get_input
from collections import Counter, defaultdict


raw_input = get_input(day=14)
begin, rules = raw_input.split('\n\n')
rules_dict = {rule[:2]: rule[-1] for rule in rules.splitlines()}


def main(steps):
    polymer = {k: begin.count(k) for k in rules_dict}
    counts = Counter(begin)

    for _ in range(steps):
        next_polymer = defaultdict(int)
        for k, v in polymer.items():
            new_val = rules_dict[k]
            next_polymer[k[0] + new_val] += v
            next_polymer[new_val + k[1]] += v
            counts[new_val] += v
        polymer = next_polymer

    most = counts.most_common()[0][1]
    least = counts.most_common()[-1][1]
    return most - least


print('Part 1: ', main(10))
print('Part 2: ', main(40))
