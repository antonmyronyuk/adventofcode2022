with open('input.txt') as input_file:
    lines = input_file.read().strip().split('\n')


def part1():
    x = 1
    cycles = 0
    res = 0

    def doc_inc_cycles():
        nonlocal cycles, res
        cycles += 1
        if cycles % 40 == 20:
            res += cycles * x

    for command in lines:
        if command == 'noop':
            doc_inc_cycles()
        else:
            doc_inc_cycles()
            doc_inc_cycles()
            x += int(command.split()[1])

    print(res)


def part2():
    x = 1
    cycles = 0
    img = []

    def doc_inc_cycles():
        nonlocal cycles, img
        img.append('#' if abs(x - cycles % 40) < 2 else '.')
        cycles += 1

    for command in lines:
        if command == 'noop':
            doc_inc_cycles()
        else:
            doc_inc_cycles()
            doc_inc_cycles()
            x += int(command.split()[1])

    for i in range(len(img) // 40):
        print(''.join(img[i * 40:(i + 1) * 40]))


part1()
part2()
