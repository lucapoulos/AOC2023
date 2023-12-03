from sys import stdin

# Part 1
# sum = 0
# for line in stdin.readlines():
#     left, right = 0, -1

#     while not line[left].isdigit():
#         left += 1
#     while not line[right].isdigit():
#         right -= 1
#     sum += int(line[left]) * 10 + int(line[right])
# print(sum)

sum = 0
valid_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def check_word(word):
    for key in valid_numbers:
        if key in word:
            return valid_numbers[key]
    return 0

for line in stdin.readlines():
    left, right = 0, -1
    l_w, r_w = 0, 0
    while not line[left].isdigit():
        l_w = check_word(line[:left])
        if l_w:
            break
        left += 1
    
    while not line[right].isdigit():
        r_w = check_word(line[right:])
        if r_w:
            break
        right -= 1
    
    if l_w == 0:
        l_w = line[left]
    if r_w == 0:
        r_w = line[right]
    print(l_w, r_w)
    sum += 10 * int(l_w) + int(r_w)
print(sum)

