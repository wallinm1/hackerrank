#!/bin/python
def displayPathtoPrincess(n,grid):
    for row_idx, row_str in enumerate(grid):
        m_found = row_str.find('m')
        if m_found != -1:
            m_row = row_idx
            m_col = m_found
        p_found = row_str.find('p')
        if p_found != -1:
            p_row = row_idx
            p_col = p_found
    ret_str = ''
    vert_diff = abs(m_row - p_row)
    horiz_diff = abs(m_col - p_col)
    if m_row < p_row:
        ret_str += vert_diff*'DOWN\n'
    if m_row > p_row:
        ret_str += vert_diff*'UP\n'
    if m_col < p_col:
        ret_str += horiz_diff*'RIGHT\n'
    if m_col > p_col:
        ret_str += horiz_diff*'LEFT\n'
    print ret_str[:-1] #remove last newline
    
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)