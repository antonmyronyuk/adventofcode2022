import json
from itertools import chain, zip_longest

with open('input.txt') as input_file:
    pairs = [
        [json.loads(line) for line in pair.split('\n')]
        for pair in input_file.read().strip().split('\n\n')
    ]


def comp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a <= b

    if isinstance(a, int) and isinstance(b, list):
        a = [a]
    elif isinstance(a, list) and isinstance(b, int):
        b = [b]

    for i, j in zip_longest(a, b, fillvalue=None):
        if i is not None and j is not None and i != j:
            return comp(i, j)
        if i is not None and j is None:
            return False
        if j is not None and i is None:
            return True

    return True


print(sum(i for i, pair in enumerate(pairs, start=1) if comp(*pair)))  # part 1

divs = [[[2]], [[6]]]
packets = list(chain.from_iterable(pairs)) + divs

for i in range(len(packets)):
    for j in range(len(packets)):
        if comp(packets[i], packets[j]):
            packets[i], packets[j] = packets[j], packets[i]

print((packets.index(divs[0]) + 1) * (packets.index(divs[1]) + 1))  # part 2
