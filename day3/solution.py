with open('input.txt') as input_file:
    lines = [line for line in input_file.read().split('\n') if line]


def get_char_score(char):
    num = ord(char)
    return num - 96 if num > 96 else num - 38


score = 0
for line in lines:
    half = len(line) // 2
    p1, p2 = set(line[:half]), set(line[half:])
    common = set(p1) & set(p2)
    score += get_char_score(common.pop())


print(score)  # part 1


score = 0
for i in range(0, len(lines), 3):
    r1, r2, r3 = lines[i:i + 3]
    common = set(r1) & set(r2) & set(r3)
    score += get_char_score(common.pop())


print(score)  # part 2
