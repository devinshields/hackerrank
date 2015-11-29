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


import bisect


def get_cumsum(int_array):
    cumsum_arr, current_sum = [], 0
    for el in int_array:
        current_sum += el
        cumsum_arr.append(current_sum)
    print 'cumsum_arr: {}'.format(cumsum_arr)
    return cumsum_arr

def apply_modulo_to_list(int_array, m):
    for i in range(len(int_array)):
        int_array[i] %= m
    print 'int_array_modulo: {}\n'.format(int_array)
    return int_array

class BinaryTree(object):
    '''
    https://docs.python.org/2/library/bisect.html#searching-sorted-lists
    '''
    def __init__(self, m, cumsum_arr):
        self.m = m
        self.cumsum_arr = cumsum_arr
        self.cumsum_sorted_arr = sorted(cumsum_arr)
        print 'cumsum_sorted_arr: {}'.format(self.cumsum_sorted_arr)


    def lower_bound(self, partial_sum):
        ''' Find rightmost value less than or equal to partial_sum '''
        i = bisect.bisect_right(self.cumsum_sorted_arr, partial_sum)
        print '\t\tlower_bound_i: {}'.format(i)
        if i:
            bound = self.cumsum_sorted_arr[i-1]
            return bound
        else:
            return 0

    def get_best_span_sum_for_partial_sum(self, partial_sum):
        low_bound = self.lower_bound(partial_sum)
        best_span_sum = (partial_sum - low_bound) % self.m
        print '\tpartial_sum: {}, low_bound: {}, best_span_sum: {}'.format(partial_sum, low_bound, best_span_sum)
        return best_span_sum


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        # read in each test case
        n, m = map(int, raw_input().strip().split(' '))
        int_array = map(int,raw_input().strip().split(' '))

        # create the cumsum array
        cumsum_mod_arr = apply_modulo_to_list(get_cumsum(int_array), m)

        # create a binary tree for O(log(n)) searching
        binary_tree = BinaryTree(m, cumsum_mod_arr)
    
        # create a var for the final answer
        maxsum = int_array[0] % m

        for i, partial_sum in enumerate(cumsum_mod_arr):
            # search for the best matching partial sum,
            # the smallest number bigger than the partial_sum
            max_at_i = binary_tree.get_best_span_sum_for_partial_sum(partial_sum)
            maxsum = max(maxsum, max_at_i)
            print 'i: {}, max_at_i: {}\n'.format(i, max_at_i)

        
        print maxsum


if __name__ == '__main__':
  main()

