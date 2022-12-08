with open('input.txt') as input_file:
    lines = input_file.read().strip().split('\n')
    n = len(lines[0])
    trees = [[int(tree) for tree in line] for line in lines]

max_score = 1
for i in range(n):
    for j in range(n):
        scores = [0] * 4

        for k in range(i + 1, n):
            scores[0] += 1
            if trees[k][j] >= trees[i][j]:
                break

        for k in range(i - 1, -1, -1):
            scores[1] += 1
            if trees[k][j] >= trees[i][j]:
                break

        for k in range(j + 1, n):
            scores[2] += 1
            if trees[i][k] >= trees[i][j]:
                break

        for k in range(j - 1, -1, -1):
            scores[3] += 1
            if trees[i][k] >= trees[i][j]:
                break

        max_score = max(max_score, scores[0] * scores[1] * scores[2] * scores[3])

print(max_score)
