# -*- coding: utf-8 -*-

import time
import copy


board = \
"000000000000000"\
"000010000000000"\
"000001000000000"\
"000111000000000"\
"000000000000000"\
"000000000000000"\
"000000000000000"\
"000000000000000"\
"000000000000000"\
"000000000000000"


def read_board(width):
    board_state =[]
    assert len(board) % width == 0
    for i in range(len(board) // width):
        board_line = board[i*width:(i+1)*width]
        board_state.append([int(b) for b in board_line])
    return board_state


def update(board_state):
    tmp_state = copy.deepcopy(board_state)
    for i, board_line in enumerate(board_state):
        for j in range(len(board_line)):
            around_state = board_state[i-1][j-1] + board_state[i-1][j] + board_state[i-1][(j+1)%len(board_line)] \
                            + board_line[j-1] + board_line[(j+1)%len(board_line)] \
                            + board_state[(i+1)%len(board_state)][j-1] + board_state[(i+1)%len(board_state)][j] \
                            + board_state[(i+1)%len(board_state)][(j+1)%len(board_line)]
            if around_state <= 1:
                tmp_state[i][j] = 0
            elif around_state == 3:
                tmp_state[i][j] = 1
            elif around_state >= 4:
                tmp_state[i][j] = 0
    return tmp_state


def board_view(board_state):
    for board_line in board_state:
        print(''.join('.' if b == 0 else '@' for b in board_line))
    print()


def main():
    board_state = read_board(15)
    board_view(board_state)
    while True:
        time.sleep(0.1)
        board_state = update(board_state)
        board_view(board_state)


if __name__ == '__main__':
    main()
