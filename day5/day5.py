from sys import stdin


def process(seeds, rmap):
    rseed = list()
    for m in rmap:
        for seed in seeds:
            if seed in m:
                rseed.append(m[seed][m.index(seed)])
    return rseed


data = stdin.readlines()

seeds = data[0].split(": ")[1].split()

i = 3
range_queue = list()
rmap = list()
while i < len(data):
    if data[i][0].isdigit():
        dest_start, source_start, rlen = (int(x) for x in data[i].strip('\n').split())
        rmap.append({range(source_start, source_start + rlen): range(dest_start, dest_start + rlen)})

    if data[i][0].isalpha():
        seeds = process(seeds, rmap)
        print(seeds)
    i += 1

