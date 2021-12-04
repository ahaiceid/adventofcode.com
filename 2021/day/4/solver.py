#!/usr/bin/python3

from itertools import chain

def read_in_chunks(file_handle):
    ''' Lazy function (generator) to read a file in chunks separated by double-newlines. '''
    data = []
    for line in file_handle:
        line = line.strip()
        if line:
            data.append(line)
        else:
            yield data
            data.clear()
    yield data

def decode_plays(chunk):
    return [int(v) for v in chunk[0].split(",")]

def decode_board(chunk):
    board = []
    for row in chunk:
        board.append([[int(v),False] for v in row.split()])
    return board

def update_board(board, play):
    for row in board:
        for value in row:
            if value[0] == play:
                value[1] = True
                return

def score_board(board):
    return sum([value[0] for value in chain(*board) if not value[1]])

def win_condition(board):
    for row in board:
        if len([1 for value in row if value[1] == True]) == 5:
            return True
    transposed_board = map(list,zip(*board))
    for row in transposed_board:
        if len([1 for value in row if value[1] == True]) == 5:
            return True

def play1(plays, boards):
    for play in plays:
        for board in boards:
            update_board(board, play)
            if win_condition(board):
                print(score_board(board)*play)
                return

def play2(plays, boards):
    boards = {i: b for i, b in enumerate(boards)}
    non_winning_boards = set(boards.keys())
    for play in plays:
        for k, board in boards.items():
            update_board(board, play)
            if win_condition(board):
                try:
                    non_winning_boards.remove(k)
                except KeyError:
                    pass
            if len(non_winning_boards) == 0:
                print(board)
                print(score_board(boards[k]) * play)
                return

def main():
    with open("input") as fh:
        plays = None
        boards = []
        for chunk in read_in_chunks(fh):
            if not plays:
                plays = decode_plays(chunk)
            else:
                boards.append(decode_board(chunk))
    play1(plays, boards)
    play2(plays, boards)

if __name__ == "__main__":
    main()