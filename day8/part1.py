with open('input.txt') as input_file:
    lines = input_file.read().strip().split('\n')
    n = len(lines[0])
    trees = [[int(tree) for tree in line] for line in lines]


visible_map = [[False] * n for _ in range(n)]

for i in range(n):
    last_visible = -1
    for j in range(n):
        if trees[i][j] > last_visible:
            visible_map[i][j] = True
            last_visible = trees[i][j]

for i in range(n):
    last_visible = -1
    for j in range(n - 1, -1, -1):
        if trees[i][j] > last_visible:
            visible_map[i][j] = True
            last_visible = trees[i][j]

for j in range(n):
    last_visible = -1
    for i in range(n):
        if trees[i][j] > last_visible:
            visible_map[i][j] = True
            last_visible = trees[i][j]

for j in range(n):
    last_visible = -1
    for i in range(n - 1, -1, -1):
        if trees[i][j] > last_visible:
            visible_map[i][j] = True
            last_visible = trees[i][j]


print(sum(sum(row) for row in visible_map))
