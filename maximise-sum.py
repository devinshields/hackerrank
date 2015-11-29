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

More Notes:

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

'''


#
# Binary search tree:
#
#   https://docs.python.org/2/library/bisect.html#searching-sorted-lists
#


def get_cumsum(int_array, m):
    cumsum_arr, current_sum = [], 0
    for el in int_array:
        current_sum += el
        current_sum %= m
        cumsum_arr.append(current_sum)
    return cumsum_arr


def get_binary_search_tree(cumsum_arr):
    # TODO

    prev_sum := find_next(T, S[i])
    if prev_sum is found:
        max_ending_at_i := (S[i] - prev_sum) % m
    max_mod_sum = max(max_mod_sum, max_ending_at_i)
    return TODO


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        # read in each test case
        n, m = map(int, raw_input().strip().split(' '))
        int_array = map(int,raw_input().strip().split(' '))

        # create the cumsum array
        cumsum_arr = get_cumsum(int_array)

        # create a binary tree for O(log(n)) searching
        binary_tree = get_binary_search_tree(cumsum_arr)
    
        # create temp variable for the final answer, any valid candidate solution will do.
        maxsum = int_array[0] % m

        # for each element in the cumsum array, search for the corresponding
        # element that maximizes:
        #         sum(int_array[i:j]) % m
        for partial_sum in cumsum_arr:
            # search for the best matching partial sum
            binary_tree.search()

            #
            prev_sum = find_next(T, S[i])
            if prev_sum is found:
                max_ending_at_i = (S[i] - prev_sum) % m
            max_mod_sum = max(max_mod_sum, max_ending_at_i)
        
        print


if __name__ == '__main__':
  main()

