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
    http://stackoverflow.com/questions/32406515/using-binary-search-to-find-the-sub-array-with-the-largest-sum-modulo-x-my-solu

    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    http://cplusplus-coding.blogspot.com/2015/07/maximise-sum.html
    http://stackoverflow.com/questions/31113993/maximum-subarray-sum-modulo-m

'''


t = int(raw_input().strip())

for a0 in xrange(t):
    n, m = map(int, raw_input().strip().split(' '))

    arr = map(int,raw_input().strip().split(' '))
    
    # note: the solution indices (i, j) are two dimensional,
    # but the output value is one dimensional (the max subset, modulo M).
    # The dynamic programming insight here is that:
    #
    #   max_modulo_subset(index <= i) = max(max_modulo_subset(index<i), max_modulo_subset(index=i))
    #
    # This way, you can tack on numbers to the input array and the problem formulation still works.
    # The tricks are:
    #
    #   1) loop over the input array and create a cumulative sum array, modulo M.
    #   2) as you go, maintain a binary search tree of all values already seen
    #       x. use this tree to search for the maximum mod-sum ending at element i (that is, search backwards).
    #   3) track the max mod sum across all i
    #
    # Something bugs me about this formulation; it depends on a mutable data structure
    # that updates as we progress through the list. The functional programmer inside
    # me cringes. The example code I've seen is unreadable. I'll think about reformulating...
    #


    # init the answer tracker 
    max_mod_sum = arr[0] % m

    # init the cumulative sum array and the binary search tree.
    # pad the input with zeros (for simpler array boundry logic)
    mod_cum_sum_arr = [0]
    binary_tree     = [0]                   # TODO: get a tree class, then create  one here.
    arr             = [0] + arr + [0]

    # skip the zero pad
    arr_enumerator = enumerate(arr)
    arr_enumerator.next()

    # loop over the array
    for i, el in arr_enumerator:
        # get the current cumulative sum, then update the cumsum sum array
        mod_cum_sum_at_i = (mod_cum_sum_arr[-1] + arr[i]) % m
        mod_cum_sum_arr.append(mod_cum_sum_at_i)

        # update the binary search tree

        # create a candidate for the largest subarray-sum modulo M.
        # the simplest candidate is of course the full cumsum so far (a.k.a.: sum(arr[:i]) )
        max_ending_at_i = mod_cum_sum_at_i

        # search for better options, query the tree
        mod_cum_sum
        

    print

