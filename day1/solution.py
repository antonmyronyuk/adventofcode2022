with open('input.txt') as input_file:
    nums = input_file.read().split('\n')

elves = [[]]
for num in nums:
    if num == '':
        elves.append([])
    else:
        elves[-1].append(int(num))


sums = [sum(elf) for elf in elves]
print(max(sums))  # part 1

sorted_sums = sorted(sums, reverse=True)
print(sum(sorted_sums[:3]))  # part 2
