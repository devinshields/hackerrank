#!/bin/python

#
n = input()
r, c = [int(i) for i in raw_input().strip().split()]

# build a grid
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

# find the princess, get as (y, x) coordinates
p_index = ''.join(grid).index('p')
p_coords = (p_index / n, p_index % n)


def nextMove(n, r, c, grid):
    ''' params: matrix size, current bot row, current bot column, grid '''
    if r < p_coords[0]:
        return 'DOWN'
    if r > p_coords[0]:
        return 'UP'
    if c < p_coords[1]:
        return 'RIGHT'
    if c > p_coords[1]:
        return 'LEFT'

print nextMove(n, r, c, grid)

