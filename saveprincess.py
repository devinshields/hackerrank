#!/usr/bin/env python
'''
https://www.hackerrank.com/challenges/saveprincess
'''


def displayPathtoPrincess(m, grid):
    '''  '''
    # make the grid into a single array
    grid_str = ''.join(grid)
    
    # find the piece locations
    m_index = grid_str.index('m')    
    p_index = grid_str.index('p')

    # convert to (y, x) space
    m_coords = (m_index / m, m_index % m)
    p_coords = (p_index / m, p_index % m)
    #print 'm_coords: {}, p_coords: {}'.format(m_coords, p_coords)
    
    # calculate y & x deltas change to move from m_coords to p_coords
    y_delta = p_coords[0] - m_coords[0]
    x_delta = p_coords[1] - m_coords[1]
    #print 'y_delta: {}, x_delta: {}'.format(y_delta, x_delta)
    
    # get the direction of travel as strings
    virt_dir = (y_delta > 0) and 'DOWN' or 'UP'
    horz_dir = (x_delta > 0) and 'RIGHT' or 'LEFT'
    
    # and output
    for i in range(abs(y_delta)):
        print virt_dir
    for i in range(abs(x_delta)):
        print horz_dir
        
    
def main():
    m = input()
    grid = []
    for row_num in xrange(0, m):
        grid.append(raw_input().strip())
    displayPathtoPrincess(m, grid)


if __name__ == '__main__':
  main()

