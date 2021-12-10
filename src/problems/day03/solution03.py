from src.tools.loader import load_data

TESTING = True


def find_most_common_digit(bin_numbers, pos: int):
    counter = 0
    for bin_number in bin_numbers:
        counter += 1 if bin_number[pos] == '1' else -1
    return counter


def find_gamma_and_epsilon(bin_numbers):
    number_length = len(bin_numbers[0])
    gam = ''
    eps = ''
    for pos in range(number_length):
        common = find_most_common_digit(bin_numbers, pos)
        gam += '1' if common > 0 else '0'
        eps += '1' if common < 0 else '0'
    return gam, eps


def filter_bin_numbers(bin_numbers, keep: str, drop: str):
    remaining = set(bin_numbers)
    number_length = len(bin_numbers[0])
    for pos in range(number_length):
        most_common_digit = find_most_common_digit(list(remaining), pos)
        if len(remaining) > 1:
            if most_common_digit >= 0:
                remaining = set([bin_number for bin_number in remaining if bin_number[pos] == keep])
            else:
                remaining = set([bin_number for bin_number in remaining if bin_number[pos] == drop])
    return remaining


if __name__ == '__main__':
    data = load_data(TESTING, '\n')
    gamma, epsilon = find_gamma_and_epsilon(data)
    oxygen, = filter_bin_numbers(data, '1', '0')
    co2, = filter_bin_numbers(data, '0', '1')
    solution_1 = int(gamma, 2) * int(epsilon, 2)
    solution_2 = int(oxygen, 2) * int(co2, 2)
    print(solution_1)
    print(solution_2)
