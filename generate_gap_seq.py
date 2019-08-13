"""

Chad Bloxham. CS 260P Project 1. May 3rd, 2019.

This file implements functions which generate the gap sequences to be used in shell-sort
on an unsorted array of size n.
"""

import numpy as np


# generate a random permutation of integers from 1 to n
def random_permutation(n):
    s = np.arange(1, n+1, dtype=np.int)
    p = np.random.permutation(s)
    return p


# generate an almost sorted permutations from 1 to n
def almost_sorted_permutation(n):
    s = np.arange(1, n+1, dtype=np.int)
    # create 2log(n) inversions to make it "almost sorted"
    inv = 2*np.log2(n)
    for j in range(int(inv)):
        ind1 = np.random.randint(0, n)
        ind2 = np.random.randint(0, n)
        temp = s[ind1]
        s[ind1] = s[ind2]
        s[ind2] = temp
    return s


# sequence used by Donald Shell.
# Start with n/2 and halve until 1 is reached
def original_seq(n):
    orig = [n/2**k for k in range(1, int(np.log2(n))+1)]
    orig = np.array(orig, dtype=np.int)
    return orig


# decreasing powers of 2 until 1 is reached
def second_seq(n):
    seq2 = [2**k - 1 for k in range(int(np.log2(n)), 0, -1)]
    seq2 = np.array(seq2, dtype=np.int)
    return seq2


# All factors of 2 or 3 less than n
def pratt_seq(n):
    pratt = []
    maxProd = n
    pow3 = 1
    while pow3 < maxProd:
        pow2 = pow3
        while pow2 < maxProd:
            pratt.append(pow2)
            pow2 *= 2
        pow3 *= 3
    # must be in descending order
    pratt = sorted(pratt, reverse=True)
    pratt = np.array(pratt, dtype=np.int)
    return pratt


# 4^k + 3*(2^k-1) + 1 for increasing k until
# n is exceeded
def fourth_seq(n):
    seq4 = []
    maxProd = n
    k = 0
    prod = 1
    while prod < maxProd:
        seq4.append(prod)
        k += 1
        prod = 4**k + 3*(2**(k-1)) + 1
    # must be in descending order
    seq4 = sorted(seq4, reverse=True)
    seq4 = np.array(seq4, dtype=np.int)
    return seq4


# powers of 3 or 5 until n is exceeded
def my_seq(n):
    seq = []
    maxProd = n
    pow5 = 1
    while pow5 < maxProd:
        pow3 = pow5
        while pow3 < maxProd:
            seq.append(pow3)
            pow3 *= 3
        pow5 *= 5
    # must be in descending order
    seq = sorted(seq, reverse=True)
    seq = np.array(seq, dtype=np.int)
    return seq
