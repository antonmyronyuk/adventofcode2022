import re

with open('input.txt') as input_file:
    assignments = [
        [int(num) for num in re.split(r'[-,]', line)]
        for line in input_file.read().split('\n')
        if line
    ]


def is_fully_overlap(start1, finish1, start2, finish2):
    return (
        start1 <= start2 <= finish2 <= finish1
        or start2 <= start1 <= finish1 <= finish2
    )


def is_partially_overlap(start1, finish1, start2, finish2):
    return max(start1, start2) <= min(finish1, finish2)


# part 1
print(sum(is_fully_overlap(*assignment) for assignment in assignments))

# part 2
print(sum(is_partially_overlap(*assignment) for assignment in assignments))
