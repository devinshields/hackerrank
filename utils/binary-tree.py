#!/usr/bin/env python
'''
use the bisect library - python doesn't have
sorted set and the 'lower_bound()' function 
needed for the iterative solution of the "Maximise Sum"
HackerRank problem:

    https://docs.python.org/2/library/bisect.html

    http://stackoverflow.com/questions/9343739/maplower-bound-equivalent-for-pythons-dict-class

'''


from bisect import bisect_left


def main():
    data = {
        200: -100,
        -50: 0,
        51: 100,
        250: 200
    }
    keys = list(data.keys())
    print data[keys[bisect_left(keys, -79)]]


if __name__ == '__main__':
    main()




