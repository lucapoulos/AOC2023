from sys import stdin
import re

def check_part(start, end):
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
    return any([bigdata[x] != '.' for x in cords])

sum = 0
bigdata = stdin.read()
n = len(bigdata.split('\n')[0]) + 1
for m in re.finditer(r'\d+', bigdata):
    if check_part(m.start(), m.end()):
        sum += int(m.group(0))
print(sum)
