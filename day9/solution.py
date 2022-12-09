with open('input.txt') as input_file:
    moves = []
    for line in input_file.read().strip().split('\n'):
        direction, distance = line.split()
        moves.append((direction, int(distance)))

dir_to_offset = {
    'U': (-1, 0),  # positions will be negative
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}


def sign(diff):
    return diff and diff // abs(diff)


def get_tail_visited_positions_count(size):
    visited = set()
    pos = [(0, 0) for _ in range(size)]
    for dir, dist in moves:
        offset = dir_to_offset[dir]
        for _ in range(dist):
            pos[0] = pos[0][0] + offset[0], pos[0][1] + offset[1]
            for i in range(1, size):
                diffs = pos[i - 1][0] - pos[i][0], pos[i - 1][1] - pos[i][1]
                if (
                    (abs(diffs[1]) > 1 and abs(diffs[0]) >= 0)
                    or (abs(diffs[0]) > 1 and abs(diffs[1]) >= 0)
                ):
                    pos[i] = pos[i][0] + sign(diffs[0]), pos[i][1] + sign(diffs[1])

            visited.add(pos[-1])

    return len(visited)


print(get_tail_visited_positions_count(2))  # part 1
print(get_tail_visited_positions_count(10))  # part 2
