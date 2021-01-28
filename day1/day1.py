import itertools
in_file = r"C:\qpipe\python\advent_of_code\day1\input.txt"
expenses = list()
with open(in_file, "r") as f:
    for line in f.readlines():
        expenses.append(int(line))

for val1, val2 in itertools.combinations(expenses, 2):
    if val1 + val2 == 2020:
        break
else:
    print("No result!")

result = val1 * val2
print(val1, val2)
print("Part1: {0}".format(result))

for val1, val2, val3 in itertools.combinations(expenses, 3):
    if val1 + val2 + val3 == 2020:
        break
else:
    print("No result!")

result = val1 * val2 * val3
print(val1, val2, val3)
print("Part2: {0}".format(result))
