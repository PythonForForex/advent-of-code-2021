from get_input import get_input


input = get_input(day=6)
input = [int(i) for i in input.split(',')]

for _ in range(80):
    input = [i - 1 for i in input]
    new_to_create = input.count(-1)
    if new_to_create:
        input += [8] * new_to_create
        input = [6 if i == -1 else i for i in input]


print(len(input))


'''
Part two
'''

import pandas as pd


input = get_input(day=6)
input = [int(i) for i in input.split(',')]

input_dict = {i: 0 for i in range(-1, 9)}

for val in input:
    input_dict[val] = input.count(val)

df = pd.DataFrame(input_dict.items())

for _ in range(256):
    df[1] = df[1].shift(-1)
    df.loc[9, 1] = df.loc[0, 1]
    df.loc[7, 1] += df.loc[0, 1]
    df.loc[0, 1] = 0.0


print(int(df[1].sum()))
