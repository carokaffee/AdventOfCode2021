from src.tools.loader import load_data

TESTING = True


def apply_bingo_game(bingo_data):
    drawn_numbers = list(map(int, bingo_data[0].split(',')))
    bingo_boards = [[list(map(int, row.split())) for row in board.split('\n')] for board in bingo_data[1:]]
    bingo_winners = [0 for _ in range(len(bingo_boards))]
    winning_board_score = 0
    losing_board_score = 0
    for i, drawn_number in enumerate(drawn_numbers):
        cross_out_number(bingo_boards, bingo_winners, drawn_number)
        if sum(bingo_winners) == 1 and winning_board_score == 0:
            winning_index = bingo_winners.index(1)
            winning_board_score = get_board_score(bingo_boards[winning_index], drawn_number)
        if sum(bingo_winners) == len(bingo_boards) - 1 and losing_board_score == 0:
            losing_index = bingo_winners.index(0)
            next_drawn_number = drawn_numbers[i + 1]
            cross_out_number(bingo_boards, bingo_winners, next_drawn_number)
            losing_board_score = get_board_score(bingo_boards[losing_index], next_drawn_number)
    return winning_board_score, losing_board_score


def cross_out_number(boards, winners, number):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            board[j] = [-1 if elem == number else elem for elem in row]
        if has_won(board):
            winners[i] = 1


def has_won(board):
    for row in board:
        if all([(elem == -1) for elem in row]):
            return True
    for col_idx in range(len(board[0])):
        col = [board[row_idx][col_idx] for row_idx in range(len(board))]
        if all([(elem == -1) for elem in col]):
            return True
    return False


def get_board_score(board, number):
    board_score = 0
    for row in board:
        for elem in row:
            board_score += max(elem, 0)
    return board_score * number


if __name__ == '__main__':
    data = load_data(TESTING, '\n\n')
    score_1, score_2 = apply_bingo_game(data)
    print(score_1)
    print(score_2)
