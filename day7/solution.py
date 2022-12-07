from collections import defaultdict

with open('input.txt') as input_file:
    tree = defaultdict(list)
    cwd = ('', )
    for line in input_file.read().strip().split('\n')[1:]:
        args = line.split(' ')
        if args[0] == '$':
            if args[1] == 'cd':
                cwd = cwd[:-1] if args[2] == '..' else cwd + (args[2], )
        elif args[0] == 'dir':
            tree[cwd].append(('dir', args[1], None))
        else:
            tree[cwd].append(('file', args[1], int(args[0])))


def get_size(path):
    return sum(
        size if type == 'file' else get_size(path + (name, ))
        for type, name, size in tree.get(path, [])
    )


def part1(max_size):
    return sum(size if (size := get_size(path)) <= max_size else 0 for path in tree)


def part2(available_size, unused_size):
    target_max_size = available_size - unused_size
    min_size_to_remove = root_size = get_size(('',))
    for path in tree:
        size = get_size(path)
        if root_size - size <= target_max_size and size < min_size_to_remove:
            min_size_to_remove = size

    return min_size_to_remove


print(part1(100_000))
print(part2(70_000_000, 30_000_000))
