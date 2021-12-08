from get_input import get_input


input = get_input(day=4)
raw_input = input.split('\n\n')

number_draw = raw_input.pop(0).split()
number_draw = [int(i) for i in number_draw[0].split(',')]

all_boards = [i.splitlines() for i in raw_input]
boards_array = [
    [[int(i) for i in board.split()] for board in boards] for boards in all_boards
]

lowest_drawn = len(number_draw)
for idx, board in enumerate(boards_array):
    numbers = number_draw[:4]
    for num in number_draw[4:]:
        numbers.append(num)

        for range_idx in range(len(board[0])):
            horizontal = board[range_idx]
            vertical = [i[range_idx] for i in board]

            if all([i in numbers for i in horizontal]) or all(
                [i in numbers for i in vertical]
            ):
                drawn = len(numbers)

                if drawn < lowest_drawn:
                    lowest_drawn = drawn
                    lowest_idx = idx

                break
        else:
            continue

        break


best_board = boards_array[lowest_idx]
least_num_drawn = number_draw[:lowest_drawn]
best_board_nums = sum(best_board, [])
unmarked_sum = sum([i for i in best_board_nums if i not in least_num_drawn])

print(unmarked_sum * least_num_drawn[-1])


'''
Part two
'''


highest_drawn = 0
for idx, board in enumerate(boards_array):
    numbers = number_draw[:4]
    for num in number_draw[4:]:
        numbers.append(num)

        for range_idx in range(len(board[0])):
            horizontal = board[range_idx]
            vertical = [i[range_idx] for i in board]

            if all([i in numbers for i in horizontal]) or all(
                [i in numbers for i in vertical]
            ):
                drawn = len(numbers)

                if drawn > highest_drawn:
                    highest_drawn = drawn
                    highest_idx = idx

                break
        else:
            continue

        break


best_board = boards_array[highest_idx]
least_num_drawn = number_draw[:highest_drawn]
best_board_nums = sum(best_board, [])
unmarked_sum = sum([i for i in best_board_nums if i not in least_num_drawn])

print(unmarked_sum * least_num_drawn[-1])
