#!/usr/bin/env python
'''
https://www.hackerrank.com/challenges/plus-minus
'''



#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


# print decimal ratio of positive, negative, and zeros, each on their own line

counter = {-1: 0, 0: 0, 1: 0}

for el in arr:
    if el == 0:
        counter[el] += 1
    else:
        counter[abs(el)/el] += 1

#
print float(counter[1]) / n
print float(counter[-1]) / n
print float(counter[0]) / n


