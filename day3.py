from get_input import get_input

input = get_input(day=3)
input = input.splitlines()


gamma_rate = ''
epsilon_rate = ''
for i in range(len(input[0])):
    all_bits = [b[i] for b in input]
    zeros = all_bits.count('0')
    ones = all_bits.count('1')

    gamma_rate += '0' if zeros > ones else '1'
    epsilon_rate += '0' if zeros < ones else '1'

    if zeros == ones:
        raise AssertionError('Unexpected result')


print(int(gamma_rate, 2) * int(epsilon_rate, 2))


'''
Part two
'''


def get_rating(revised_input, dominant=True):
    for i in range(len(revised_input[0])):
        all_bits = [b[i] for b in revised_input]
        zeros = all_bits.count('0')
        ones = all_bits.count('1')

        idx_key = '0' if zeros > ones else '1'
        if not dominant:
            idx_key = '0' if zeros <= ones else '1'

        revised_input = [b for b in revised_input if b[i] == idx_key]

        if len(revised_input) == 1:
            return int(revised_input[0], 2)


generator = get_rating(input)
scrubber = get_rating(input, dominant=False)

print(generator * scrubber)
