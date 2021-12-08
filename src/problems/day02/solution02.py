from src.tools.loader import load_data

TESTING = True


def solve_part_1(commands):
    horiz = 0
    depth = 0
    for command in commands:
        instruction, number = command.split()
        if instruction == 'down':
            depth += int(number)
        if instruction == 'up':
            depth -= int(number)
        if instruction == 'forward':
            horiz += int(number)
    return horiz * depth


def solve_part_2(commands):
    horiz = 0
    depth = 0
    aim = 0
    for command in commands:
        instruction, number = command.split()
        if instruction == 'down':
            aim += int(number)
        if instruction == 'up':
            aim -= int(number)
        if instruction == 'forward':
            horiz += int(number)
            depth += aim * int(number)
    return horiz * depth


if __name__ == '__main__':
    data = load_data(TESTING, '\n')
    print(solve_part_1(data))
    print(solve_part_2(data))
