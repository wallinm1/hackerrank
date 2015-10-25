#!/usr/bin/python
import os
import pickle

def manhattan_min(pos_bot, pos_d):
    man_min = 1000000
    bot_r, bot_c = pos_bot
    for pos in pos_d:
        d_r, d_c = pos
        man_sum = abs(d_r - bot_r) + abs(d_c - bot_c)
        if man_sum < man_min:
            man_min = man_sum
    return man_min

def legal_moves(pos, board_height, board_width):
    posr, posc = pos
    moves = {}
    moves["UP"] = (posr - 1, posc)
    moves["DOWN"] = (posr + 1, posc)
    moves["LEFT"] = (posr, posc - 1)
    moves["RIGHT"] = (posr, posc + 1)
    legal_moves = moves.copy()
    for move in moves:
        pos_new = moves[move]
        new_r, new_c = pos_new
        if new_r < 0 or new_r >= board_height or new_c < 0 or new_c >= board_width:
            del legal_moves[move]
    return legal_moves
        
def next_move(posr, posc, board):
    board_height = len(board)
    board_width = len(board[0])
    pos_bot = (posr, posc)
    fname = 'state.txt'
    if os.path.isfile(fname):
        with open(fname, 'rb') as handle:
            board_dict = pickle.loads(handle.read())
    else:
        board_dict = {}
        for row_idx in range(board_height):
            for col_idx in range(board_width):
                board_dict[(row_idx, col_idx)] = 'o'
    for row_idx, row in enumerate(board):
        for col_idx, elem in enumerate(row):
            if elem == 'd':
                board_dict[(row_idx, col_idx)] = 'd'
            elif elem == '-':
                board_dict[(row_idx, col_idx)] = '-'
    d_found = []
    o_found = []
    clean_found = []
    for pos in board_dict:
        if board_dict[pos] == 'd':
            d_found.append(pos)
        elif board_dict[pos] == 'o':
            o_found.append(pos)
        else:
            clean_found.append(pos)
    if pos_bot in d_found:
        print "CLEAN"
        board_dict[pos_bot] = '-'
        with open(fname, 'wb') as handle:
            pickle.dump(board_dict, handle)
    else:
        moves = legal_moves(pos_bot, board_height, board_width)
        min_min = 1000000
        best_move = ""
        for move in moves:
            pos_new = moves[move]
            if len(d_found)>0:
                new_min = manhattan_min(pos_new, d_found)
            elif len(o_found)>0:
                new_min = manhattan_min(pos_new, o_found)
            else: #len(clean_found)>0:
                new_min = manhattan_min(pos_new, clean_found)
            if new_min < min_min:
                best_move = move
                min_min = new_min
        with open(fname, 'wb') as handle:
            pickle.dump(board_dict, handle)
        print best_move
        
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)