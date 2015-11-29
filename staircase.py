#!/usr/bin/env python
'''
https://www.hackerrank.com/challenges/staircase
'''

import sys

n = int(raw_input().strip())

for row in range(n):
    space_count, hash_count= n - row - 1, row + 1
    print '{}{}'.format(' ' * space_count, '#' * hash_count)

