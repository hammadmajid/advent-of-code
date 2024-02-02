with open("input.txt") as file:
    first_line = file.readline()


floor = 0

for char in first_line:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

print(floor)
