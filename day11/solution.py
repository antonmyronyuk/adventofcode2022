import dataclasses
import math
from typing import Callable

with open('input.txt') as input_file:
    monkeys_data = input_file.read().strip().split('\n\n')


@dataclasses.dataclass
class Monkey:
    div: int
    index_true: int
    index_false: int
    items: list[int]
    operation: Callable[[int], int]
    inspect_count: int = 0

    @classmethod
    def parse(cls, data: str) -> 'Monkey':
        lines = data.split('\n')
        operation_return = lines[2].split(' = ')[-1]
        return cls(
            div=int(lines[3].split(' ')[-1]),
            items=[int(num) for num in lines[1].split(':')[1].strip().split(', ')],
            index_true=int(lines[4].split(' ')[-1]),
            index_false=int(lines[5].split(' ')[-1]),
            operation=eval(f'lambda old: {operation_return}')
        )


def process_worry_levels(rounds: int, divider: int) -> int:
    monkeys = [Monkey.parse(data) for data in monkeys_data]
    dividers_lcm = math.lcm(*[monkey.div for monkey in monkeys])
    for _ in range(rounds):
        for monkey in monkeys:
            cur_items = monkey.items
            monkey.items = []
            for item in cur_items:
                new_item = monkey.operation(item) // divider % dividers_lcm
                dividable = new_item % monkey.div == 0
                index = monkey.index_true if dividable else monkey.index_false
                monkeys[index].items.append(new_item)
                monkey.inspect_count += 1

    a, b = sorted(monkey.inspect_count for monkey in monkeys)[-2:]
    return a * b


print(process_worry_levels(20, 3))  # part 1
print(process_worry_levels(10000, 1))  # part 2
