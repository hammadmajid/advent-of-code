with open("input.txt") as file:
    first_line = file.readline()


floor = 0

for i, char in enumerate(first_line):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

    if floor == -1:
        print(i + 1)
        exit(0)
