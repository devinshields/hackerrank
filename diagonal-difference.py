#!/usr/bin/env python
'''
https://www.hackerrank.com/challenges/diagonal-difference
'''


import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)


south_east_diag = [a[i][i] for i in range(n)]
south_west_diag = [a[i][n-i-1] for i in range(n)]

print abs(sum(south_east_diag) - sum(south_west_diag))

