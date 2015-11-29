#!/usr/bin/env python
'''
https://www.hackerrank.com/challenges/angry-professor
'''


import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    # print 'YES' if cenceled, 'NO' if not.
    if sum(a_i <= 0 for a_i in a) < k:
        print 'YES'
    else:
        print 'NO'

