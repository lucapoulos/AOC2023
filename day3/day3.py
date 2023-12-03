from sys import stdin
import re

# Part 1
# def check_part(start, end):
#     above = list(range(start - n, end - n))
#     below = list(range(start + n, end + n))
#     cords = above + below
#     # If not on the edge, you can add diagonals and sides
#     if start % n != 0:
#         cords += [start - 1, start - 1 + n, start - 1 - n]
#     if (end + 1) % n != 0:
#         cords += [end, end + n, end - n]

#     # Remove out of index cords
#     cords = filter(lambda x: x >= 0 and x < len(bigdata), cords)
#     return any([bigdata[x] != '.' for x in cords])

# sum = 0
# bigdata = stdin.read()
# n = len(bigdata.split('\n')[0]) + 1
# for m in re.finditer(r'\d+', bigdata):
#     if check_part(m.start(), m.end()):
#         sum += int(m.group(0))
# print(sum)

# Part 2
def check_part(start, end):
    # check_part now returns a list of all stars around a part
    above = list(range(start - n, end - n))
    below = list(range(start + n, end + n))
    cords = above + below
    # If not on the edge, you can add diagonals and sides
    if start % n != 0:
        cords += [start - 1, start - 1 + n, start - 1 - n]
    if (end + 1) % n != 0:
        cords += [end, end + n, end - n]

    # Remove out of index cords
    cords = filter(lambda x: x >= 0 and x < len(bigdata), cords)
    return [x for x in cords if bigdata[x] == '*']

sum = 0
bigdata = stdin.read()
n = len(bigdata.split('\n')[0]) + 1
stars = dict()
for m in re.finditer(r'\d+', bigdata):
    for star in check_part(m.start(), m.end()):
        if star in stars and stars[star] != m:
            sum += int(stars[star].group()) * int(m.group())
        stars[star] = m
print(sum)
        
        

