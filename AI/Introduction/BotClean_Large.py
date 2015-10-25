#!/usr/bin/python
def manhattan_min(pos_bot, pos_d):
    man_min = 1000000
    bot_r, bot_c = pos_bot
    for pos in pos_d:
        d_r, d_c = pos
        man_sum = abs(d_r - bot_r) + abs(d_c - bot_c)
        if man_sum < man_min:
            man_min = man_sum
    return man_min
       
def next_move(posr, posc, dimh, dimw, board):
    pos_bot = (posr, posc)
    pos_d = []
    for row_idx, row in enumerate(board):
        d_found = []
        for d_idx, r in enumerate(row):
            if r == 'd':
                d_found.append(d_idx)
        for d_col in d_found:
            pos_d.append((row_idx, d_col))
    if pos_bot in pos_d:
        print "CLEAN"
    else:
        moves = {}
        moves["UP"] = (posr - 1, posc)
        moves["DOWN"] = (posr + 1, posc)
        moves["LEFT"] = (posr, posc - 1)
        moves["RIGHT"] = (posr, posc + 1)
        min_min = 1000000
        best_move = ""
        for move in moves:
            pos_new = moves[move]
            new_r, new_c = pos_new
            if new_r < 0 or new_r >= dimh:
                continue
            elif new_c < 0 or new_c >= dimw:
                continue
            else:
                new_min = manhattan_min(pos_new, pos_d)
                if new_min <= min_min:
                    best_move = move
                    min_min = new_min
        print best_move
        
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)