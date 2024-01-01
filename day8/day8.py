from sys import stdin


class location:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.name} = ({self.left}, {self.right})'
        

data = stdin.readlines()
moveset = data[0].strip('\n')

locations = dict()

for line in data[2:]:
    name, left, right = line[:3], line[7:10], line[12:15]
    loc = location(name,left,right)
    locations[loc.name] = loc

cur = locations['AAA']
i = 0
while cur.name != 'ZZZ':
    if moveset[i % len(moveset)] == 'R':
        cur = locations[cur.right]
    else:
        cur = locations[cur.left]
    i += 1

print(i)
