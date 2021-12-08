from src.tools.loader import load_data

TESTING = True


def count_increase(numbers):
    counter = 0
    prev = numbers[0]
    for depth in numbers:
        counter += depth > prev
        prev = depth
    return counter


def count_sum_increase(numbers):
    counter = 0
    for i in range(3, len(numbers)):
        counter += numbers[i] > numbers[i - 3]
    return counter


if __name__ == '__main__':
    data = load_data(TESTING, '\n')
    depths = list(map(int, data))
    solution_1 = count_increase(depths)
    solution_2 = count_sum_increase(depths)

    print(solution_1)
    print(solution_2)
