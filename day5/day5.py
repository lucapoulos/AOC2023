from sys import stdin


def process(seeds, rmap):
    rseed = list()
    for seed in seeds:
        if seed in rmap:
            rseed.append(rmap[seed])
        else:
            rseed.append(seed)
    return rseed


data = stdin.readlines()

seeds = [int(x) for x in data[0].split(": ")[1].split()]

i = 3
rmap = dict()
while i < len(data):
    if data[i][0].isdigit():
        dest_start, source_start, rlen = (int(x) for x in data[i].strip('\n').split())
        for j in range(source_start, source_start + rlen): 
            rmap[j] = dest_start + (j - source_start)

    # Does not call process on last map...
    if data[i][0].isalpha():
        seeds = process(seeds, rmap)
        print(data[i],seeds)
        rmap = dict()
    i += 1
print(min(process(seeds,rmap)))
