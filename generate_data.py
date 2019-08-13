"""

Chad Bloxham. CS 260P Project 1. May 3rd, 2019.

This file implements shell-sort and computes the average runtime for each gap sequence
for various input array sizes.
"""

import time
from generate_gap_seq import *


# Compares values at indices separated by a multiple of the current gap value.
# Corrects inversions by pushing up greater values and placing smaller values
# earlier in the array. Final gap value is 1, so sorting is guaranteed.
def shell_sort(A, n, gaps):
    S = np.array(A, dtype=np.int)
    for gap in gaps:
        for i in range(gap, n):
            j = i
            temp = S[i]
            # test if value at index j is greater than temp
            while j >= gap and S[j - gap] > temp:
                # if so, push up the greater value
                S[j] = S[j-gap]
                j -= gap
            S[j] = temp
    return S


# for each gap sequence and input array size, run five times and compute average runtime
# perform for random arrays and almost sorted arrays
def generate_data():
    # will perform on input arrays ranging from 2^8 and 2^18
    minExp = 8
    maxExp = 18
    N = np.array([2**k for k in range(minExp, maxExp+1)])
    rand_avg_times = np.empty((5, len(N)), dtype=np.float)
    as_avg_times = np.empty((5, len(N)), dtype=np.float)
    for i in range(len(N)):
        gap_seq = [original_seq(N[i]), second_seq(N[i]), pratt_seq(N[i]), fourth_seq(N[i]), my_seq(N[i])]
        for j in range(len(gap_seq)):
            t = np.float(0.0)
            for k in range(5):
                rand_perm = random_permutation(N[i])
                start = time.time()
                s = shell_sort(rand_perm, N[i], gap_seq[j])
                end = time.time()
                t += end - start
            rand_avg_times[j][i] = t / 5.0
            t = np.float(0.0)
            for k in range(5):
                as_perm = almost_sorted_permutation(N[i])
                start = time.time()
                s = shell_sort(as_perm, N[i], gap_seq[j])
                end = time.time()
                t += end - start
            as_avg_times[j][i] = t / 5.0

    # save data to text files
    np.savetxt('N.txt', N)
    np.savetxt('rand_times.txt', rand_avg_times)
    np.savetxt('as_times.txt', as_avg_times)
