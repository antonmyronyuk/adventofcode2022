import copy

with open('input.txt') as input_file:
    lines = [line for line in input_file.read().split('\n')]
    input_delimiter = lines.index('')

stacks_number = (len(lines[0]) + 1) // 4
stacks = [[] for _ in range(stacks_number)]
for line in reversed(lines[:input_delimiter - 1]):
    for stack_index in range(stacks_number):
        crate = line[stack_index * 4 + 1]
        if crate != ' ':
            stacks[stack_index].append(crate)

moves = [
    [int(num) for num in line.split() if num.isdigit()]
    for line in lines[input_delimiter:]
    if line
]


def make_moves(stacks, reverse):
    for count, move_from, move_to in moves:
        moved = stacks[move_from - 1][-count:]
        stacks[move_to - 1] += reversed(moved) if reverse else moved
        stacks[move_from - 1] = stacks[move_from - 1][:-count]

    return ''.join(stack[-1] for stack in stacks)


print(make_moves(copy.deepcopy(stacks), reverse=True))  # part 1
print(make_moves(copy.deepcopy(stacks), reverse=False))  # part 2
