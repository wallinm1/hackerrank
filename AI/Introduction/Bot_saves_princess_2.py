#!/bin/python
def nextMove(n,r,c,grid):
    for row_idx, row_str in enumerate(grid):
        m_found = row_str.find('m')
        if m_found != -1:
            m_row = row_idx
            m_col = m_found
        p_found = row_str.find('p')
        if p_found != -1:
            p_row = row_idx
            p_col = p_found
    if m_row < p_row:
        ret_str = 'DOWN'
    if m_row > p_row:
        ret_str = 'UP'
    if m_col < p_col:
        ret_str = 'RIGHT'
    if m_col > p_col:
        ret_str = 'LEFT'
    return ret_str

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
