from sys import stdin

# Part 1
# points = 0
# for line in stdin.readlines():
#     x = line.split(':')[1].split('|')
#     winning = {e for e in x[0].strip().split()}
#     yours = {e for e in x[1].strip(' \n').split()}
#     z = winning.intersection(yours)
#     if z:
#         points += 2 ** (len(z) - 1)
# print(points)

# Part 2
scratchcards = 0
data = stdin.readlines()
cards = [0 for _ in data]
for id, line in enumerate(data):
    cards[id] += 1
    x = line.split(':')[1].split('|')
    winning = {e for e in x[0].strip().split()}
    yours = {e for e in x[1].strip(' \n').split()}
    z = winning.intersection(yours)
    if z:
        cards[id+1: id+1 + len(z)] = [cards[id] + x for x in cards[id+1: id+1 + len(z)]]
    scratchcards += cards[id]

print(scratchcards)
