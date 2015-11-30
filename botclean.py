#!/usr/bin/env python
'''
https://www.hackerrank.com/challenges/botclean
'''


DIRT_CHAR = 'd'


def get_move(posr, posc, d_coords):
    if (posr, posc) == d_coords:
        return 'CLEAN'
    if posr < d_coords[0]:
        return 'DOWN'
    if posr > d_coords[0]:
        return 'UP'
    if posc < d_coords[1]:
        return 'RIGHT'
    if posc > d_coords[1]:
        return 'LEFT'

    
def next_move(posr, posc, board):
    '''  '''
    n = len(board[0])
    bot_coords = (posr, posc)

    # base case, no dirt left
    board_str = ''.join(map(lambda row: ''.join(row), board))
    if DIRT_CHAR not in board_str:
        return
    
    # find remaiing dirty tiles    
    dirt_indices = [d_index for d_index, char in enumerate(board_str) if char == DIRT_CHAR]
    dirt_tile_coords = [(d_index / n, d_index % n) for d_index in dirt_indices]
    #print 'dirt_tile_coords: {}'.format(dirt_tile_coords)
    
    # pick a route. let's do fifo dirt, first index first.
    move = get_move(posr, posc, dirt_tile_coords[0])
    print move
        

def main():
    # bot initial conditions
    bot_coords = tuple(int(i) for i in raw_input().strip().split())
    
    # read in the dirt board
    board = [[j for j in raw_input().strip()] for i in range(5)]

    # try a next move
    next_move(bot_coords[0], bot_coords[1], board)

    
if __name__ == "__main__":
    main()


