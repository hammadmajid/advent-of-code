def parse(line) -> tuple[int, int, int]:
    length = 0
    width = 0
    height = 0

    buffer = ""

    for char in line:
        if char != "x":
            buffer += char
        else:
            if length == 0:
                length = int(buffer)
            elif width == 0:
                width = int(buffer)
            elif height == 0:
                height = int(buffer)
            buffer = ""

    return (length, width, height)


total: int = 0

with open("input.txt") as file:
    content = file.readlines()

    for line in content:
        (length, width, height) = parse(line + "x")

        parameters = [
            (2 * length) + (2 * width),
            (2 * width) + (2 * height),
            (2 * height) + (2 * length),
        ]

        ribbon = min(parameters)
        bow = length * width * height

        total += ribbon + bow

print(total)
