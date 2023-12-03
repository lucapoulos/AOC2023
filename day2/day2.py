from sys import stdin

# Part 1
# def check_sets(sets, bag, id):
#     for val, color in [s.split(' ') for s in sets.split(', ')]:
#         if bag[color] < int(val):
#             return 0
#     return id

# sum = 0
# bag = {'blue': 14, 'red': 12, 'green': 13}
# for id, line in enumerate(stdin.readlines()):
#     x = line.strip('\n').split(': ')
#     sets = x[1].replace(';',',')
#     sum += check_sets(sets, bag, id+1)
# print(sum)

# Part 2

def check_sets(sets):
    max_bag = {'blue': 0, 'red': 0, 'green': 0}
    for val, color in [s.split(' ') for s in sets.split(', ')]:
        max_bag[color] = max(int(val), max_bag[color])
    return max_bag['blue'] * max_bag['green'] * max_bag['red']
sum = 0
for line in stdin.readlines():
    x = line.strip('\n').split(': ')
    sets = x[1].replace(';',',')
    sum += check_sets(sets)
print(sum)
