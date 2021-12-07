from get_input import get_input

input = get_input()
input = [int(i) for i in input.splitlines()]

def get_increasing(input):
	start = 0
	last_value = None

	for value in input:
		if last_value:
			if value > last_value:
				start +=1
		last_value = value


	return start


print(get_increasing(input))


'''
Part two 
'''

import pandas as pd

df = pd.DataFrame(input)
sums = df[0].rolling(3).sum().dropna()
input2 = sums.astype('int32').to_list()

print(get_increasing(input2))
