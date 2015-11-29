#!/usr/bin/env python
'''

PROBLEM:
    https://www.hackerrank.com/challenges/maximise-sum
        First line contains T, number of test cases to follow.
        Each test case consists of exactly 2 lines.

        First line of each test case contain
        2 space separated integers N and M,
        size of the array and modulo value M. 

        Second line contains N space separated integers
        representing the elements of the array.

    Your target is to find the maximum value of sum of subarray modulo M.
    For every test case output the maximum value asked above in a newline.

NOTES:
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    http://cplusplus-coding.blogspot.com/2015/07/maximise-sum.html
    http://stackoverflow.com/questions/31113993/maximum-subarray-sum-modulo-m

'''


t = int(raw_input().strip())

for a0 in xrange(t):
    n, m = map(int, raw_input().strip().split(' '))

    arr = map(int,raw_input().strip().split(' '))

    # the solution indices (i, j) are two dimensional,
    # but the output value is one dimensional (the max modulo subset).

    print

