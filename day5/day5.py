from sys import stdin


def process(seeds, rmap):
    rseed = list()
    
    return rseed


data = stdin.readlines()

seeds = data[0].split(": ")[1].split()

i = 3
range_queue = list()
rmap = dict()
while i < len(data):
    if data[i][0].isdigit():
        dest_start, source_start, rlen = (int(x) for x in data[i].strip('\n').split())
        for i in range(source_start, source_start + rlen): 
            rmap[i] = dest_start + (i - source_start)

    if data[i][0].isalpha():
        seeds = process(seeds, rmap)
        print(seeds)
    i += 1

