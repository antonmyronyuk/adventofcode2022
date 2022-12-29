from collections import deque

with open('input.txt') as input_file:
    field = [list(line) for line in input_file.read().strip().split('\n')]
    n, m = len(field), len(field[0])
    visited_map = [[0] * m for _ in range(n)]


start = next((i, j) for i in range(n) for j in range(m) if field[i][j] == 'S')
end = next((i, j) for i in range(n) for j in range(m) if field[i][j] == 'E')
field[start[0]][start[1]], field[end[0]][end[1]] = 'a', 'z'

queue = deque([(end, 1)])
while queue:
    (i, j), distance = queue.popleft()
    if visited_map[i][j]:
        continue

    visited_map[i][j] = distance
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = i + di, j + dj
        if (
            0 <= ni < n
            and 0 <= nj < m
            and ord(field[i][j]) - ord(field[ni][nj]) < 2
        ):
            queue.append(((ni, nj), distance + 1))


print(visited_map[start[0]][start[1]] - 1)  # part 1
shortest_distance = min(
    visited_map[i][j] for i in range(n) for j in range(m)
    if field[i][j] == 'a' and visited_map[i][j]
)
print(shortest_distance - 1)  # part 2
